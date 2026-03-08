# Rosalind Solutions Repository

### rsx module
Custom made python library to handle simple rosalind tasks, with all functions documented and type checked.

Includes functionality for parsing fasta files, saving files, finding reverse complements and a lot more.

#### `rsx.tools` Function Reference

| Function | Parameters | Returns | Description |
| :--- | :--- | :--- | :--- |
| **`get`** | `dest: str` | `str` | Reads a file at the given path relative to the `rsx` folder and returns its data as a readable string. |
| **`put`** | `data: str`, `file_name`, `directory='Outputs/'`, `project_dir=True` | `None` | Saves string data to a `.txt` file at the specified directory (defaults to an `Outputs/` folder). |
| **`reverse_complement`** | `s: str` | `str` | Takes a DNA string in the 5' to 3' direction and returns its DNA reverse complement, also in the 5' to 3' direction. |
| **`basecount`** | `s: str` | `tuple` | Returns the count of bases in a DNA/RNA string in the format `(A, T, G, C)` or `(A, U, G, C)`. Returns an error message on base mismatch. |
| **`fasta_strings`** | `raw: str` | `dict` | Parses raw FASTA formatted data and returns a dictionary of each sequence in the format `{ID : DNA_string}`. |
| **`hammingdist`** | `s: str`, `t: str` | `int` | Calculates the Hamming distance (number of point mutations) between two strings of equal length. |
| **`transcribe`** | `dna: str` | `str` | Transcribes a 5'-DNA-3' coding strand into its corresponding 5'-mRNA-3' strand (replaces T with U). |
| **`reverseTranscribe`** | `rna: str` | `str` | Reverse transcribes an RNA string back into its corresponding DNA string (replaces U with T). |
| **`transitionCount`** | `s: str`, `t: str` | `int` | Returns the number of transition point mutations between two DNA strings of the same length. |
| **`transversionCount`**| `s: str`, `t: str` | `int` | Returns the number of transversion point mutations between two DNA strings of the same length. |
| **`identifyPair`** | `s1: str`, `s2: str` | `list` | Identifies if two strings contain overlapping snippets. Returns a list of matches containing the substring and their start/stop indices. |

#### `rsx.proteins` Function Reference

| Function | Parameters | Returns | Description |
| :--- | :--- | :--- | :--- |
| **`translate`** | `rna: str` | `str` | Translates an RNA sequence into its corresponding amino acid (polypeptide) sequence by reading codons. |
| **`uniprotget`** | `uniprot_id: str`, `only_string=True` | `str` or `None` | Fetches protein sequence data from the UniProt REST API. If `only_string` is `True`, returns just the clean protein string; if `False`, returns the full raw FASTA text. On failing to fetch the data, it returns None.|

### Solutions/

Contains my own solutions to the rosalind problems over the years.

Solutions are labelled by the tag/code of the problem.

