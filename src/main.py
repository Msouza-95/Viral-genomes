from Bio import SeqIO
from Bio.Seq import Seq 
from utils import findByFrame as findFrame
from utils import DTO, findOrfs

g = DTO.Genome()

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
frame = findFrame.execute(seq)
 
startCodons = frame[0]
stopCodons = frame[1]

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




#  localização das ORFs putativas
ofrsPutativas = findOrfs.execute(startCodons,stopCodons)
                      
 #mostar ofs                      
for i in range(0, len(ofrsPutativas)):
    print(ofrsPutativas[i].start, ofrsPutativas[i].end)