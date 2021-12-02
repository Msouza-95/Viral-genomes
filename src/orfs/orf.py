
from orfs import findByFrame as findFrame
from orfs import  findOrfs
from Bio.Seq import Seq

def execute (genomes):
    
    lenght = 8#len(genomes)
    
    ofrsPutativas = []
    for i in range(7,lenght):
        seq = genomes[i].gene
        id = genomes[i].id
     
        # buscar  dos stopcondos e startcondos nos 3 frames
        frames = findFrame.execute(seq ,id)
        lenghtFrames = len(frames)
        for j  in range(0,lenghtFrames):
            
            startCodons = frames[j][0]
            stopCodons = frames[j][1]
            #  localização das ORFs putativas
            putivas =findOrfs.execute(startCodons,stopCodons)
            ofrsPutativas.append(putivas)
   
        
    return ofrsPutativas