#!/usr/bin/env python3
from value import Number_of_storeys
print("Content-type: text/html")
print("")
print("<html><head><title>hello</title>")
print('<link rel="stylesheet" type="text/css" href="../html/bootstrap.min.css">')
print('<style>body{background-color:#111;}.space{margin-top:10px;}.header{text-align:center;color:#DADADA;}</style>')
print("</head><body><br><br>")
import cgi,cgitb,os
cgitb.enable()
form = cgi.FieldStorage()

"""
lists to contain keys(names) of matrices
"""
mass = []
height = []
stiff = []
# print('<h1 style="color:white">',a,'</h1>')
#for item in range(0,5):
#    list[item]=item

"""
dictionaries to contain key:value pair according to lists above
"""
mass_values = {}
height_values = {}
stiff_values = {}
#for var in list.keys():
#    values[var]=form.getvalue(var)
#    print(values[var])
#print(values)

# print(Number_of_storeys)

"""
Getting the list(or size) of mass matrix
"""
for i in range(0,Number_of_storeys):
	for j in range(0,1):
		temp = "mass "+str(i)+" "+str(j)+" "
		mass.append(temp)

print(mass)

for var in mass:
	# print(var)
	mass_values[var]=form.getvalue(var)
	# print(mass_values.values())
	print("<br><br>")
# print(values)
print('<br><h3 class="header">The Mass matrix is:</h3><br>')
for i in range(0,Number_of_storeys):
	for j in range(0,1):
		mtemp = "mass "+str(i)+" "+str(j)+" "
		print('<h4 class="header">',mass_values.get(mtemp,'11'),'</h4><br>')



"""
Getting the height matrix list
"""

for i in range(0,Number_of_storeys):
	for j in range(0,1):
		htemp = "height "+str(i)+" "+str(j)+" "
		height.append(htemp)

for var in height:
	# print(var)
	height_values[var]=form.getvalue(var)
	# print(height_values.values())
	print("<br>")
print(height_values)
print('<br><h3 class="header">The height matrix is:</h3><br>')
for i in range(0,Number_of_storeys):
	for j in range(0,1):
		mtemp = "height "+str(i)+" "+str(j)+" "
		print('<h4 class="header">',height_values.get(mtemp,'11'),'</h4><br>')




"""
Getting the stiffness matrix list
"""

for i in range(0,Number_of_storeys):
	for j in range(0,1):
		stemp = "stiff "+str(i)+" "+str(j)+" "
		stiff.append(stemp)

for var in stiff:
	# print(var)
	stiff_values[var]=form.getvalue(var)
	# print(height_values.values())
	print("<br>")
print(stiff_values)
print('<br><h3 class="header">The Stiffness matrix is:</h3><br>')
for i in range(0,Number_of_storeys):
	for j in range(0,1):
		stemp = "stiff "+str(i)+" "+str(j)+" "
		print('<h4 class="header">',stiff_values.get(stemp,'11'),'</h4><br>')

# file = open('data.in', 'a')

# for var in list.keys():
#     print('<br>',var,' = ',values[var],'<br>')
    # file.write('# name: ')
    # file.write(var)
    # file.write('\n# type: scalar\n')
    # file.write(values[var])
    # file.write('\n\n\n')
    #for val in values.keys():
    #    print(val,'<br>')
# os.system('rm output')
# os.system('sh octave.sh')
#os.system("octave program.m>nee.out")
# output = open('output', 'r')
print("<br><h4>Output</h4><br>")
# print(output.read())


print("<br></body></html>")
