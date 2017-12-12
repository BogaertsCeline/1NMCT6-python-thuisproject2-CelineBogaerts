import requests

def download():
    params={"format":"json","language":"nl"}
    response=requests.get("https://data.kortrijk.be/studentenvoorzieningen/koten.json")
    if response.status_code==200:
        response_jason=response.json()
        return response_jason
    else:
        return None

print(download())