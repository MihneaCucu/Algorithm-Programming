def citeste_studenti():
    f = open("studenti.in", "r")
    #citim din fisier cuvintele
    linii_studenti = f.readlines()
    linii = []
    for linie in linii_studenti:
        student = []
        linie = linie.split()
        for cuvant in linie:
            cuvant = cuvant.strip(',')
            student.append(cuvant)
        linii.append(student)
    #student: nume, prenume, grupa, lista de note
    date_formatate_studenti = []
    for linie in linii:
        nume = linie[0]
        prenume = linie[1]
        grupa = linie[2]
        note = linie[3:]
        note = [int(nota) for nota in note]
        date_formatate_student = [nume, prenume, grupa, note]
        date_formatate_studenti.append(date_formatate_student)
    return date_formatate_studenti


date_studenti = citeste_studenti()

def grupe():
    dictionar = {}
    for student in date_studenti:
        grupa = student[2]
        nume = student[0] + ' ' + student[1]
        if grupa not in dictionar:
            dictionar[grupa] = []
        dictionar[grupa].append(nume)
    for grupa in dictionar:
        print(grupa, dictionar[grupa])

grupe()

def promovare(grupa):
    for student in date_studenti:
        if student[2] == grupa:
            if len(student[3]) != 5:
                print(student[0] + ' ' + student[1] + ' ' + "restantier")
            else:
                s = 0
                ok = 1
                for nota in student[3]:
                    if nota < 5:
                        print(student[0] + ' ' + student[1] + ' ' + "restantier")
                        ok = 0
                        break
                    s = s + nota
                if ok == 1:
                    media = float(s/5)
                    print(student[0] + ' ' + student[1] + ' ' + str(media))


k = input("grupa este ")
promovare(k)


def medie(*note):
    return sum(note)//len(note)


def repartizare():
    studenti_repartizati = []
    for student in date_studenti:
        promovare_student = []
        numar_restante = 0
        if len(student[3]) != 5:
            promovare_student.append(student[0] + ' ' + student[1])
            numar_restante = 5-len(student[3])
            promovare_student.append(0)
            promovare_student.append(numar_restante)
        else:
            s = 0
            ok = 1
            for nota in student[3]:
                if nota < 5:
                    promovare_student.append(student[0] + ' ' + student[1])
                    promovare_student.append("restantier")
                    ok = 0
                    numar_restante += 1
                s = s + nota
            if ok == 1:
                media = float(s/5)
                promovare_student.append(student[0] + ' ' + student[1])
                promovare_student.append(media)
                promovare_student.append(0)
            else:
                promovare_student.append(numar_restante)
        studenti_repartizati.append(promovare_student)
    return studenti_repartizati

def sortare_repartizare():
    studenti_repartizati = repartizare()

