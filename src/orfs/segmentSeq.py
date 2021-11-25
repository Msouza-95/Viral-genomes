

def execute(genome,orfs):
    
    
    lengthGenome = len(genome)
    linOrfs = len(orfs)
    
    
    for i in range(0,lengthGenome):
        for j in range(0, linOrfs):
            col = len(orfs[j])
            for k in range(0 , col):
                if( genome[i].id == orfs[j][k].id):
                     start = orfs[j][k].start-1
                     end = orfs[j][k].end
                     gene = genome[i].gene
                     cut = gene[start: end]
                     orfs[j][k].seq = cut
                    
    return orfs               