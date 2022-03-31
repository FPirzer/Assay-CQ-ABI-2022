import Bio.Entrez as ez

ez.email = "serebix@ŋmx.de"

with ez.einfo() as query:
    xml_string = query.read()
with ez.einfo() as query:
    ncbiDict = ez.read(query)

# To write the xml STRING to a file:
# ncbiQueryInput = open("Query.xml", "w")
# if you want the dictionary to be saved use ez.read(ez.einfo())
# ncbiQueryInput.write(str(ez.einfo().read()))
# ncbiQueryInput.close()

# To just get the pubmed subcategory
# with ez.einfo(db="pubmed") as query:
#     PubMedDict = ez.read(query)
#
# print(PubMedDict["DbInfo"].keys())

print(ncbiDict["DbList"])

with ez.esearch(db="pubmed", term="proechimys[title]", retmax="40") as query:
    record_pub = ez.read(query)
print(record_pub)

# for db in ncbiDict["DbList"]:
#     with ez.esearch(db=db, term="hepatitis", retmax="40") as query:
#         number = ez.read(query)
#         print(number["Count"])
Idlist = record_pub["IdList"]
for ids in Idlist:
    with ez.esummary(db="pubmed", id=ids) as handle:
        record = ez.read(handle)
        print(record[0])
        # print("Journal info\nid:", record[0]["Id"], "\nTitle: ", record[0]["Title"])
