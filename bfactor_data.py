from glob import glob
import numpy as np
import copy
import shutil
import subprocess
import os
import re
import string
import struct
import math




startpath=os.getcwd()
namei= input("enter name data file: ")
namef= input("enter name pdb output file: ")
namepdb= input("enter name pdb file: ")


file1=open(namei,'r')

Listrm=[]

for line in file1:
   # print line
   # print line[5:25]
   
    Listrm.append(float(line))

file1.close()

file1=open(namepdb+'.pdb','r')
filen=open(namef+'.pdb','w')
ki=0
for line in file1:
    if(line[0:4]=='ATOM'):
        ki=ki+1
        kres=int(line[24:26])
        if(ki==1):
            kt=1
            kref=int(line[24:26])
            rmsf=Listrm[kt-1]
        elif(kref !=kres):
            kref=kres
            kt=kt+1
            rmsf=Listrm[kt-1]
       # print line
       # print line
        ar='%6.2f'%rmsf
        stringa=line[0:60]+ar
        filen.write(stringa+'\n')
    elif(line[0:6]=='HEADER'):
        filen.write(line)    
stringa='END'
filen.write(stringa+'\n')
