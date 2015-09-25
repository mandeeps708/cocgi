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
list = []
# print('<h1 style="color:white">',a,'</h1>')
#for item in range(0,5):
#    list[item]=item

#    values = {}
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
		list.append(temp)
print(list)

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
