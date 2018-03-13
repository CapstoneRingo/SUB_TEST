import os

os.system('plink -serial /dev/ttyACM0 -sercfg 115200 8,n,1,X')

os.system('G28.3 X0')
os.system('G1 X1 F40')
