
from Class import orf

def execute(startCodons,stopCodons ):
    lenghtStart = len(startCodons)
    lenghtStop = len(stopCodons)

    ofrs = []

    init = 0;
    for j in range (0,lenghtStop):
        for k in range(init,lenghtStart):
            if(startCodons[k].one < stopCodons[j].three):
                ofr = orf.ORF(startCodons[k].one,stopCodons[j].three)
                ofrs.append(ofr)
                init += 1
                break
    
    return ofrs