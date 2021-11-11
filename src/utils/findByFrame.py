from Bio.Seq import Seq
from utils import DTO 


def execute(seq):
    
    frame1 = findInFrame(0,seq)
    startCodons = frame1[0]
    stopCodons = frame1[1]

    frame2 = findInFrame(1, seq)
    startCodons.extend(frame2[0])
    stopCodons.extend(frame2[1])

    #frame 3
    frame3 = findInFrame(2, seq)
    startCodons.extend(frame3[0])
    stopCodons.extend(frame3[1])
    
    return startCodons, stopCodons 
        
        
def findInFrame(frame, seq):
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
            positionCodons = DTO.Position(i, i+1, i+2)
            startCodons.append(positionCodons)
            
        elif(test == TAA or test == TAG or test == TGA):
            positionCodons = DTO.Position(i, i+1, i+2)     
            stopCodons.append(positionCodons)
       
    return startCodons , stopCodons



