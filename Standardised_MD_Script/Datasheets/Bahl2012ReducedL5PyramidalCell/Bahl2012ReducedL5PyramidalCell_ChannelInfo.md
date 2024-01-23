Channel information
===================

<p style="font-family:arial">Channel information at: T = 6.3 degC, E_rev = 0 mV, [Ca2+] = 5e-05 mM</p>


<h2>nat</h2>

Ion: <b>na</b> |
Conductance expression: <b>g = gmax * m<sup>3</sup> * h </b> |
NeuroML2 file: <a href="../BahlModel/nat.channel.nml">BahlModel/nat.channel.nml</a></div>
<details><summary>Notes</summary>Sodium channel, Hodgkin-Huxley style kinetics.
            Comments from original mod file:
            26 Ago 2002 Modification of original channel to allow variable time step and to correct an initialization
            error.
            Done by Michael Hines(michael.hines@yale.e) and Ruggero Scorcioni(rscorcio@gmu.edu) at EU Advance Course in
            Computational Neuroscience. Obidos, Portugal
            Sodium channel, Hodgkin-Huxley style kinetics.
            Kinetics were fit to data from Huguenard et al. (1988) and Hamill et
            al. (1991)
            qi is not well constrained by the data, since there are no points
            between -80 and -55. So this was fixed at 5 while the thi1,thi2,Rg,Rd
            were optimized using a simplex least square proc.
            Voltage dependencies are shifted approximately from the best
            fit to give higher threshold
            Author: Zach Mainen, Salk Institute, 1994, zach@salk.edu
            May 2006: set the tha -28 mV, vshift 0 and thinf -55 mV to comply with measured
            Somatic Na+ kinetics in neocortex. Kole, ANU, 2006
        </details>

<div><a href="imgs/Bahl2012ReducedL5PyramidalCellnat.inf.png"><img alt="nat steady state" src="imgs/Bahl2012ReducedL5PyramidalCellnat.inf.png" width="350" style="padding:10px 35px 10px 0px"/></a>
<a href="imgs/Bahl2012ReducedL5PyramidalCellnat.tau.png"><img alt="nat time course" src="imgs/Bahl2012ReducedL5PyramidalCellnat.tau.png" width="350" style="padding:10px 10px 10px 0px"/></a>
</div>
</div>

<h2>nap</h2>

Ion: <b>na</b> |
Conductance expression: <b>g = gmax * m </b> |
NeuroML2 file: <a href="../BahlModel/nap.channel.nml">BahlModel/nap.channel.nml</a></div>
<details><summary>Notes</summary>NeuroML2 file automatically generated from NMODL file: ./NEURON/channels/nap.mod</details>

<div><a href="imgs/Bahl2012ReducedL5PyramidalCellnap.inf.png"><img alt="nap steady state" src="imgs/Bahl2012ReducedL5PyramidalCellnap.inf.png" width="350" style="padding:10px 35px 10px 0px"/></a>
<a href="imgs/Bahl2012ReducedL5PyramidalCellnap.tau.png"><img alt="nap time course" src="imgs/Bahl2012ReducedL5PyramidalCellnap.tau.png" width="350" style="padding:10px 10px 10px 0px"/></a>
</div>
</div>

<h2>kca</h2>

Ion: <b>k</b> |
Conductance expression: <b>g = gmax * n </b> |
NeuroML2 file: <a href="../BahlModel/kca.channel.nml">BahlModel/kca.channel.nml</a></div>
<details><summary>Notes</summary>NeuroML2 file automatically generated from NMODL file: ./NEURON/channels/kca.mod</details>

<div><a href="imgs/Bahl2012ReducedL5PyramidalCellkca.inf.png"><img alt="kca steady state" src="imgs/Bahl2012ReducedL5PyramidalCellkca.inf.png" width="350" style="padding:10px 35px 10px 0px"/></a>
<a href="imgs/Bahl2012ReducedL5PyramidalCellkca.tau.png"><img alt="kca time course" src="imgs/Bahl2012ReducedL5PyramidalCellkca.tau.png" width="350" style="padding:10px 10px 10px 0px"/></a>
</div>
</div>

<h2>kfast</h2>

Ion: <b>k</b> |
Conductance expression: <b>g = gmax * n </b> |
NeuroML2 file: <a href="../BahlModel/kfast.channel.nml">BahlModel/kfast.channel.nml</a></div>
<details><summary>Notes</summary>Potassium channel, Hodgkin-Huxley style kinetics
            Comments from original mod file:
            26 Ago 2002 Modification of original channel to allow variable time step and to correct an initialization error.
            Done by Michael Hines(michael.hines@yale.e) and Ruggero Scorcioni(rscorcio@gmu.edu) at EU Advance Course in Computational Neuroscience. Obidos, Portugal
            Potassium channel, Hodgkin-Huxley style kinetics
            Kinetic rates based roughly on Sah et al. and Hamill et al. (1991)
            Author: Zach Mainen, Salk Institute, 1995, zach@salk.edu
        </details>

<div><a href="imgs/Bahl2012ReducedL5PyramidalCellkfast.inf.png"><img alt="kfast steady state" src="imgs/Bahl2012ReducedL5PyramidalCellkfast.inf.png" width="350" style="padding:10px 35px 10px 0px"/></a>
<a href="imgs/Bahl2012ReducedL5PyramidalCellkfast.tau.png"><img alt="kfast time course" src="imgs/Bahl2012ReducedL5PyramidalCellkfast.tau.png" width="350" style="padding:10px 10px 10px 0px"/></a>
</div>
</div>

<h2>km</h2>

Ion: <b>k</b> |
Conductance expression: <b>g = gmax * m </b> |
NeuroML2 file: <a href="../BahlModel/IKM.channel.nml">BahlModel/IKM.channel.nml</a></div>
<details><summary>Notes</summary>NeuroML2 file automatically generated from NMODL file: ./NEURON/channels/IKM.mod</details>

<div><a href="imgs/Bahl2012ReducedL5PyramidalCellkm.inf.png"><img alt="km steady state" src="imgs/Bahl2012ReducedL5PyramidalCellkm.inf.png" width="350" style="padding:10px 35px 10px 0px"/></a>
<a href="imgs/Bahl2012ReducedL5PyramidalCellkm.tau.png"><img alt="km time course" src="imgs/Bahl2012ReducedL5PyramidalCellkm.tau.png" width="350" style="padding:10px 10px 10px 0px"/></a>
</div>
</div>

<h2>sca</h2>

Ion: <b>ca</b> |
Conductance expression: <b>g = gmax * m<sup>2</sup> * h </b> |
NeuroML2 file: <a href="../BahlModel/sca.channel.nml">BahlModel/sca.channel.nml</a></div>
<details><summary>Notes</summary>NeuroML2 file automatically generated from NMODL file: ./NEURON/channels/SlowCa.mod</details>

<div><a href="imgs/Bahl2012ReducedL5PyramidalCellsca.inf.png"><img alt="sca steady state" src="imgs/Bahl2012ReducedL5PyramidalCellsca.inf.png" width="350" style="padding:10px 35px 10px 0px"/></a>
<a href="imgs/Bahl2012ReducedL5PyramidalCellsca.tau.png"><img alt="sca time course" src="imgs/Bahl2012ReducedL5PyramidalCellsca.tau.png" width="350" style="padding:10px 10px 10px 0px"/></a>
</div>
</div>

<h2>ih</h2>

Ion: <b>hcn</b> |
Conductance expression: <b>g = gmax * qq </b> |
NeuroML2 file: <a href="../BahlModel/ih.channel.nml">BahlModel/ih.channel.nml</a></div>
<details><summary>Notes</summary>Deterministic model of kinetics and voltage-dependence of Ih-currents
                in layer 5 pyramidal neuron, see Kole et al., 2006. Implemented by
                Stefan Hallermann.

                Added possibility to shift voltage activiation (vshift) and allowed access to gating variables, Armin Bahl 2009

                Predominantly HCN1 / HCN2
        </details>

<div><a href="imgs/Bahl2012ReducedL5PyramidalCellih.inf.png"><img alt="ih steady state" src="imgs/Bahl2012ReducedL5PyramidalCellih.inf.png" width="350" style="padding:10px 35px 10px 0px"/></a>
<a href="imgs/Bahl2012ReducedL5PyramidalCellih.tau.png"><img alt="ih time course" src="imgs/Bahl2012ReducedL5PyramidalCellih.tau.png" width="350" style="padding:10px 10px 10px 0px"/></a>
</div>
</div>
