#!C:\Users\fiant\AppData\Local\Programs\Python\Python310\python.exe
import re

print("Content-Type: text/html\n\n")
print('<html>')

print('<head>')
print("""
<style>
table, td {
  border: 1px solid black;
  border-collapse: collapse;
}
</style>
""")
print('<title>Python CGI : readTable-files</title>')
print('</head>')

print('<body>')
grade = {
    "A": 4,
    "B+": 3.5,
    "B": 3,
    "C+": 2.5,
    "C": 2,
    "D+": 1.5,
    "D": 1,
    "E": 0
}
# print(grade.keys())
# print(grade.get("A"))

print('<h3>Python CGI : readTable-files</h3>')
txt = []
f = open("002_tableData.txt", "r")
x = f.read()
f.close()

x = re.sub("\n", "", x)
# print(x)
txt = re.split(",", x)
# print(txt)
# print(txt[0])

new_txt = [
    [txt[0],txt[1],txt[2]],
    [txt[3],txt[4],txt[5]],
    [txt[6],txt[7],txt[8]],
    [txt[9],txt[10],txt[11]]
]
# print(new_txt)
# print(new_txt[0][0],new_txt[0][1],new_txt[0][2])

print('<table>')
print('<tr>')
print(f'<td>{new_txt[0][0]}</td>')
print(f'<td>{new_txt[0][1]}</td>')
print(f'<td>{new_txt[0][2]}</td>')
print('</tr>')
print('<tr>')
print(f'<td>{new_txt[1][0]}</td>')
print(f'<td>{new_txt[1][1]}</td>')
print(f'<td>{new_txt[1][2]}</td>')
print('</tr>')
print('<tr>')
print(f'<td>{new_txt[2][0]}</td>')
print(f'<td>{new_txt[2][1]}</td>')
print(f'<td>{new_txt[2][2]}</td>')
print('</tr>')
print('<tr>')
print(f'<td>{new_txt[3][0]}</td>')
print(f'<td>{new_txt[3][1]}</td>')
print(f'<td>{new_txt[3][2]}</td>')
print('</tr>')
print('</table><br>')

if new_txt[1][2] in grade:
    new_txt[1][2] = grade.get("A")
    # print(new_txt[1][2])
if new_txt[2][2] in grade:
    new_txt[2][2] = grade.get("C+")
    # print(new_txt[2][2])
if new_txt[3][2] in grade:
    new_txt[3][2] = grade.get("B")
    # print(new_txt[3][2])
list = [new_txt[1][2],new_txt[2][2],new_txt[3][2]]
avg = sum(list)/len(list)
print(f'<h3>Avg = {round(avg, 2)}</h3>')

print('</body>')

print('</html>')