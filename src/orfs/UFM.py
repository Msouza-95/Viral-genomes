

def execute(data):
    
    coding = []
    line = len(data)
    print("metodo 1")
    for i in range(0,line):   
        col = len(data[i])
        for j in range(0, col):
           A= [0]*3
           G= [0]*3
           C= [0]*3  
           seq = data[i][j].seq
           lengthSeq = len(seq)
           m= int(lengthSeq/3)
            #precorrer a seq
          # print(seq)
          # print(lengthSeq)
           for q in range(0,lengthSeq,3):
              #no startCodons sempre A vai está sempre na primeira posição e G sempre na terceira posição
                if(q!=0):
                    #quantidade de A na posisão x 
                    #   print("-------")
                    #   print(seq[q])
                    #   print(seq[q+1])
                    #   print(seq[q+2])
                    #   print("-------")
                    if(seq[q]=="A"):
                        A[0]+=1
                    if(seq[q+1]=="A"):
                        A[1]+=1
                    if(seq[q+2]=="A"):
                        A[2]+=1
                        
                    #quantidade de G na posisão x 
                    if(seq[q]=="G"):
                        G[0]+=1
                    if(seq[q+1]=="G"):
                        G[1]+=1
                    if(seq[q+2]=="G"):
                        G[2]+=1
                        
                        #quantidade de G na posisão x 
                    if(seq[q]=="C"):
                        C[0]+=1
                    if(seq[q+1]=="C"):
                        C[1]+=1
                    if(seq[q+2]=="C"):
                        C[2]+=1
                else:
                    A[0]+=1
                    G[2]+=1
            
           for k in range(0,3):
                A[k]= A[k]/m
                G[k]= G[k]/m
                C[k]= C[k]/m
                # print("------")
                # print("A " ,  k,A[k]) 
                # print("C " ,  k,C[k])
                # print("G " ,  k,G[k]) 
                # print("------")
        
            #f1 = PG1 PA2 PC3 + PA1 PC2 PG3 - 2 PC1 PG2 PA3
           f1 =G[0]*A[1]*C[2] + A[0]*C[1]*G[2] - 2*C[0]*G[1]*A[2]
           #f2 = 2 PA1 PG1 - PA2 PG2 - PA3 PG3
           f2 = 2*A[0]*G[0] - A[1]*G[1] - A[2]*G[2] 
           #f3 = PG1 PC1 - PG2 PC2
           f3 = G[0]*C[0]  - G[1]*C[1]     
           #  que precisam ser positivas nas ORFs codificantes. Se alguma variável for negativa a ORF é não 
           # codificante
        
           if(f1>=0 and f2>=0 and f3>=0):
                #Em caso contrário, se calcula a feature
                # F = 20 ( f1 + f2 ) 
                F = 20 * (f1 +f2)
                #GC = PG1 + PG2 + PG3 + PC1 + PC2 + PC3
                GC = G[0]+G[1]+G[2]+C[0]+C[1]+C[2]
                # se GC  > 0.55
                if(GC > 0.55):# se adiciona F = F + 20 f3
                    F = F + 20*f3
                # Por último, uma ORF é codificante se F >= 1
                if(F>1):# é codificante
                    coding.append(data[i][j])
                
                         
    return coding                  



def filterBySize(data):
    
    codons = []
    sizeData = len(data)
    
    for i in range(0,sizeData):
         sizeSeq = len(data[i].seq)
         if(sizeSeq>=300):
             codons.append(data[i])

    return codons