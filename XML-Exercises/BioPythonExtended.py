import Bio.Entrez as ez

ez.email = "serebix@gmx.de"
with ez.esearch(db="pubmed", term="hepacivirus", retmax="10") as query:
    PubMed_ID = ez.read(query)

PubID_list = PubMed_ID["IdList"]
print(PubID_list)

# nucSeq = []
# with ez.esearch(db="nucleotide", term="hepacivirus", retmax="10") as query:
#     nucID = ez.read(query)
#     nucID_list = nucID["IdList"]
#     for ID in nucID_list:
#         with ez.efetch(db="nucleotide", id=ID, retmode="xml") as nuc:
#             nuc_list = ez.read(nuc)
#             nucSeq.append(nuc_list[0]["GBSeq_sequence"])

# protSeq = []
# with ez.esearch(db="protein", term="hepacivirus", retmax="10") as query:
#     protID = ez.read(query)
#     protID_list = protID["IdList"]
#     for ID in protID_list:
#         with ez.efetch(db="protein", id=ID, retmode="xml") as prot:
#             prot_list = ez.read(prot)
#             protSeq.append(prot_list[0]["GBSeq_sequence"])

# geneSeq = []
# with ez.esearch(db="gene", term="hepacivirus", retmax="10") as query:
#     geneID = ez.read(query)
#     geneID_list = geneID["IdList"]
#     for ID in geneID_list:
#         with ez.efetch(db="gene", id=ID, retmode="xml") as gene:
#             gene_list = ez.read(gene)
