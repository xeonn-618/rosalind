import sys
sys.path.append(sys.path[0] + '/..')

from rsx.tools import reverse_complement, fasta_strings, get, put

data = get('Datasets/rosalind_long.txt')
data = fasta_strings(data)
allStrings = list(data.values())

len_map = [len(a) for a in allStrings]
min_overlap = min(len_map)//2

def superstring(arr: list, min_overlap=4, rotations=0):

    if len(arr) == 1:
        return(arr[0])
    
    if rotations >= len(arr):
        return "".join(arr)
    
    current_frag = arr[0]
    overlap_map = []
    for candidate_frag in arr[1:]:
        min_length = min([len(current_frag), len(candidate_frag)])
        overlap = 0
        i = 1
        while i <= min_length:
            checkString1 = current_frag[len(current_frag)-i:]
            checkString2 = candidate_frag[:i]
            if checkString1 == checkString2:
                overlap = i
            i += 1

        overlap_map.append(overlap)
    
    overlap_map_rc = []

    for candidate_frag in arr[1:]:
        rc_frag = reverse_complement(candidate_frag)
        min_length = min([len(current_frag), len(rc_frag)])
        overlap = 0
        i = 1
        while i <= min_length:
            checkString1 = current_frag[len(current_frag)-i:]
            checkString2 = rc_frag[:i]
            if checkString1 == checkString2:
                overlap = i
            i += 1

        overlap_map_rc.append(overlap)

    new_frag = ''
    max_index = 0
    max_overlap = max(overlap_map)

    if max(overlap_map_rc) <  min_overlap and max(overlap_map) < min_overlap:
        arr.append(arr.pop(0))
        return superstring(arr, rotations=rotations+1)

    if max(overlap_map_rc) > max_overlap and max(overlap_map_rc) >= min_overlap :
        max_overlap = max(overlap_map_rc)
        for index, overlap in enumerate(overlap_map_rc):
            if overlap == max_overlap:
                max_index = index
                break
        overlap_frag = arr[1:][max_index]
        new_frag += current_frag[:len(current_frag)-overlap] + reverse_complement(overlap_frag)[:]

    else:
        for index, overlap in enumerate(overlap_map):
            if overlap == max_overlap:
                max_index = index
                break
        overlap_frag = arr[1:][max_index]
        new_frag += current_frag[:len(current_frag)-overlap] + overlap_frag[:]
    


    arr[0] = new_frag
    del arr[1+max_index]
    return superstring(arr)
        

result = superstring(allStrings, min_overlap=4)

# print(result)
put(result, 'output')
print(f"Result saved at Outputs/output.txt")