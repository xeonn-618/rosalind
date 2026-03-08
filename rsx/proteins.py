from rsx.data import *
from rsx.tools import *
import requests

def translate(rna:str) -> str:
    '''Translate an RNA sequence into its corresponding amino acid
    sequence.'''
    polypeptide = ''
    i = 0
    while i <= len(rna)-3:
        codon = rna.replace('U','T')[i:i+3]
        polypeptide += codontab[codon]
        i+=3
    return polypeptide

def uniprotget(uniprot_id:str,only_string=True) -> str | None:
    '''Returns the string data of a uniprot id in fasta format.
    only_string returns the entire data, setting it to false will only return the
    protein string part.'''
    url = f"https://rest.uniprot.org/uniprotkb/{uniprot_id}.fasta"
    response = requests.get(url)

    # Check the status code
    if response.status_code == 200:
        print(f"{uniprot_id} Request successful!")
        data = response.text
        if only_string:
            data = data[data.find('\n')+1:].replace('\n', '')
            return data
        return data
    else:
        print(f"Request failed with status code: {response.status_code}")
        