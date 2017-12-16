import random

from Student import Student
from Adres import Adres
import requests


class Studentenhuis:
    __list_studentenhuizen = []
    __aantal_studenthuizen_in_kortijk=0

    def __init__(self, par_aant_kamer, par_adres=Adres("adres", "huisnr", "bin", "bus", "gemeente"), par_student=[]):
        self.__aant_kamer = 0
        self.__adres = None
        self.__student = []

        self.aant_kamer = par_aant_kamer
        self.adres = par_adres
        self.studenten = par_student
        Studentenhuis.__list_studentenhuizen.append(self)
        Studentenhuis.__aantal_studenthuizen_in_kortijk+=1

    def __str__(self):
        vrije_kamer=self.aant_kamer-len(self.student)
        return "Kamers: {0}, vrije kamer : {1}, {2}".format(self.aant_kamer, vrije_kamer, self.adres)

    # Aantal kamers
    @property
    def aant_kamers(self):
        return self.__aant_kamer

    @aant_kamers.setter
    def aant_kamers(self, value):
        try:
            if str(value) != "":
                self.__aant_kamer = int(value)
            else:
                raise ValueError
        except (ValueError, TypeError):
            self.__aant_kamer = "foutief"
            print("Foutmelding: Geen geldige aantal kamers")

    @property
    def adres(self):
        return self.__adres

    @adres.setter
    def adres(self, value):
        if isinstance(value, Adres):
            self.__adres = value
        else:
            raise ValueError("Geen object van de klasse Adres")

    @property
    def student(self):
        return self.__student

    @student.setter
    def student(self, value):
        if isinstance(value, Student):
            self.__student = value
        else:
            raise ValueError("Geen object van de klasse Student")

    @staticmethod
    def __download():
        params = {"format": "json", "language": "nl"}
        response = requests.get("https://data.kortrijk.be/studentenvoorzieningen/koten.json")
        if response.status_code == 200:
            response_jason = response.json()
            return response_jason
        else:
            return None

    @staticmethod
    def inlezen_bestand():
        resultaat = []
        list_json = Studentenhuis.__download()
        for element in list_json:
            try:
                adres = element["ADRES"]
                huisnr = element["HUISNR"]
                bisnr = element["Bisnr."]
                busnr = element["Busnr."]
                gemeente = element["GEMEENTE"]
                aant_kamer = element["aantal kamers"]
                adres_klas = Adres(adres, huisnr, bisnr, busnr, gemeente)
                Studentenhuis(aant_kamer, adres_klas)
            except Exception as ex:
                print("Foutmelding: " + str(ex))



    @staticmethod
    def zoek_studentenhuizen_in_straat(straat):
        new=[]
        try:
            if straat!="":
                for studentenhuis in Studentenhuis.__list_studentenhuizen:
                    if studentenhuis.adres==straat:
                        #print(studentenhuis)
                        new.append(studentenhuis)
                return new
            else:
                raise ValueError
        except ValueError:
            return "Foutieve straat"

    @staticmethod
    def zoek_studentenhuizen_op_aantal_kamers(par_min,par_max):
        try:
            if par_min>par_max:
                raise ValueError
            else:
                new=[]
                for studentenhuis in Studentenhuis.__list_studentenhuizen:
                    if par_min<studentenhuis.aant_kamer <par_max:
                        new.append(studentenhuis)
                return  new
        except (ValueError, TypeError):
            return "Foutief minimum of maximum of beide"

    @staticmethod
    def zoek_studentenhuis_student(straat,student):
        if isinstance(student,Student):
            for studentenhuis in Studentenhuis.__list_studentenhuizen:
                if studentenhuis.adres==straat:
                    if len(studentenhuis.student) < studentenhuis.aant_kamer:
                        print(student)
                        studentenhuis.student.append(student)
                        return studentenhuis

    @staticmethod
    def geef_random_studentenhuis():
        lijst=Studentenhuis.__list_studentenhuizen
        leng=len(lijst)+1
        getal=random.randrange(0,leng)
        return lijst[getal]

    @staticmethod
    def geef_lijst_studentenhuizen():
        return Studentenhuis.__list_studentenhuizen

    @staticmethod
    def aantal_studentenhuizen_in_kortijk():
        return Studentenhuis.__aantal_studenthuizen_in_kortijk
