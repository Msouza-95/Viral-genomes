from Bio import SeqIO
from Bio.Seq import Seq 
from utils import findByFrame as findFrame

class Genome:
    
    def __init__(self) -> None:
        self.id =0
        self.gene = 0

class ORF:
    
    def __init__(self,start , end) -> None:
        self.start = start 
        self.end = end



g = Genome()

genomes = []

for seq_record in SeqIO.parse("Data/sequence_Dengue_virus1.fasta","fasta"):
    g.gene= str(seq_record.seq)
    g.id = seq_record.id
    genomes.append(g)


#finaliza leitura

#seq = Seq(genomes[0].gene)
seq = Seq("CCGATGCTTTTTCCGTTGGTTGTTCATCAGAATGGATCTGCTCTCTAATAAAAAACTGTTAGTCTACGTGGACCG")
print(genomes[0].id)

#frame 1
frame1 = findFrame.findByCodons(0, seq)
 
startCodons = frame1[0]
stopCodons = frame1[1]

#frame 2
frame2 = findFrame.findByCodons(1, seq)
startCodons.extend(frame2[0])
stopCodons.extend(frame2[1])

#frame 3
frame3 = findFrame.findByCodons(2, seq)
startCodons.extend(frame3[0])
stopCodons.extend(frame3[1])

#FRAME 1


# print(startCodons)

for i in range(0,len(startCodons)):
    print('--------Start-------------')
    print(startCodons[i].one,startCodons[i].two,startCodons[i].three)
    print(seq[startCodons[i].one],seq[startCodons[i].two],seq[startCodons[i].three])
for i in range(0,len(stopCodons)):
    print('--------Stop-------------')
    print(stopCodons[i].one,stopCodons[i].two,stopCodons[i].three)
    print(seq[stopCodons[i].one],seq[stopCodons[i].two],seq[stopCodons[i].three])

# print(stopCodons[0].one,stopCodons[0].two,stopCodons[0].three)
# print(stopCodons[1].one,stopCodons[1].two,stopCodons[1].three)
# print(stopCodons[len(stopCodons)-1].one,stopCodons[len(stopCodons)-1].two,stopCodons[len(stopCodons)-1].three)




# parte localizar as possiveiz orfs 
lenghtSeq = len(seq)
lenghtStart = len(startCodons)
lenghtStop = len(stopCodons)

ofrs = []
print(lenghtSeq)
init = 0;
for j in range (0,lenghtStop):
    for k in range(init,lenghtStart):
        if(startCodons[k].one < stopCodons[j].three):
           ofr = ORF(startCodons[k].one,stopCodons[j].three)
           ofrs.append(ofr)
           print("achei ofs")
           init += 1
           print(init)
           break
           
        
        
    
            
            
for i in range(0, len(ofrs)):
    print(ofrs[i].start, ofrs[i].end)