import os
from helpers.fastq import (
    read_fastq, write_fastq,
    check_gc, check_length, check_quality,
    my_bounds, ensure_dir,
)

def filter_fastq(input_fastq, output_fastq, gc_bounds = (0,100), length_bounds = (0,2**32), quality_threshold = 0):

    """
     Filter reads in a FASTQ file by GC content, length, and mean quality.

     Reads the input file record by record and writes passing reads to folder "filtered". If not exist -
     create folder "filtered".

     Arguments
         input_fastq (str): Path to the input FASTQ file.
         output_fastq (str): Name of the output file. Saved inside the
             'filtered/' directory (created automatically if not exist).
         gc_bounds (int | float | tuple): GC content interval in percent.
             A single number is treated as the upper bound (lower bound
             is 0). Defaults to (0, 100).
         length_bounds (int | float | tuple): Read length interval.
             A single number is treated as the upper bound.
             Defaults to (0, 2**32).
         quality_threshold (float): Minimum mean Phred33 quality.
             Defaults to 0.

     Returns:
         None
     """


    gc_bounds = my_bounds(gc_bounds, 0, 100)
    length_bounds = my_bounds(length_bounds, 0, 2 ** 32)
    ensure_dir("filtered")
    output_path = os.path.join("filtered", output_fastq)
    with open(input_fastq) as in_file, open(output_path, "w") as out_file:
        while True:
            record = read_fastq(in_file)
            if record is None:
                break
            header, seq, plus, qual = record
            if (check_gc(seq, gc_bounds)
                    and check_length(seq, length_bounds)
                    and check_quality(qual, quality_threshold)):
                write_fastq(record, out_file)

from helpers.bio_files import ( read_multiline_fasta, write_oneline_fasta,name_out_file)

def convert_multiline_fasta_to_oneline(input_fasta, output_fasta = None):
    """
    Function to convert multiline fasta to oneline. Create an output path if not exist.
    Arguments:
        input_fasta (str): Path to the input fasta file.
        output_fasta (str): Name of the output fasta file. Defaults to None
    Returns:
        None
    """
    path = name_out_file(input_fasta, output_fasta)
    records = read_multiline_fasta(input_fasta)
    write_oneline_fasta(records, path)

from helpers.bio_files import (read_blast_results, write_blast_results)

def parse_blast_output(input_blasta,output_blasta):
    """
    Function to parse the output of BLAST.

    Arguments:
        input_blasta (str): Path to the input BLAST file.
        output_blasta (str): Name of the output BLAST file.
    """
    records = read_blast_results(input_blasta)
    write_blast_results(records,output_blasta)


        
    
            