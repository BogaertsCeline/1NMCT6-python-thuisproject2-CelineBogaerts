class Adres:
    def __init__(self, par_straat, par_huisnr, par_bisnr, par_busnr, par_gemeente):
        self.__straat = None
        self.__huisnr = None
        self.__bisnr = None
        self.__busnr = None
        self.__gemeente = None

        self.straat = par_straat
        self.huisnr = par_huisnr
        self.bisnr = par_bisnr
        self.busnr = par_busnr
        self.gemeente = par_gemeente

    def __str__(self):

    # Straat
    @property
    def straat(self):
        return self.__straat

    @straat.setter
    def straat(self, value):
        try:
            if value != "":
                self.__straat = value
            else:
                raise ValueError
        except ValueError:
            self.__straat = "Foutief"
            print("Foutmeding: Geen geldig adres!")

    # Huisnr
    @property
    def huisnr(self):
        return self.__huisnr

    @huisnr.setter
    def huisnr(self, value):
        try:
            if value != "":
                self.__huisnr = value
            else:
                raise ValueError
        except ValueError:
            self.__huisnr = "Foutief"
            print("Foutmeding: Geen geldig huisnummer!")

    # Bisnr
    @property
    def bisnr(self):
        return self.__bisnr

    @bisnr.setter
    def bisnr(self, value):
        self.__bisnr = value

    # Busnr
    @property
    def busnr(self):
        return self.__busnr

    @busnr.setter
    def busnr(self, value):
        self.__busnr = value

    # Gemeente
    @property
    def gemeente(self):
        return self.__gemeente

    @gemeente.setter
    def gemeente(self, value):
        try:
            if value != "":
                self.__gemeente = value
            else:
                raise ValueError
        except ValueError:
            self.__gemeente = "foutief"
            print("Foutmelding: Geen geldige gemeente")
