import xml.dom.minidom as mini
xml_string = "<a><b>1</b><c>2</c></a>"
root1 = mini.parseString(xml_string)
root2 = mini.parse("Books.xml")
print(root1.firstChild.childNodes[1].firstChild.nodeValue)

xml_string2 = "<a><b>1</b><b>2</b><b>3</b></a>"
root3 = mini.parseString(xml_string2)

liste_knoten_b2 = root3.getElementsByTagName("b")
summe2=0
for node in liste_knoten_b2:
    summe2 += int(node.firstChild.nodeValue)
print(summe2)
