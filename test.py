from Studentenhuis import Studentenhuis
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
        kad_afd=element["KAD.AFD"]
        kad_sectie=element["KAD.SECTIE"]
        kad_nr=element["KAD.NR"]
        studentenhuis = Studentenhuis(adres, huisnr, bisnr, busnr, gemeente, aant_kamer, kad_afd, kad_sectie, kad_nr)
        resultaat.append(studentenhuis.__str__())
     except Exception as ex:
        print("Foutmelding: " + str(ex))
 return resultaat

print( inlezen_bestand())