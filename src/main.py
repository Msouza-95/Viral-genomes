from reading import read
from Mycsv import csv 
from orfs import orf
from orfs import UFM
from orfs import segmentSeq
from Bio.Seq import Seq


# leitura dos dados dos genomas 
genomes =read.execute()

#buscar possiveis ofrs 
ofrsPutativas = orf.execute(genomes)

#estrutura de ofrsPutativas é uma matriz: ofrsPutativas[i][j]


#gravar na csv 
csv.writer(ofrsPutativas)   
    
print("Etapa 1 Finalizou!")

ofrs = segmentSeq.execute(genomes, ofrsPutativas)


#Universal Feature Method (UFM) – Método das Características Universais

UFM.execute(ofrs)

print("Etapa 2 Finalizou!")
# seq = Seq("ABCDEFGAJDKAJDK")

# corte = seq[6:11]


