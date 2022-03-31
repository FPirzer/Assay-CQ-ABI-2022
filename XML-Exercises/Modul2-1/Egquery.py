import Bio.Entrez as ez

ez.email = "serebix@gmx.de"
handle = ez.read(ez.egquery(term="biopython"))
record = ez.read(handle)
for row in record["eGQueryResult"]:
    print(row["DbName"], row["Count"])
