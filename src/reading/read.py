from utils import DTO
from Bio import SeqIO

def execute():
    g = DTO.Genome()

    genomes = []

    for seq_record in SeqIO.parse("Data/sequence_Dengue_virus1.fasta","fasta"):
        g.gene= str(seq_record.seq)
        g.id = seq_record.id
        genomes.append(g)

    return genomes