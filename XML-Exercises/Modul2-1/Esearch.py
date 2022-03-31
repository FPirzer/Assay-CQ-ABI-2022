import Bio.Entrez as ez 
ez.email = "christoph-knorr@gmx.de"
with ez.esearch(db="pubmed", term="biopython[title]", retmax="40" ) as query:
    record_pub = ez.read(query)
    
if "19304878" in record_pub["IdList"]:
    print("Your article was found")
    
with ez.esearch(db="nucleotide", term="Cypripedioideae[Orgn] AND matK[Gene]", idtype="acc") as query:
    record_nuc = ez.read(query)
    
    
print(record_nuc["Count"])
print(record_nuc["IdList"])

with ez.esearch(db="nlmcatalog", term="computational[Journal]", retmax="20") as handle:
    record_jou = ez.read(handle)
    
print(record_jou["Count"],"computational journals found")
print("The first 20 are\n",record_jou["IdList"])
