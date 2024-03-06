
from neuromllite.utils import load_simulation_json
from neuromllite.utils import load_network_json
from neuromllite.NetworkGenerator import generate_and_run

import numpy as np
import matplotlib.pyplot as plt

pops_vs_colors = {'Exc':'b','SST':'m','PV':'r','VIP':'g'}

pre_mod_vals = {}
post_mod_vals = {}

def analyse(version):

    sim = load_simulation_json('Sim%s.json'%version)
    net = load_network_json('%s.json'%version)

    net.parameters['weight_scale_SST'] = 1.0
    net.parameters['delay_vip_mod_curr'] = '100s'

    net.parameters['baseline_current_Exc'] = '0.068  nA'
    net.parameters['baseline_current_PV'] = '0.216 nA'
    net.parameters['baseline_current_SST'] = '0.058 nA'
    net.parameters['baseline_current_VIP'] = '0.092 nA'
    #pyr = 1, sst < 6, pv > 10, vip < 4

    traces, events = generate_and_run(sim, 
                                      network=net, 
                                      simulator="jNeuroML",
                                      base_dir='./',
                                      target_dir='./',
                                      return_results=True)

    fig, ax = plt.subplots()
    plt.get_current_fig_manager().set_window_title('Rate traces: %s'%version)

    for key in sorted(traces.keys()):
        if key != "t":
            ts = traces['t']
            vs = traces[key]
            pop = key.split('/')[0]

            color = 'k' # black
            colour = pops_vs_colors[pop]
            ax.plot(ts,vs, label=pop, color=colour)
            ax.legend()
                                    
            plt.xlabel("Time (s)")
            plt.ylabel("(SI units)")

            pre_mod_vals[pop] = vs[0]
            post_mod_vals[pop] = vs[-1]
    
    pops = [pop for pop in pops_vs_colors.keys()]
    rates = [pre_mod_vals[pop]for pop in pops_vs_colors.keys()]
    colors = pops_vs_colors.values()

    print(rates)

    fig, ax = plt.subplots()
    plt.get_current_fig_manager().set_window_title('Steady state rates (start simulation): %s'%version)
    ax.set_ylabel('Avg firing rate (Hz)')
    ax.bar(pops, rates, color=colors)

    fig, ax = plt.subplots()
    plt.get_current_fig_manager().set_window_title('Steady state rates (end simulation): %s'%version)
    ax.set_ylabel('Avg firing rate (Hz)')
    rates = [post_mod_vals[pop]for pop in pops_vs_colors.keys()]
    ax.bar(pops, rates, color=colors)

    print(rates)

def analyse_SST_reduced(version, SST_weights, target_pop, figsize):
    pops = {key: [] for key in target_pop}
    pop_rates = {key: [] for key in target_pop}
    colours = {key: [] for key in target_pop}

    sim = load_simulation_json('Sim%s.json'%version)
    net = load_network_json('%s.json'%version)

    net.parameters['delay_vip_mod_curr'] = '100s'

    net.parameters['baseline_current_Exc'] = '0.068  nA'
    net.parameters['baseline_current_PV'] = '0.216 nA'
    net.parameters['baseline_current_SST'] = '0.058 nA'
    net.parameters['baseline_current_VIP'] = '0.092 nA'

    for i in range(len(SST_weights)):
        net.parameters['weight_scale_SST'] = SST_weights[i]

        traces, events = generate_and_run(sim, 
                                        network=net, 
                                        simulator="jNeuroML",
                                        base_dir='./',
                                        target_dir='./',
                                        return_results=True)
        
        for key in sorted(traces.keys()):
            if key != "t":
                ts = traces['t']
                vs = traces[key]
                pop = key.split('/')[0]
                
                pre_mod_vals[pop] = vs[0]
                post_mod_vals[pop] = vs[-1]

        for pop in target_pop:
            pos = target_pop.index(pop)

            pops[pop].append(str(100 - 100*SST_weights[i]) + "%")
            pop_rates[pop].append(post_mod_vals[target_pop[pos]])

            if SST_weights[i] == 0.6:
                colours[pop].append('pink')
            elif SST_weights[i] == 1.0:
                colours[pop].append('grey')
            else:
                colours[pop].append('silver')

    pop_names = ['Pyr' if z == 'Exc' else z for z in target_pop]

    fig, axs = plt.subplots(1, len(target_pop), figsize=figsize)
    plt.get_current_fig_manager().set_window_title('Steady state rates (start simulation): %s'%version)

    for pop in target_pop:
        if len(target_pop) == 1:
            axs.set_ylabel('%s firing rate (Hz)' % pop_names[0])
            axs.set_xlabel('SST connectivity reduction (%)')
            axs.bar(pops[pop], pop_rates[pop], width=0.8, color=colours[pop])
        else:
            pos = target_pop.index(pop)
            axs[0].set_ylabel('Firing rate (Hz)')
            axs[pos].set_xlabel(pop_names[pos])
            axs[pos].bar(pops[pop], pop_rates[pop], width=0.8, color=colours[pop])

    print(pops)
    print(pop_rates)

if __name__ == '__main__':

    #for v in ['delMolinoEtAl_low_baseline','delMolinoEtAl_high_baseline']:
    #    analyse(v)

    #analyse('delMolinoEtAl_adjusted')

    analyse_SST_reduced('delMolinoEtAl_adjusted', [1.0, 0.8, 0.6, 0.4, 0.2, 0.0], ['Exc'], figsize = (6.4, 4.8))

    analyse_SST_reduced('delMolinoEtAl_adjusted', [1.0, 0.6], ['SST', 'PV', 'VIP'], figsize = (8.5, 4.8))

    plt.show()