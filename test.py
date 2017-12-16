from Student import Student
from Studentenhuis import Studentenhuis

#Inlezen bestand
ingelezen=Studentenhuis.inlezen_bestand()


def lijst_studentenhuizen():
    #Print lijst Studentenhuizen
    lijst=Studentenhuis.geef_lijst_studentenhuizen()

    print("\n Dit zijn alle studentenhuizen:")
    for element in lijst:
        print(element)

#lijst_studentenhuizen()

def studentenhuizen_zoeken():
    straat="Sint-Denijsestraat"
    lijst=Studentenhuis.zoek_studentenhuizen_in_straat(straat)

    print("\n Dit zijn alle studentenhuizen met als straat {0}:".format(straat))
    for element in lijst:
        print(element)

#studentenhuizen_zoeken()

def aantal_kamers():
    mini=10
    maxi=50
    lijst=Studentenhuis.zoek_studentenhuizen_op_aantal_kamers(mini,maxi)

    print("\nDit zijn alle studentenhuizen met kamers tussen {0} en {1}".format(mini,maxi))
    for element in lijst:
        print(element)

#aantal_kamers()

def registratie_student():
    voornaam="Celine"
    naam="Bogaerts"
    straat="Sint-Denijsestraat"
    student1=Student(voornaam,naam)
    registratie=Studentenhuis.zoek_studentenhuis_student(straat,student1)

    print("\nIn die studentenhuis zijt de persoon nu:")
    print(registratie)

#registratie_student()

def random_studentenhuis():
    random=Studentenhuis.geef_random_studentenhuis()

    print("\nDit is een random studentenhuis:")
    print(random)

#random_studentenhuis()

def aantal_studentenhuizen():
    aantal=Studentenhuis.aantal_studentenhuizen_in_kortijk()

    print("\nDit is het aantal studentenhuizen in Kortijk: {0}".format(aantal))

#aantal_studentenhuizen()