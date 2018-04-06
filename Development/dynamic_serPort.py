import subprocess
import serial

cmd1 = ["""find /dev -name ttyAMC0"""]
cmd2 = ["""find /dev -name ttyUSB0"""]
AMCsearch = subprocess.check_output(cmd1,shell=True)
USBsearch = subprocess.check_output(cmd2,shell=True)

result1 = AMCsearch.split("tty")
result2 = USBsearch.split("tty")

if len(result1) != 1 :
    GPIOPort = "/dev/ttyAMC1"
else :
    GPIOPort = "/dev/ttyAMC0"

if len(result2) != 1 :
    TINYPort = "/dev/ttyUSB1"
else :
    TINYPort = "/dev/ttyUSB0"

serPort = serial.Serial(GPIOPort, 115200, timeout=None)
driverPort = serial.Serial(TINYPort, 115200, timeout=None)
