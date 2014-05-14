#!/bin/python
import cgi
import os
import commands
import string
import smtplib
import time
import sys
import re
import os

#--------------------------------------------------------------------------#
# for viewing the tracebacks on the webpage, instead of checking the
# web server's error log all the time.  Syntax errors however have
# to be checked in the web server's erro log file
#--------------------------------------------------------------------------#
sys.stderr = sys.stdout

print "Content-type: text/html"
print

form = cgi.FieldStorage()
form_ok = 0

if ( form.has_key("sentence") ):
	if ( form["sentence"] != "" and
		 form["sentence"].value != "Enter the sentence here and select a database" 
	   ):
		form_ok = 1

if not form_ok:
	print "<HTML><BODY><H1>Error</H1>"
	if not form.has_key("sentence"):
		print "Please enter a sentence. </BODY></HTML>"
		sys.exit(1)
	elif (form["sentence"].value == "Enter the sentence here and select a database"):
		print "Please enter a sentence. </BODY></HTML>"
		sys.exit(1)
	else:
		print "Please select a document collection. </BODY></HTML>"
		sys.exit(1)

sentence = form["sentence"].value
tagging = form["tagging"].value
format = form["format"].value

commands.getstatusoutput("rm -rf sample*")
sample_file = open("sample.txt", "w")
sample_file.write("%s\n" % (sentence))
sample_file.close()

tag = ""
if( tagging == "Thematic Roles" ):
	tag = "--tag=theta"
elif( tagging == "PropBank Arguments" ):
	tag = "--tag=argument"
elif( tagging == "Opinion and Opinion Holder" ):
	tag = "--tag=opinion"

os.putenv("ASSERT", "/home/vinicius/siri/assert-v0.14b")
os.putenv("DISPLAY", "localhost:0.0") 

if( format == "HTML" ):
	out_format = "--html"
elif( format == "plain" ):
	out_format = "--plain"

(i, o, e) = os.popen3("$ASSERT/scripts/assert %s %s sample.txt" % (tag, out_format) )

i.close()
result = o.read()
o.close()

status = e.read()
e.close()
#print "status:", status

if( format == "plain" ):
	print result
elif( format == "HTML" ):
	sentence = re.sub(">", "&gt;", sentence)
	sentence = re.sub("<", "&lt;", sentence)
	sentence = re.sub(r"\n  *", "<br>", sentence)

	output = """
<!doctype html public "-//w3c//dtd html 4.0 transitional//en">
<html>
<head>
   <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
   <meta name="GENERATOR" content="Mozilla/4.76 [en] (X11; U; Linux 2.2.16-22 i686) [Netscape]">
   <title>ASSERT Output</title>
</head>
<body bgcolor="#FFFFFF">

<center><table BORDER=0 WIDTH="80%s" NOSAVE >
<tr ALIGN=CENTER VALIGN=BOTTOM NOSAVE>
<td NOSAVE><img SRC="http://localhost/assert/directions.jpg"></td>

<td><img SRC="http://localhost/assert/assert.jpg" height=100></td>

<td><img SRC="http://localhost/assert/fn.gif" height=85></td>
</tr>
</table></center>

<br>
<hr>
<font size=+2>

<table BORDER=0 width="100%s">
<tr>
<td ALIGN=LEFT VALIGN=TOP width="20%s"><b><font size=+2>Plain Sentence</font></b>
</td>

<td width="80%s"><font size=+2>%s</font>
<br>&nbsp;</td>
</tr>

<tr NOSAVE>
<td COLSPAN="2" NOSAVE>
<hr SIZE=1></td>

<td></td>
</tr>

<tr NOSAVE>
<td ALIGN=LEFT VALIGN=TOP NOSAVE><b><font size=+2>Semantic Parse(s)</font></b></td>
<td>
<font size=+2>
%s
</font>
</td>
</tr>
</table>
<br>

<hr>

<table BORDER=0 COLS=3 WIDTH="100%s" NOSAVE >
<tr ALIGN=CENTER VALIGN=BOTTOM NOSAVE>
<td NOSAVE><img SRC="http://jdialog.colorado.edu/assert/colorado.gif" HSPACE=40 ></td>

<td><img SRC="http://jdialog.colorado.edu/assert/arda_logo.gif" ></td>

<td><img SRC="http://jdialog.colorado.edu/assert/columbia.gif" HSPACE=40 ></td>
</tr>
</table>
</body>
</html>
	""" % ("%", "%", "%", "%", sentence, result, "%")
	print output
