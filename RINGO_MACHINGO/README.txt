General Purpose Documentation for Ringo Machine:

This folder contains all scripts for running, tuning, and testing the overlay placement system known as "Ringo". The most important files are as follows:


-------Class and Function Definitions-------------

These files form the foundation for all others, and define the classes and functions used to control the system.In all files that run the machine, a RINGO object is first created that contains all commands and functions to run the machine. The machine is operated by calling the functions from this object.

ex. In the python interpreter, the following could be entered:
>> from RINGO import *
>> r = RINGO() 	#Create the RINGO object. An intialization sequence will start.
>> r.head.extend() #An example of how to access the head linear actuator. This command will cause the head actuator to extend. 

The files included in this section are:
- RINGO.py: 
- MachineComponents.py:
- MachineLib.py: 


--------Testing Scripts---------------------------

These files are pre-defined scripts used in testing the machine. The header comments instruct the user how to prepare for the test. The test files are:

- Test1_Homing.py
- Test2_Pneumatics.py
- Test3_TrayUnloadReload.py
- Test4_OverlayDispenser.py
- Test5_BackingRemoval.py
- Test6_NonAdhesivePlacement.py
- Test7_FullSystem.py


--------Tuning Scripts----------------------------

Several subsystems need to be tuned to work properly. These scripts are used to find the proper tuning parameters to enable the machine to work properly. 

- BR_Tuning.py
- Tray_Tuning.py
- Jig_Tuning.py

-------Other---------------------------------------

A few other miscellaneous scripts are included (such as a demonstration script). These files have descriptions in the file heading. 
