#PA1106 - Scrapping using library
#Reading XML from a file

import xml.etree.ElementTree as ET
tree = ET.parse("student.xml")
root=tree.getroot()
print("Root Element :" , root.tag)

for student in root.findall("student"):
    name = student.find("name").text
    course = student.find("course").text
    age = student.find("age").text

    print("Name :" , name)
    print("Course :" , course)
    print("Age :" , age)