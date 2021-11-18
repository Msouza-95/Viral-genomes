from Bio.Seq import Seq
from utils import DTO


def execute(seq, id):
    
    frames = []
    for i in range(1, 3):
        frame = findInFrame(i,seq, id)
        frames.append(frame)
     
    # frame2 = findInFrame(1, seq,id)
    # startCodonsFrame1.extend(frame2[0])
    # stopCodonsFrame1.extend(frame2[1])

    # #frame 3
    # frame3 = findInFrame(2, seq,id)
    # startCodonsFrame1.extend(frame3[0])
    # stopCodonsFrame1.extend(frame3[1])
    
   
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
            positionCodons = DTO.Position(i, i+1, i+2, id, frame)
            startCodons.append(positionCodons)
            
        elif(test == TAA or test == TAG or test == TGA):
            positionCodons = DTO.Position(i, i+1, i+2, id, frame)     
            stopCodons.append(positionCodons)
       
     
     
    return startCodons , stopCodons



