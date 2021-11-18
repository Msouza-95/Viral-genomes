from reading import read
from Bio.Seq import Seq 
from Mycsv import csv 
from orfs import orf


# leitura dos dados dos genomas 
genomes =read.execute()

#buscar possiveis ofrs 
ofrsPutativas = orf.execute(genomes)

#gravar na csv 
csv.writer(ofrsPutativas)   
    
print("Etapa 1 Finalizou!")

