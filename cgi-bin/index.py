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
print('<h1 class="header">CivilOctave</h1>')
print('<form class="col-lg-12" name="search" action="try.py" method="POST"> \           <div class="input-group" style="width:340px;text-align:center;margin:0 auto;">\             <input class="form-control input-lg space" type="text" name="Soil_type" placeholder="Soil_type">    \
                <br>    \
                <input class="form-control input-lg space" type="text" name="Number_of_storeys" placeholder="Number_of_storeys"><br><input class=" form-control input-lg space" type="text" name="Importance_factor" placeholder="Importance_factor">   \
                <br>    \
                <input class=" form-control input-lg space" type="text" name="Response_reduction_factor" placeholder="Response_reduction_factor">   \
                <br>    \
                <input class=" form-control input-lg space" type="text" name="Zone_factor" placeholder="Zone_factor">  \
                <br>    \
                <input class=" form-control input-lg space" type="text" name="Gravity_acceleration" placeholder="Gravity_acceleration">     \
                <br>    \
                <input class=" form-control input-lg space" type="text" name="Modes_considered" placeholder="Modes_considered"> \
                <br>')

"""
Mass Matrix
"""
#If mass_matrix depends on something from above form
#mass_matrix = form.getvalue('Number_of_storeys')
#print(mass_matrix)
print('<h3 class="header">Mass Matrix</h3><br>')
for row in range(1, 5):
    print('<div class="row">')
    for col in range(1, 5):
        print('<input class="input-lg col-md-3 col-sm-3 col-xs-3 space" type="text" name="Zone_factor" placeholder="m',row,col,'">')
    print('</div>')

"""
Height Storey
"""
print('<h3 class="header">Height storey</h3>')
for row in range(1, 5):
    print('<div class="row">')
    for col in range(1, 2):
        print('<input class="input-lg col-md-12 col-sm-12 space" type="text" name="Zone_factor" placeholder="m',row,col,'">')
    print('</div>')

"""
Stiffness_storey
"""
print('<h3 class="header">Stiffness storey</h3>')
for row in range(1, 5):
    print('<div class="row">')
    for col in range(1, 2):
        print('<input class="input-lg col-md-12 col-sm-12 space" type="text" name="Zone_factor"  placeholder="m',row,col,'">')
    print('</div>')


"""
    <input class="input-lg col-md-3 space" type="text" name="Zone_factor" placeholder="matrix"><input class="input-lg col-md-3 space" type="text" name="Zone_factor" placeholder="matrix"><input class="input-lg col-md-3 space" type="text" name="Zone_factor" placeholder="matrix"> \
"""
print('<br><br>    \
                <input class="btn-lg btn-success" type="submit" value="Submit"> \
            </div></form>')
print("<br></body></html>")
