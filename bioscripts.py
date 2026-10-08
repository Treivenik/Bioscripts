import os
from helpers.fastq import (
    read_fastq, write_fastq,
    check_gc, check_length, check_quality,
    my_bounds, ensure_dir,
)

def filter_fastq(input_fastq, output_fastq, gc_bounds = (0,100), length_bounds = (0,2**32), quality_threshold = 0):
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
    path = name_out_file(input_fasta, output_fasta)
    records = read_multiline_fasta(input_fasta)
    write_oneline_fasta(records, path)
        
    
            