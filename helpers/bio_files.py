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


def name_out_file(input_fasta,output_fasta = None, name = '_oneline.fasta'):
    if output_fasta is None:
        if input_fasta.endswith('.fasta'):
            return f"{input_fasta[:-len('.fasta')]}{name}"
        else:
            return f"{input_fasta}{name}"
    else:
        return output_fasta

def read_blast_results(path):
    records = []
    with open (path) as file:
        for line in file:
            if line.startswith("Description"):
                info = file.readline().strip()
                index = info.find("  ")
                if index != -1:
                    info = info[:index]
                records.append(info)
                continue
    return records

def write_blast_results(records,path):
    with open (path, "w") as out_file:
        for protein_info in sorted(records):
            out_file.write(protein_info + "\n")



    


        