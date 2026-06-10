import re
with open(r"C:\Python Learning\techsupport.txt", "r", errors="ignore") as file:
    content = file.read()

match = re.search(r"^hostname\s+(\S+)", content, re.MULTILINE)

if match:
    print("Hostname:", match.group(1))
else:
    print("Hostname not found")   

