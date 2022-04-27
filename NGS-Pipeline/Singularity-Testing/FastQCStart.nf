nextflow.enable.dsl = 2

//  container "https://depot.galaxyproject.org/singularity/"

process prefetchprocess {
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
  storeDir "${params.outdir}"
  container "https://depot.galaxyproject.org/singularity/sra-tools:2.11.0--pl5262h314213e_0"
  input:
    path sraresult
    val accession
  output:
    path "${accession}*.fastq"
  script:
    """
    fasterq-dump.2.11.0 ${sraresult}
    """
}

process qualitycheck {
  storeDir "${params.outdir}/fastqc/"
  container "https://depot.galaxyproject.org/singularity/fastqc%3A0.11.9--hdfd78af_1"
  input:
    path dumpedfastq
    val accession
  output:
    path "${accession}*.html"
    path "${accession}*.zip", emit:zipout
  script:
    """
    fastqc ${dumpedfastq}
    """
}

process fastpqualicheck {
  storeDir "${params.outdir}/trimmed/"
  container "https://depot.galaxyproject.org/singularity/fastp:0.20.1--h8b12597_0"
  input:
    path dumpedfastq
    val accession
  output:
    path "${accession}*_fastp.fastq"
    path "${accession}*_fastp.html"
    path "${accession}_fastp.json", emit:jsonoutput
  script:
  if(dumpedfastq instanceof List){
    """
    fastp -i ${dumpedfastq[0]} -o ${dumpedfastq[0].getSimpleName()}_fastp.fastq -I ${dumpedfastq[1]} -O ${dumpedfastq[1].getSimpleName()}_fastp.fastq -h ${accession}_fastp.html -j ${accession}_fastp.json
    """
    }else{
    """
    fastp -i ${dumpedfastq} -o ${dumpedfastq.getSimpleName()}_fastp.fastq -h ${dumpedfastq.getSimpleName()}_fastp.html -j ${dumpedfastq.getSimpleName()}_fastp.json
    """
    }
}

process multiquali {
  storeDir "${params.outdir}/multiqc/"
  container "https://depot.galaxyproject.org/singularity/multiqc:1.9--py_1"
  input:
    path multi_input
  output:
    path "multiqc*.html"
  script:
    """
    multiqc .
    """
}

workflow {
  sraresult = prefetchprocess(params.accession)
  dumpedfastq=dumpprocess(sraresult, params.accession)
  fastqc_out=qualitycheck(dumpedfastq, params.accession)
  fastp_out=fastpqualicheck(dumpedfastq, params.accession)
  multiqcinput=fastp_out.jsonoutput.concat(fastqc_out.zipout)
  multiqcinput.view()
  multiquali(multiqcinput.collect())
}
