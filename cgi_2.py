#!/usr/bin/python3.4


text = """Content-type: text/html

<TITLE>CGI 101</TITLE>
<h1>A second CGI Script</h1>
<HR>
<p>Hello, CGI World!</p>
<HR>
<table border=1>
"""

print(text)

for i in range(5):
    print('<tr>')
    for j in range(4):
        print('<td>%d.%d</d>' % (i,j))
    print('</tr>')

print("""
</table>
<HR>
""")
