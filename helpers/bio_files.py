import os
def read_multiline_fasta(path):
    records = []                
    header = None              
    seq = []              

    with open(path) as file:
        for line in file:                 
            line = line.strip()         
            if not line:                
                continue

            if line.startswith(">"):  
                if header is not None:
                    records.append((header, "".join(seq)))
                header = line          
                seq = []          

            else:                       
                seq.append(line)  

    if header is not None:
        records.append((header, "".join(seq)))

    return records


def write_oneline_fasta(records,path):
    with open (path, 'w') as out_file:
        for header,seq in records:
            out_file.write(f"{header}\n{seq}\n")


def name_out_file(input_fasta,output_fasta = None, name = '_oneline', form = '.fasta'):
    if output_fasta is None:
        if input_fasta.endswith('.fasta'):
            return f"{input_fasta[:-len('.fasta')]}{name}{form}"
        else:
            return f"{input_fasta}{name}{form}"
    else:
        return output_fasta
    


        