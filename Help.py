"""
def analizaBitke(vojska):
  dolzina = len(vojska[0])
  a = 0
  b = 0
  sezprez = []
  for x in range(dolzina):
    if vojska[0][x] > vojska[1][x]: #[0] = seznam, [x] = index seznam
      a +=1
    elif vojska[0][x] < vojska[1][x]:
      b +=1
  return [a,b]
vojska = [[2, 3, 6, 8, 2, 4, 6], [2, 3, 5,  6,7, 5, 4]]
print(analizaBitke(vojska))
"""
"""
def najboljsiPriblizek(sezS,ciljnoStevilo):
  bliz = float("inf")
  prvost = 0
  drugost = 0
  for x in sezS: 
    for y in sezS:
      if abs((x + y)-ciljnoStevilo) < bliz:
        bliz = abs(x+y-ciljnoStevilo)
        prvost = x    
        drugost = y
  return([ciljnoStevilo,prvost,drugost,bliz])
        
print(najboljsiPriblizek([19, 23, 29, 31, 37, 61, 67, 71, 89, 97], 543))
"""
"""
import requests
url = "https://api.frankfurter.app/latest"
call = requests.get(url).json()
kljuc = max(call["rates"],key = call["rates"].get)
print(kljuc,call["rates"][kljuc])
"""
