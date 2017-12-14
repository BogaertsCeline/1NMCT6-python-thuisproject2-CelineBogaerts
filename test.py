from Studentenhuis import Studentenhuis
from Adres import Adres
import requests

#inlezen jason bestand
def __download():
    params={"format":"json","language":"nl"}
    response=requests.get("https://data.kortrijk.be/studentenvoorzieningen/koten.json")
    if response.status_code==200:
        response_jason=response.json()
        return response_jason
    else:
        return None

def inlezen_bestand():
 resultaat = []
 list_json = __download()
 for element in list_json:
     try:
        adres= element["ADRES"]
        huisnr = element["HUISNR"]
        bisnr = element["Bisnr."]
        busnr = element["Busnr."]
        gemeente=element["GEMEENTE"]
        aant_kamer=element["aantal kamers"]
        adres_klas=Adres(adres,huisnr,bisnr,busnr,gemeente)
        studentenhuis = Studentenhuis(aant_kamer, adres_klas)
        #print(studentenhuis)
        #resultaat.append(studentenhuis)
        #adres=Adres(adres,huisnr,bisnr,busnr,gemeente)
        #print(adres)
        resultaat.append(studentenhuis.__str__())
     except Exception as ex:
        print("Foutmelding: " + str(ex))
 return resultaat

print( inlezen_bestand())