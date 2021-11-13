#from Class import orf
from utils import DTO

def execute(startCodons,stopCodons ):
    lenghtStart = len(startCodons)
    lenghtStop = len(stopCodons)

    ofrs = []

    numberOfr =0 
    init = 0;
    for j in range (0,lenghtStop):
        for k in range(init,lenghtStart):
            if(startCodons[k].one < stopCodons[j].three):
                numberOfr += 1
                #ofr = orf.ORF(startCodons[k].one,stopCodons[j].three)
                ofr = DTO.ORF("id","frame",numberOfr,startCodons[k].one,stopCodons[j].three)
                ofrs.append(ofr)
                init += 1
                break
    
    return ofrs