import xml.dom.minidom as mini

book = mini.parse("book.xml")
#Da Atom bei XML files den Zeilenumbruch zu einem Stück Text umwandelt
#muss man das beim Index beachten!
print(book.firstChild.childNodes[9].firstChild.nodeValue)
