import sys
import os
import csv

def Template_Replace(F, O, R):
	with open(F, 'r') as file :
		filedata = file.read()
	filedata = filedata.replace(O, R)
	with open(F, 'w') as file:
		file.write(filedata)
		
Stack = []		

with open(sys.argv[1], 'r') as file:
	reader = csv.reader(file)
	for row in reader:
		os.system("cp templates/JDL.tpl condor_"+row[0]+".jdl") 
		os.system("cp templates/SHELL.tpl pico_"+row[0]+".sh") 
		os.system("chmod 755 pico_"+row[0]+".sh") 
		Template_Replace("condor_"+row[0]+".jdl", "#USER#", sys.argv[2])
		Template_Replace("condor_"+row[0]+".jdl", "#EXEC#", "pico_"+row[0])
		Template_Replace("condor_"+row[0]+".jdl", "#PATH#", sys.argv[3])
		Template_Replace("pico_"+row[0]+".sh", "#NAME#", row[0])
		Template_Replace("pico_"+row[0]+".sh", "#INPUT#", row[1])
		Template_Replace("pico_"+row[0]+".sh", "#YEAR#", row[5])
		Template_Replace("pico_"+row[0]+".sh", "#RUN#", row[4])
		Template_Replace("pico_"+row[0]+".sh", "#WEIGHT#", str(float(row[2])/float(row[3])))
		Template_Replace("pico_"+row[0]+".sh", "#TRIGGER#", row[6])
		Stack.append("condor_"+row[0]+".jdl")
		
for s in Stack:
	os.system("condor_submit "+ s)
