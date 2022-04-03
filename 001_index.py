#!C:\Users\fiant\AppData\Local\Programs\Python\Python310\python.exe

import datetime
now = datetime.datetime.now()

print("Content-Type: text/html\n\n")
print('<html>')
print('<head>')
print('<title>Hello World - First CGI Program</title>')
print('</head>')
print('<body>')
print('<h2><font color="blue">Hello World! This is my first CGI program</h2>')

print(f"Current date and time : ", now.strftime("%Y-%m-%d %H:%M:%S"))

print("""
<ol>
 <li>a</li>
 <li>b</li>
 <li>c</li>
</ol>
""")

print('</body>')
print('</html>')

