# !/usr/bin/python37all
import cgi
import json

# retrieve data
form = cgi.FieldStorage()

if "angle_submit" in form: # if angle was submitted
    angle = form.getvalue('angleslider') # get slider value
    data = {"angle":angle, "zero":'no'} # store values
elif "zero_submit" in form: # if zero was submitted
    data = {"angle":0, "zero":'yes'} # store values (0 as angle)

# put into json
with open('lab5.json', 'w') as f:  
  json.dump(data,f)

# new html page
print('Content-type:text/html\n\n')
print('</html>')
print('<html>')
print('<form action="/cgi-bin/stepper_control.cgi" method="POST">')
print('<input type="range" name="angleslider" min ="0" max="359" value ="500"/><br>')
print('<input type="submit" value="Submit Angle" name="angle_submit" />')
print('<br> <br>')
print('<strong>Or...</strong>')
print('<br> <br>')
print('<input type="submit" value="Zero the position" name="zero_submit" />')
print('</form>')
print('</html>')