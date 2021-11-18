from utils import DTO
from Bio import SeqIO

def execute():

    genomes = []

    for seq_record in SeqIO.parse("Data/sequence_Dengue_virus1.fasta","fasta"):
        g = DTO.Genome(seq_record.id, seq_record.seq)
        genomes.append(g)
        
        
    return genomes