# MReaPy_ABLM2_Extension
Python action script for Reaper. One-click insert and calibration of all ABLM2 instances of the project regarding ID mapping and/or plugin delay compensation.  

# What is it?
These are 5 action scripts you can use to make the ABLM2 plugin of TBProAudio more comfortable to use. 
You may just want to use the "MReaPy_ABLM_InsertAndCalibrate.py" action script, which uses all the other available action scripts and automatically adds two ABLM2 instances before and after your plugin chain, fully calibrated and ready to use. 

# Use
**MReaPy_ABLM_ID.py**
Calibrates all ABLM2 instances in a project to match two instances IDs on a track at a time, which is expected to be the main use case. 

###### MReaPy_ABLM_PDC.py
Calibrates all ABLM2 instances of a project by calculating and applying each FX chain plugin delay compensation (PDC) between two ABLM2 instances.

###### MReaPy-ABLM_Calibrate.py
Triggers both ID and PDC calibration for all ABLM2 instances in the project.

###### MReapy_ABLM_Insert.py 
Automatically inserts two ABLM2 instances before and after the track's FX chain, if any. No calibration performed. 

###### MReaPy_ABLM_InsertAndCalibrate.py
The combination of ABLM_Insert and ABLM_Calibrate. Automatically inserts two ABLM2 instances before and after the track's FX chain, if any. Then calibrates all ABLM2 instances in the project (both ID and PDC).


# Installation 
###### Requirements
- Python 3.9<
- Reaper [SWS/S&M Extension](https://www.sws-extension.org/) 

###### Download 
Download all scripts from this repository and put them in the same folder. 

>sws_python.py and sws_pythoncommands.py are mandatory references that should always be in the same folder of my scripts. The sws_python.py script is the main reference for the Reaper API in order to work, sws_pythoncommands.py are handy functions I wrote for tedious tasks and are referenced in all my scripts (feel free to check them and use them for your own).

Next, add all or any of the scripts as needed using the action list window in Reaper.

>"Actions" → "Show Action List" → "New Action..." → "Load Reascript" → select file → execute or assign a shortcut.




