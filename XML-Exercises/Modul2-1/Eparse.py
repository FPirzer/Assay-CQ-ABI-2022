import Bio.Entrez as ez
ez.email = "christoph-knorr@gmx.de"
handle = open("Homo_sapiens.xml", "b")
records = ez.parse(handle)
for record in records:
    status = record["Entrezgene_track-info"]["Gene-track"]["Gene-track_status"]
    if status.attributes["value"]=="discontinued":
        continue
    geneid = record["Entrezgene_track-info"]["Gene-track"]["Gene-track_geneid"]
    genename = record["Entrezgene_gene"]["Gene-ref"]["Gene-ref_locus"]
    print(geneid, genename)