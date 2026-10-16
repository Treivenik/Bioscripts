import os
def gc_content(seq):
    count=0
    for i in seq.lower():
        if i in 'gc':
            count+=1
    return (count/len(seq))*100

def mean_quality(qual):
    quality_line=[]
    for i in qual:
        real_quality=ord(i)-33
        quality_line.append(real_quality)
    return round(sum(quality_line)/len(quality_line),2)

def my_bounds(bounds, simple_low, simple_high): #надо связать с gc_bounds
    if isinstance(bounds, (int,float)):
        return (simple_low,bounds)
    low, up = bounds
    return (low, up)


def check_gc(seq,gc_bounds): #GC состав рида входит в инетервал?
    low, up = gc_bounds  # использует my_bounds-результат
    gc = gc_content(seq)  # использует gc_content
    return low <= gc <= up

def check_length(seq,length_bounds):
    low,up = length_bounds
    length= len(seq)
    return low <= length <= up


def check_quality(qual,quality_threshold):
    return mean_quality(qual) >= quality_threshold

def read_fastq(file):
    header = file.readline().strip()
    if not header:
        return None                      
    seq = file.readline().strip()
    plus = file.readline().strip()
    qual = file.readline().strip()
    return (header, seq, plus, qual)

def write_fastq(record,file):
    header, seq, plus, qual = record
    file.write(f"{header}\n{seq}\n{plus}\n{qual}\n")
            
def ensure_dir(path):
    os.makedirs(path, exist_ok=True)
             
    
    