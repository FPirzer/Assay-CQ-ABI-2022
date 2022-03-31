from Bio import SeqIO
import Bio.Entrez as ez
ez.email = "christoph-knorr@gmx.de"
handle = ez.efetch(db="nucleotide", id="EU490707", rettype="gb", retmode="text")
print(handle.read())

with ez.efetch(db="nucleotide", id="EU490707", rettype="gb", retmode="text") as handle:
    record1 = SeqIO.read(handle, "genbank")
print(record1.id)

with ez.efetch(db="nucleotide", id="EU490707", retmode="xml") as handle:
    record2 = ez.read(handle)
print(record2[0]["GBSeq_definition"])
print(record2[0]["GBSeq_source"])