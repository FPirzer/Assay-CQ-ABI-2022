nextflow.enable.dsl = 2

params.hashlen=51
params.outdir="results"

process velvet {
  publishDir "${params.outdir}", mode:"move", overwrite:true 
  container "https://depot.galaxyproject.org/singularity/velvet%3A1.2.10--hed695b0_3"
  input:
    path fastq
    val hashlen
  output:
    path "velvetdir"
  script:
    if(fastq instanceof List){
    """
    velveth velvetdir ${hashlen} -shortPaired -fastq -separate ${fastq}
    velvetg velvetdir
    """
    }else{
      """
      velveth velvetdir ${hashlen} -fastq -short ${fastq}
      velvetg velvetdir
      """
    }
}

params.indir=null
workflow {
  fastqchannel=channel.fromPath("${params.indir}/*.fastq").collect()
  fastqchannel.view()
  velvet(fastqchannel, params.hashlen)
}
