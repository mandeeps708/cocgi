#!/usr/bin/python3

print("Content-type: text/html")
print("")
print("<html><head><title>hello</title></head>")
print("<body><br><br>")
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
os.system("octave program.m>nee.out")
output = open('nee.out', 'r')
print("<br><h4>Output</h4><br>")
print(output.read())
print("<br></body></html>")

