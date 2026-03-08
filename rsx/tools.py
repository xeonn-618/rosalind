from pathlib import Path
from .data import PAIRS  # keep importing constants if needed

def get(dest: str) -> str:
    """
    dest -> path to file relative to the rsx folder
    returns data in a readable string
    Works on any OS as long as rsx library is in the same folder as this script
    """
    # Get the directory of THIS script
    project_root = Path(__file__).parent.parent
    # Full path to the file
    file_path = project_root / dest

    # Read the file
    with open(file_path, 'r', encoding='utf-8') as f:
        data = f.read()

    return data

def put(data:str,file_name, directory='Outputs/',project_dir=True) -> None:
    '''
    Takes data in string format and saves it in a .txt file
    at the provided directory (default: Outputs folder) relative to root directory
    with the provided file_name
    '''
    if project_dir:
        project_root = Path(__file__).parent.parent

        with open(f"{project_root}/{directory+file_name+'.txt'}", "w") as f:
            f.write(data)
            f.close()
    else:
        with open(f"/{directory+file_name+'.txt'}", "w") as f:
            f.write(data)
            f.close()

def reverse_complement(s:str) -> str:
    '''
    Takes a DNA string s in 5' to 3' direction and returns
    a DNA reverse complement in the 5' to 3' direction.
    '''
    sc = ''
    for base in s:
        sc += PAIRS.get(base, '')
    return sc[::-1]

def basecount(s:str):
    '''
    Returns the count of ATGC/AUGC of a given DNA/RNA string
    in the form (A, T, G, C) or (A, U, G, C)'''
    counts = {'A':0,'T':0,'C':0,"G":0, 'U':0}
    for base in s:
        if base not in 'ATGCU': return('Base mismatch!')
        counts[base] += 1
    if 'U' in s:
        counts['T'] = counts['U']   
    return (counts['A'],counts['T'],counts['G'],counts['C'])

def fasta_strings(raw:str) -> dict:
    '''
    Returns a dict of each different DNA string in fasta format
    in the raw data in the form {ID : DNA_string}.'''
    split_data = raw.split('>')[1:]
    dict = {}
    blank = ''
    for i in range(len(split_data)):
        end = split_data[i].find('\n')
        label = split_data[i][:end]
        dict[label] = blank.join(tuple((x if x != '\n' else blank for x in split_data[i][end+1:])))
    return dict

def hammingdist(s:str, t:str) -> int:
    '''Return number of point mutations in string T and S.'''
    length = len(s)
    result = tuple([1 if s[x] != t[x] else 0 for x in range(length)])
    return sum(result)

def transcribe(dna:str) -> str:
    '''
    Transcribes a string of 5'-DNA-3' (Coding Strand, i.e mRNA ~ coding strand except for U->T
    into its corresponding 5'-mRNA-3'
    '''
    return dna.replace('T','U')

def reverseTranscribe(rna:str) -> str:
    '''Return the reverse transcript of an RNA string into its
    corresponding DNA string.'''
    return rna.replace('U','T')

def transitionCount(s:str,t:str)->int:
    '''Returns the number of transition point mutations
    in DNA strings S and T'''
    if len(s) != len(t): raise ValueError("DNA Length Mismatch!!!")
    c = 0
    for i in range(len(s)):
        bs,bt = s[i], t[i]
        AG1,AG2 = bs == 'A' and bt =='G', bs =='G' and bt == 'A'
        CT1,CT2 = bs == 'C' and bt =='T', bs == 'T' and bt =='C'
        if AG1 or AG2 or CT1 or CT2:
            c += 1
    return c

def transversionCount(s:str,t:str)->int:
    '''Returns the transversion point mutation count of strings t and s'''
    if len(s) != len(t): raise ValueError("DNA Length Mismatch!!!")
    c = 0
    purine = ['A','G']
    pyrimidine = ['C','T']
    for i in range(len(s)):
        if (s[i] in purine and t[i] in pyrimidine) or (s[i] in pyrimidine and t[i] in purine):
            c += 1
    return c

def identifyPair(s1:str, s2:str):
    '''Identify if two given strings are a pair of snippets which overlap
    from either side. If they are pairs, return ((start1, stop1), (start2, stop2))
    else return none'''

    checked = set({})
    matches = []
    edge1 = len(s1) - 1
    edge2 = len(s2) - 1

    for i1, base1 in enumerate(s1):
        for i2, base2 in enumerate(s2):
            
            if base1 == base2:
                # print(f"Found a match at i1 i2:{i1, i2} of {base1},\nChecking for bigger match") # debug    
                length = 1
                substr1 = s1[i1:i1+length] # check for edge case
                substr2 = s2[i2:i2+length]
                while substr1 == substr2 and length <=edge1 and length <= edge2:
                    # print(f"Found a bigger match!\n->{substr1}") # debug
                    if substr1 not in checked:
                        checked.add(substr1)
                        matches.append([substr1, ((i1, i1+length), (i2, i2+length))])
                    length += 1
                    substr1 = s1[i1:i1+length] # check for edge case
                    substr2 = s2[i2:i2+length]
    return matches