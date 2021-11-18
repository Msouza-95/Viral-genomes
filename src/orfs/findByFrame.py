from Bio.Seq import Seq
from utils import DTO


def execute(seq, id):
    
    frames = []
    for i in range(0, 3):
        frame = findInFrame(i,seq, id)
        frames.append(frame)
     
    return frames 
        
        
def findInFrame(frame, seq , id):
    TAA = Seq("TAA") #stop-codons
    TAG = Seq("TAG") #stop-codons
    TGA = Seq("TGA")#stop-codons
    ATG = Seq("ATG") #start-codons
    stopCodons = []
    startCodons = []
    lenghtSeq = len(seq)
    for i in range(frame, lenghtSeq,3):
        
        if(i+6>lenghtSeq):
            break
       
        test = Seq(seq[i+1]).join([Seq(seq[i]),Seq(seq[i+2])])
    
        if(test==ATG):
            positionCodons = DTO.Position(i, i+1, i+2, id, frame+1)
            startCodons.append(positionCodons)
            
        elif(test == TAA or test == TAG or test == TGA):
            positionCodons = DTO.Position(i, i+1, i+2, id, frame+1)     
            stopCodons.append(positionCodons)
       
     
     
    return startCodons , stopCodons



