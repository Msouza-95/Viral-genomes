from reading import read
from Bio.Seq import Seq 
from utils import findByFrame as findFrame
from utils import DTO, findOrfs
from Mycsv import csv 


# leitura dos dados dos genomas 
genomas =read.execute()

#seq = Seq(genomes[0].gene)
seq = Seq("CCGATGCTTTTTCCGTTGGTTGTTCATCAGAATGGATCTGCTCTCTAATAAAAAACTGTTAGTCTACGTGGACCG")
#print(genomes[0].id)


# buscar  dos stopcondos e startcondos nos 3 frames
frame = findFrame.execute(seq)
 
startCodons = frame[0]
stopCodons = frame[1]

#  localização das ORFs putativas
ofrsPutativas = findOrfs.execute(startCodons,stopCodons)



#print de test
for i in range(0,len(startCodons)):
    print('--------Start-------------')
    print(startCodons[i].one,startCodons[i].two,startCodons[i].three)
    print(seq[startCodons[i].one],seq[startCodons[i].two],seq[startCodons[i].three])
for i in range(0,len(stopCodons)):
    print('--------Stop-------------')
    print(stopCodons[i].one,stopCodons[i].two,stopCodons[i].three)
    print(seq[stopCodons[i].one],seq[stopCodons[i].two],seq[stopCodons[i].three])

#gravar na csv 
csv = csv.writer(ofrsPutativas)
      
         
for i in range(0, len(ofrsPutativas)):
    print(ofrsPutativas[i].start, ofrsPutativas[i].end)
    
    

