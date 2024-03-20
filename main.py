from bs4 import BeautifulSoup
import lxml
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "Upgrade-Insecure-Requests": "1",
    "Accept-Encoding": "gzip, deflate, br",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
}

response = requests.get("https://www.amazon.ca/Solo-Leveling-Manga-Set-1-6/dp/B0BZDX8169/ref=sr_1_2?crid=DX3NIQMYC4LT&dib=eyJ2IjoiMSJ9.7Gp4I4sSYsUzZ0jTVozILePCEz5f-gzxnRvgwlteiVTABi0BH7qWX0o3HMxCRaZ5ANUnJLCJEIK10A1kZiKE5fgrxRcOYhtaAUn1AbI0HWmLOzO_VwOruQ6fY6qUbTPvgYg7OFDftcSe5aIJ9ZxZBaQ5BChjdEzW0diP-u7NYNBg4Mu2uMzEMJ-rYEnyPdgZ1rCa3tepl4vjo-adLYv_3pRw8bIzEDNaOAfHpigOD6tjqsR48bEiG4dgZwKUpVmAV9m-r4z6xGYiKsfwnlBSXRuAGfOHByl1k0SMTKstgYg.ioq4xEh_s6k2hMLoP3ztgEK0c-EiFEDeRH3yZWCw0WE&dib_tag=se&keywords=solo+leveling+box+set&qid=1710937821&sprefix=solo+leve%2Caps%2C367&sr=8-2", headers=headers)
contents = response.text

soup = BeautifulSoup(contents, 'lxml')

print(soup.prettify())
