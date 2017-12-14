class Student:
    def __init__(self,par_voornaam,par_naam):
        self.__voornaam=None
        self.__naam=None

        self.voornaam=par_voornaam
        self.naam=par_naam

    def __str__(self):

    @property
    def voonaam(self):
        return self.__voornaam

    @voonaam.setter
    def voonaam(self, value):
        try:
            if value!="":
                self.__voornaam=value
            else:
                raise ValueError
        except (ValueError,TypeError):
            self.__voornaam ="foutief"
            print("Foutmelding: Geen geldige voornaam")

    @property
    def naam(self):
        return self.__naam

    @naam.setter
    def naam(self, value):
        try:
            if value!="":
                self.__naam=value
            else:
                raise ValueError
        except (ValueError,TypeError):
            self.__naam ="foutief"
            print("Foutmelding: Geen geldige voornaam")