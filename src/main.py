
from reading import read
from Mycsv import csv 
from orfs import orf
from orfs import UFM
from orfs import segmentSeq


pathGenoma = "Data/sequence_SARS_Virus.fasta"
# leitura dos dados dos genomas 
genomes =read.execute(pathGenoma )

#buscar possiveis ofrs 
ofrsPutativas = orf.execute(genomes)

#estrutura de ofrsPutativas é uma matriz: ofrsPutativas[i][j]


#gravar na csv 
csv.orfsPotential(ofrsPutativas)   
    
print("Etapa 1 Finalizou!")

ofrs = segmentSeq.execute(genomes, ofrsPutativas)


#Universal Feature Method (UFM) – Método das Características Universais

coding = UFM.execute(ofrs)

print("Etapa 2 Finalizou!")
# seq = Seq("ABCDEFGAJDKAJDK")

# corte = seq[6:11]
codingFilter = UFM.filterBySize(coding)
csv.orfsCoding(codingFilter)
print("Arquivo salvo no csv")