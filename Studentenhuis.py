from Adres import Adres
class Studentenhuis:
    def __init__(self, par_adres, par_huisnr,par_bisnr, par_busnr, par_gemeente, par_aant_kamer, par_kad_afd ="", par_kad_sectie= "", par_kad_nr=""):

        self.__aant_kamer = 0
        self.__kad_afd = 0
        self.__kad_sectie = None
        self.__kad_nr = None


        self.aant_kamer=par_aant_kamer
        self.kad_afd=par_kad_afd
        self.kad_sectie=par_kad_sectie
        self.kad_nr=par_kad_nr

    def __str__(self):
        return "{0} {1} {2} {3}".format(self.adres, self.huisnr, self.gemeente, self.aant_kamer)


    #Aantal kamers
    @property
    def aant_kamers(self):
        return self.__aant_kamer

    @aant_kamers.setter
    def aant_kamers(self, value):
        try:
            if str(value)!="":
                self.__aant_kamer=int(value)
            else:
                raise ValueError
        except (ValueError,TypeError):
            self.__aant_kamer="foutief"
            print("Foutmelding: Geen geldige aantal kamers")

    #Kad_afd
    @property
    def kad_afd(self):
        return self.__kad_afd

    @kad_afd.setter
    def kad_afd(self, value):
        self.__kad_afd=value

    #Kad_sectie
    @property
    def kad_sectie(self):
        return self.__kad_sectie

    @kad_sectie.setter
    def kad_sectie(self, value):
        self.__kad_sectie=value

    #Kad_nr
    @property
    def kad_nr(self):
        return self.__kad_nr

    @kad_nr.setter
    def kad_nr(self, value):
        self.__kad_nr = value