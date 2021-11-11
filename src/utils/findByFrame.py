from Bio.Seq import Seq 

class Position:
    def __init__(self, one , two, three) -> (None):
        self.one = one
        self.two =two 
        self.three = three 
        
        
        
def findByCodons(frame, seq):
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
            positionCodons = Position(i, i+1, i+2)
            startCodons.append(positionCodons)
            
        elif(test == TAA or test == TAG or test == TGA):
            positionCodons = Position(i, i+1, i+2)     
            stopCodons.append(positionCodons)
       
    return startCodons , stopCodons



