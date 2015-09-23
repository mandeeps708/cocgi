#!/usr/bin/python3

print("Content-type: text/html")
print("")
print("<html><head><title>hello</title>")
print('<link rel="stylesheet" type="text/css" href="../html/bootstrap.min.css">')
print('<style>body{background-color:#111;}.space{margin-top:10px;}.header{text-align:center;color:#DADADA;}</style>')
print("</head><body><br><br>")

import cgi,cgitb,os
cgitb.enable()
form = cgi.FieldStorage()
list = {'Soil_type':'','Number_of_storeys':'','Importance_factor':'','Response_reduction_factor':'','Zone_factor':'','Gravity_acceleration':'','Modes_considered':''}
values = {}
for var in list.keys():
    values[var]=form.getvalue(var)
    #print(values[var])
#print(values,'\n')
#b = sorted(values)

#Soil_type =  form.getvalue('Soil_type')
#Number_of_storeys=  form.getvalue('Number_of_storeys')
#Importance_factor=  form.getvalue('Importance_factor')
#Response_reduction_factor=  form.getvalue('Response_reduction_factor')
#Zone_factor=  form.getvalue('Zone_factor')
#Gravity_acceleration=  form.getvalue('Gravity_acceleration')
#Modes_considered=  form.getvalue('Modes_considered')

dependent = form.getvalue('Number_of_storeys')
storeys = int(dependent)

print('<form class="col-lg-12" name="search" action="matrix.py" method="POST"> \
	<div class="input-group" style="width:340px;text-align:center;margin:0 auto;">')
"""
Mass Matrix
"""
#If mass_matrix depends on something from above form
#mass_matrix = form.getvalue('Number_of_storeys')
#print(mass_matrix)
print('<h3 class="header">Mass Matrix</h3><br>')
for row in range(0,storeys):
    print('<div class="row">')
    for col in range(0, 1):
        print('<input class="form-control input-lg col-md-3 col-sm-3 col-xs-3 space" type="text" name="mass',row,col,'" placeholder="m',row,col,'">')
    print('</div>')

"""
Height Storey
"""
print('<h3 class="header">Height storey</h3>')
for row in range(0,storeys):
    print('<div class="row">')
    for col in range(0, 1):
        print('<input class="form-control input-lg col-md-12 col-sm-12 space" type="text" name="height',row,col,'" placeholder="h',row,col,'">')
    print('</div>')

"""
Stiffness_storey
"""
print('<h3 class="header">Stiffness storey</h3>')
for row in range(0,storeys):
    print('<div class="row">')
    for col in range(0, 1):
        print('<input class="form-control input-lg col-md-12 \
         col-sm-12 space" type="text" name="stiff',row,col,'" \
         placeholder="s',row,col,'">')
    print('</div>')
print('<br><br><input class="btn-lg btn-success" type="submit" value="Submit">')
print('</div></form>')

mat = open('matrixx', 'w')


print("<h4>Input</h4>")
file = open('data.in', 'a')

for var in list.keys():
    print('<br>',var,' = ',values[var],'<br>')
    file.write('# name: ')
    file.write(var)
    file.write('\n# type: scalar\n')
    file.write(values[var])
    file.write('\n\n\n')
    #for val in values.keys():
    #    print(val,'<br>')
os.system('rm output')
os.system('sh octave.sh')
#os.system("octave program.m>nee.out")
output = open('output', 'r')
print("<br><h4>Output</h4><br>")
print(output.read())
print("<br></body></html>")

