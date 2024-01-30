#!/bin/bash

#current_directory=$(pwd)
#cd ~
#source /home/ixanthakis/wsl_repos/Dissertation_Repos/nsimenv3/bin/activate
#cd $current_directory

python MD-script.py -model Hay2011L5bPyramidalCell -filepath HayModel/ -netfile HayModel/TestL5PC.net.nml \
                    -cellfile HayModel/L5PC.cell.nml -lemsfile HayModel/LEMS_TestL5PC.xml \
                    -start "-0.5" -end "1.0" -step "0.05" -list "(-1.0, -0.5, 1.0)"

python MD-script.py -model Hay2011L5bPyrSoma -filepath HayModel/ -netfile HayModel/L5bPyrCellHayEtAl2011.net.nml \
                    -cellfile HayModel/Soma_AllCML.cell.nml -lemsfile HayModel/LEMS_L5bPyrCellHayEtAl2011.xml \
                    -start "-0.04" -end "0.1" -step "0.005" -list "(-0.01,-0.005,0.01,0.05)"

python MD-script.py -model Bahl2012ReducedL5PyramidalCell -filepath BahlModel/ -netfile BahlModel/pyr_multi_comp_original.net.nml \
                    -cellfile BahlModel/pyr.cell.nml -lemsfile BahlModel/LEMS_pyr_multi_comp_original.xml \
                    -start "-0.5" -end "1.0" -step "0.05" -list "(-1.0, -0.5, 1.0)"

python MD-script.py -model Yao2022HumanL23Pyr -filepath Yao_2022_Model/NeuroML2/ \
                    -netfile Yao_2022_Model/NeuroML2/HL23PYR.net.nml \
                    -cellfile Yao_2022_Model/NeuroML2/HL23PYR.cell.nml \
                    -lemsfile Yao_2022_Model/NeuroML2/LEMS_HL23PYR_sim.xml \
                    -start "-0.5" -end "1.0" -step "0.05" -list "(-1.0, -0.5, 1.0)"

python MD-script.py -model Yao2022HumanL23PV -filepath Yao_2022_Model/NeuroML2/ \
                    -netfile Yao_2022_Model/NeuroML2/HL23PV.net.nml \
                    -cellfile Yao_2022_Model/NeuroML2/HL23PV.cell.nml \
                    -lemsfile Yao_2022_Model/NeuroML2/LEMS_HL23PV_sim.xml \
                    -start "-0.5" -end "1.0" -step "0.05" -list "(-1.0, -0.5, 1.0)"

python MD-script.py -model Yao2022HumanL23SST -filepath Yao_2022_Model/NeuroML2/ \
                    -netfile Yao_2022_Model/NeuroML2/HL23SST.net.nml \
                    -cellfile Yao_2022_Model/NeuroML2/HL23SST.cell.nml \
                    -lemsfile Yao_2022_Model/NeuroML2/LEMS_HL23SST_sim.xml \
                    -start "-0.5" -end "1.0" -step "0.05" -list "(-1.0, -0.5, 1.0)"

python MD-script.py -model Yao2022HumanL23VIP -filepath Yao_2022_Model/NeuroML2/ \
                    -netfile Yao_2022_Model/NeuroML2/HL23VIP.net.nml \
                    -cellfile Yao_2022_Model/NeuroML2/HL23VIP.cell.nml \
                    -lemsfile Yao_2022_Model/NeuroML2/LEMS_HL23VIP_sim.xml \
                    -start "-0.5" -end "1.0" -step "0.05" -list "(-1.0, -0.5, 1.0)"

#pynml-channelanalysis BahlModel/kca.channel.nml BahlModel/sca.channel.nml BahlModel/nat.channel.nml \
#                      BahlModel/pas.channel.nml BahlModel/kfast.channel.nml \
#                      BahlModel/nap.channel.nml BahlModel/IKM.channel.nml BahlModel/ih.channel.nml \
#                      -html -md