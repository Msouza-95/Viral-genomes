import csv

from utils.DTO import Genome

def writer(data):
    
  
    d = len(data)

    
    with open('Results/ORFs_potenciais.csv', 'w', newline='') as file:
        fieldnames = ["Genoma","Frame","ORFS" ,"Start", "End"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        

        writer.writeheader()
        for i in range(0,d):
            c = len(data[i])
            for j in range(0,c ):
                writer.writerow({"Genoma":data[i][j].id,"Frame": data[i][j].frame,"ORFS": data[i][j].orf, "Start":data[i][j].start, "End": data[i][j].end})

