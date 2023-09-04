import csv

# Deschideți fișierul CSV pentru citire
with open('Note.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)

    # Creați o listă pentru a stoca elevii și notele lor
    students = []

    # Parcurgeți rândurile din fișier
    for row in reader:
        # Adăugați elevul și notele sale la listă
        students.append({
            'name': row[0],
            'math': int(row[1]),
            'romanian': int(row[2])
        })

    # Cereți utilizatorului ce elev dorește să aleagă
    name = input('Ce elev doriți să alegeți? ')

    # Găsiți elevul în listă
    student = next(student for student in students if student['name'] == name)

    # Cereți utilizatorului ce operațiune dorește să efectueze
    operation = input('Ce operațiune doriți să efectuați? (adunare, scădere, medie aritmetică) ')

    # Efectuați operația dorită
    if operation == 'adunare':
        result = student['math'] + student['romanian']
    elif operation == 'scădere':
        result = student['math'] - student['romanian']
    else:
        result = (student['math'] + student['romanian']) / 2

    # Imprimați rezultatul
    print('Rezultatul este:', result)
