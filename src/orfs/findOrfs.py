#from Class import orf
from utils import DTO

def execute(startCodons,stopCodons ):
    lenghtStart = len(startCodons)
    lenghtStop = len(stopCodons)
   
    ofrs = []

    numberOfr =0 
    init = 0
    for j in range (0,lenghtStop):
        for k in range(init,lenghtStart):
            if(startCodons[k].one < stopCodons[j].three):
                numberOfr += 1
                #ofr = orf.ORF(startCodons[k].one,stopCodons[j].three)
                
                ofr = DTO.ORF(stopCodons[j].id,stopCodons[j].frame,numberOfr,startCodons[k].one+1,stopCodons[j].three+1)
               
                ofrs.append(ofr)
                init += 1
                break
    
    return ofrs