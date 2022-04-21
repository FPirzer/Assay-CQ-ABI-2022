nextflow.enable.dsl=2

process count_codon {
  publishDir "${params.outdir}", mode: 'copy', overwrite: true
  input:
    tuple path(inputname), val(searchword)
    //path inputname
    //val searchword
  output:
    path "${searchword}.wordcount", emit: wordcount
  script:
    """
    grep -o -i ${searchword} ${inputname}  | wc -l > ${searchword}.wordcount
    """
}

workflow {
  inputchannel = channel.fromPath(params.inputfilepath)
  condons= channel.fromList(["ATG","TGA","TAG","TAA"])
  combinedchannel= inputchannel.combine(condons)
  count_codon(combinedchannel)
}
