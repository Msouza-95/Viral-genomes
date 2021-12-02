import numpy as np

def UFM2(orf): # UNIVERSAL FEATURE METHOD 2013
    
    stops = ['TAA','TAG','TGA']
    
    Nuc=np.zeros((4,3,3),dtype=float) # nuc,pos,frame 

    hs={'A':0,'G':1,'C':2,'T':3}

    F=np.zeros((3),dtype=float)

    # sequence length ckeck 
    
    n=int((len(orf)-3)/3)
    
    inc=1/3/n
    
    if 3*(n+1)!=len(orf):
        print("WRONG ORF SIZE = ",len(orf))
        return 0,0
    
    # counting nucleotide frequencies at each codon position and frame
#     inv_n=1/n
    
    for f in range(3):
        
        nstops=0
        
        for p in range(f,n,3):
            codon_name = ''.join(tuple(orf[p:p+3]))
            if codon_name in stops:
                nstops+=1/n #2
            for c in range(3):
                Nuc[hs[codon_name[c]],c,f]+=inc #1/inv_n
        
    # evaluating discriminant function for each frame
       
        den=1 # versao do denominador da formula do artigo - 0.01 to avoid div by zero é eliminado efetuando a multiplicação apenas das freqs não nulas

        if Nuc[2,0,f]>0:
            den*=Nuc[2,0,f]

        if Nuc[1,1,f]>0:
            den*=Nuc[1,1,f]
        
        if Nuc[0,2,f]>0:
            den*=Nuc[0,2,f]
            
        F[f]=Nuc[0,0,f]*Nuc[1,0,f]/(den +nstops)
        
    # applying main decision criterium to avoid unnecessary calculations
        if f>0 and F[f]>F[0]: # main decision criterium
            return f, -1
                  
    # applying secondary decision criteria
    
#     if Nuc[1,0,0]>Nuc[1,1,0]: # and Nuc[0,1,0]>Nuc[3,0,0]: # os dois criterios são fortes demais para SARS-Cov-2 !
        return F[0], 1
#     else: 
#         return 0, -2

#     return(1)