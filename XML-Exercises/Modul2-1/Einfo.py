import Bio.Entrez as ez 
ez.email = "christoph-knorr@gmx.de"

with ez.einfo() as query:
    xml_string = query.read()
with ez.einfo() as query:
    parse_dict = ez.read(query)

print(xml_string)
print(parse_dict["DbList"])

with ez.einfo(db="pubmed") as query:
    PubMedDict = ez.read(query)
    
print(PubMedDict["DbInfo"].keys())
for field in PubMedDict["DbInfo"]["FieldList"]:
    print("%(Name)s, %(FullName)s, %(Description)s" % field)