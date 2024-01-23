#!/bin/bash

current_directory=$(pwd)
cd ~
source /home/ixanthakis/wsl_repos/Dissertation_Repos/nsimenv3/bin/activate
cd $current_directory

python MD-script.py -model Hay2011L5bPyramidalCell -filepath HayModel/ -netfile HayModel/TestL5PC.net.nml \
                    -cellfile HayModel/L5PC.cell.nml -lemsfile HayModel/LEMS_TestL5PC.xml

python MD-script.py -model Bahl2012ReducedL5PyramidalCell -filepath BahlModel/ -netfile BahlModel/pyr_multi_comp_original.net.nml \
                    -cellfile BahlModel/pyr.cell.nml -lemsfile BahlModel/LEMS_pyr_multi_comp_original.xml

#pynml-channelanalysis BahlModel/kca.channel.nml BahlModel/sca.channel.nml BahlModel/nat.channel.nml \
#                      BahlModel/pas.channel.nml BahlModel/kfast.channel.nml \
#                      BahlModel/nap.channel.nml BahlModel/IKM.channel.nml BahlModel/ih.channel.nml \
#                      -html -md