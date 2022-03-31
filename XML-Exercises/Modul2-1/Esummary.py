import Bio.Entrez as ez 
ez.email = "christoph-knorr@gmx.de"

id_list = ["19304878", "18606172", "16403221", "16377612", "14871861", "14630660"]

for ids in id_list:
    with ez.esummary(db="pubmed", id=ids) as handle:
        record = ez.read(handle)
    
    print("Journal info\nid:",record[0]["Id"],"\nTitle: ",record[0]["Title"])