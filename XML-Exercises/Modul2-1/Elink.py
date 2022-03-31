import Bio.Entrez as ez

ez.email = "christoph-knorr@gmx.de"
pmid = "19304878"
record = ez.read(ez.elink(dbfrom="pubmed", id=pmid))
print(record)
