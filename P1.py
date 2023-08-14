import csv #import modul csv implicit

nume_fisier="P1note.csv" #calea catre fisierul tinta

#listare intreg document .csv
with open(nume_fisier, 'r', newline='') as csvfile:
    catalog_read = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in catalog_read:
        print (row [0],",", row[1],",",row[2],",", row[3])
