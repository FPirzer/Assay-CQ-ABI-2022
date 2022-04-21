nextflow.enable.dsl = 2

//  container "https://depot.galaxyproject.org/singularity/"

process prefetch {
  storeDir "${params.outdir}"
  container "https://depot.galaxyproject.org/singularity/sra-tools:2.11.0--pl5262h314213e_0"
  input:
    val accession
  output:
    path "${accession}/${accession}.sra"
  script:
    """
    prefetch $accession
    """
}

process dumpprocess {
  publishDir "${params.outdir}", mode: "copy", overwrite: true
  container "https://depot.galaxyproject.org/singularity/sra-tools:2.11.0--pl5262h314213e_0"
  input:
    path sraresult
    val accession
  output:
    path "${accession}.fastq"
  script:
    """
    fasterq-dump.2.11.0 ${accession}.sra
    """
}

workflow {
  sraresult = prefetch(params.accession)
  dumpprocess(sraresult, params.accession)
}
