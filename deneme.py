import python_veritabanı
import collections
def sayı_tekar(liste):
  tekar=[]
  
  for liste_uzunluk in range(len(liste)):
    sayı=0
    for tekar_uzunluk in range(len(liste)):
      if liste[tekar_uzunluk]==liste[liste_uzunluk]:
        sayı+=1
    tekar.append([sayı,liste[liste_uzunluk]])
  return tekar            
     

def split(kelime):
     return [char for char in kelime]


def sıralama(liste):
 for liste_sayı1 in range(len(liste)):
   for liste_sayı2 in range(liste_sayı1):
      if liste[liste_sayı1]>liste[liste_sayı2]:
        sayı_tut=liste[liste_sayı2]
        liste[liste_sayı2]=liste[liste_sayı1]
        liste[liste_sayı1]=sayı_tut
 print(liste)
 return liste[0]

def kelime_cevirici(harfler):
  kelime=""
  for x in harfler:
    kelime+=x
  return kelime   


verile = python_veritabanı.veriler()
bulunan_indeks=0
veri = verile.sorgu('selam')
print(veri)
kelime =split('selam')

liste_=[]
liste_1=[]
liste_sayılar=[]
sayı=0

for kelime1 in veri:
  sayı+=1
  liste_.append([kelime1[0],sayı])

for liste_uzunluk in range(len(liste_)):
  bölünmüş_hal=split(liste_[liste_uzunluk][0])
  for bölünmüş_hal_uzunluk in range(len(bölünmüş_hal)):
    for kelime_uzunluk in range(len(kelime)):
      if kelime[kelime_uzunluk]==bölünmüş_hal[bölünmüş_hal_uzunluk]:
        liste_sayılar.append(liste_[liste_uzunluk][1])

liste_sayılar=sayı_tekar(liste_sayılar)
liste_sayma=[]

for liste_sayılar_uzunluk in range(len(liste_sayılar)):
   liste_sayma.append( liste_sayılar[liste_sayılar_uzunluk][0])


liste_tekar_sayıları=[item for item, count in collections.Counter(liste_sayma).items() if count > 1]

en_büyük_sayı=sıralama(liste_tekar_sayıları)
bulunan_yer=0
for liste_uzun in range(len(liste_sayılar)):
  if liste_sayılar[liste_uzun][0]==en_büyük_sayı:
    bulunan_yer=liste_sayılar[liste_uzun][1]

for liste__uzunluk in range(len(liste_)):
  if liste_[liste__uzunluk][1]==bulunan_yer:
    print(liste_[liste__uzunluk][0])