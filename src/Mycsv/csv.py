import csv

def writer(data):
    d = len(data)
    
    with open('Results/ORFs_potenciais.csv', 'w', newline='') as file:
        fieldnames = ["Genoma","Frame","ORFS" ,"Start", "End"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        

        writer.writeheader()
        for i in range(0,d):
            writer.writerow({"Genoma":data[i].id,"Frame": data[i].frame,"ORFS": data[i].orf, "Start":data[i].start, "End": data[i].end})

