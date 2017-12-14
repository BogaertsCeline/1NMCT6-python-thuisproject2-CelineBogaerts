from Student import Student
from Adres import Adres


class Studentenhuis:
    def __init__(self, par_aant_kamer,
                 par_adres=Adres("adres", "huisnr", "bin", "bus", "gemeente"),par_student=[]):
        self.__aant_kamer = 0
        self.__adres = None
        self.__student=None

        self.aant_kamer = par_aant_kamer
        self.adres = par_adres
        self.studenten=par_student

    def __str__(self):
        return "Kamers: {0}, {1}".format(self.__aant_kamer, self.__adres)

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
        return  self.__student

    @student.setter
    def student(self, value):
        if isinstance(value,Student):
            self.__student=value
        else:
            raise ValueError("Geen object van de klasse Student")