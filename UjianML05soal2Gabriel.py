from bs4 import BeautifulSoup
import requests

req = requests.get('http://digidb.io/digimon-list/')
soup = BeautifulSoup(req.content, 'html.parser')
# print(soup.prettify())

datalist = soup.select('td') # 0:13
digimons=[]
# Ada 341 digimon di digidb.io
jumlah = 341
for i, k in zip(range(0, len(datalist)+1, int(len(datalist)/jumlah)), range(13, len(datalist)+1, int(len(datalist)/jumlah))):
    digimon = datalist[i:k]
    _id = int(digimon[0].b.string)
    name = digimon[1].a.string
    image = digimon[1].img['src']
    stage = digimon[2].center.string
    _type = digimon[3].center.string
    attribute = digimon[4].center.string
    memory = digimon[5].center.string
    slots = digimon[6].center.string
    hp = digimon[7].center.string
    sp = digimon[8].center.string
    atk = digimon[9].center.string
    defense = digimon[10].center.string
    intelligence = digimon[11].center.string
    speed = digimon[12].center.string
    x = {
        "no": _id,
        "digimon": name,
        "image": image,
        "stage": stage,
        "type": _type,
        "attribute": attribute,
        "memory": memory,
        "equip slots": slots,
        "hp": hp,
        "sp": sp,
        "atk": atk,
        "def": defense,
        "int": intelligence,
        "spd": speed
    }
    digimons.append(x)
import json
with open('digimon.json', 'w', encoding='utf-8') as digifile:
    json.dump(digimons, digifile)