#!/usr/bin/python2
 
import cgi,cgitb
import commands
import random
 
'''
The Common Gateway Interface (CGI) is a standard for writing programs that can interact through a Web server with a client running a Web browser.
    CGI is the standard for programs to interface with HTTP servers.
    CGI programming is written dynamically generating webpages that respond to user input or webpages that interact with software on the server
'''
 
cgitb.enable()
 
''' cgitb.enable() activates special exception handler that will display detail reports in the web browser if any error occurs.'''
 
 
print "Content-type:text/html"
print ""
 
'''above tell the client what kind of data is following , eg. here data specified is HTML 
The line "Content-type: text/html" is special piece of text that must be the first thing sent to the browser by any CGI script.
 
print "" ->it specifies the end of the headers
'''
 
 
data = cgi.FieldStorage()      #To get at submitted form data, it’s best to use the FieldStorage class.
lang = data.getvalue('lang')   #chosen language is extracted from html value that is in data
 
cmd = ""
 
 
#port = str(random.random())[-4:]
#print commands.getoutput("whoami")
 
if lang=='python':
	commands.getstatusoutput("sudo docker run -it sahu")  #opens a docker containers named satyam which is 		#centos6 image 
	commands.getstatusoutput("service shellinaboxd restart") # it starts shellinabox which is a software to 	#run various shells like of python php ruby etc on web browsers.
	print "Username : pyt"  
	print "Password : pyt"
	#inside the container we have added a new user having python shell above named as pyt and password pyt
	print "<a href='https://172.17.0.2:4200'> Go to Python </a>"
	#http: //IP of Container:4200 -> open this ip in browser.-
	#Shellinabox listens on port no 4200 by default and responds to client at request at this port
 
 