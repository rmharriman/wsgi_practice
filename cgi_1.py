#!/usr/bin/python3.4

"""
Apache version is 2.4.10
Needed to load the cgi module using the builtin in apache2 app
a2enmod cgid

Modify the cgid mod in /etc/apache2/mods-enabled/cgid.conf
Add these lines:

# Directive tells Apache where cgi scripts are
ScriptAlias "/cgi-bin/" "/srv/cgi-bin/"


<Directory "/srv/cgi-bin">
    Options ExecCGI
    Require all granted
    SetHandler cgi-script
</Directory>

Place CGI scripts in the /srv/cig-bin folder on the webserver and adjust permissions accordingly (755)

Images are in the html root folder. Link is an absolute path there.

"""

text = """Content-type: text/html

<TITLE>CGI 101</TITLE>
<h1>A second CGI Script</h1>
<HR>
<p>Hello, CGI World!</p>
<IMG src="http://localhost/ppsmall.gif" BORDER=1 ALT=[image]>
<HR>
"""

print(text)
