from utils import DTO
from Bio import SeqIO

def execute(pathGenoma):

    genomes = []

    for seq_record in SeqIO.parse(pathGenoma,"fasta"):
        g = DTO.Genome(seq_record.id, seq_record.seq)
        genomes.append(g)
        
        
    return genomes