# mn is count of mature rabbits in nth month
# yn is count of young rabbits in nth month

generations = [(0,1),(1,0)]
n = 81
m = 18# here, m is different from m0 or m1, its the life span of the rabbits

for gen in range(1,n-1):
    n_actual = gen + 2
    m0, y0 = generations[gen] # n-1'th gen
    if n_actual <= m:
        m1, y1 = m0+y0, m0
        generations.append((m1,y1))
    else:
        ym = generations[n_actual-1-m][1] # no of younge rabbits of n-m generation
        m1, y1 = m0+y0-ym, m0
        generations.append((m1,y1))

print(sum(generations[-1]))


    
    