nextflow.enable.dsl=2

process split_file {
  publishDir "./Trash", mode:"move", overwrite:true
  input:
    path infile
  output:
    path "*.fasta"
  script:
    """
    python /home/cq/Githubstuff/Assay-CQ-ABI-2022/NGS-Pipeline/christofParser.py ${infile}
    """
}

// process count_word {
//
//   input:
//     path "*.fasta"
//     val word
//   output:
//     path "*.fasta.wordcount"
//   script:
//   """
//   grep -o -i ${word} ${*.fasta} > grepresult
//   cat grepresult | wc -l > ${*.fasta}.wordcount
//   """
// }

workflow {
  inchannel = channel.fromPath(params.infile)
  splitfiles = split_file(inchannel)
// count_word(splitfiles.flatten(), params.word)
}
