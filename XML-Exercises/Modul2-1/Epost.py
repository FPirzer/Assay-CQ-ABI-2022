import Bio.Entrez as ez 
ez.email = "christoph-knorr@gmx.de"

id_list = ["19304878", "18606172", "16403221", "16377612", "14871861", "14630660"]
print(ez.epost("pubmed", id=",".join(id_list)).read())

search_results = ez.read(ez.epost("pubmed", id=",".join(id_list)))
webenv = search_results["WebEnv"]
query_key = search_results["QueryKey"]