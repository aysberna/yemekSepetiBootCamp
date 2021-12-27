""" Bir metnin uzunluğunu hesaplamak için bir Python programı yazınız. ipucu Len fonksiyonu """
metin = input('Metin giriniz: ')
print(len(metin))

"""Kullanıcı tarafından girilen bir metnin ilk iki ve son iki karakterini ekrana yazdıran Python programını yazınız."""
metin = input('Metin giriniz: ')
print(metin[:2] + ' ' + metin[len(metin)-2:])

"""Kullanıcıdan değişecek metin ve eski harf ve yeni harf bilgisini alarak girilen metin üzerinden değişikliği yapıp sonucu ekrana yazdıran Python programını yazınız."""
metin = input('Metin giriniz: ')
eski = input('Değiştirilecek harfi giriniz: ')
yeni = input('Yeni harfi giriniz: ')
yeniMetin = metin.replace(eski, yeni)
print(yeniMetin)

"""Kullanıcı tarafından girilen bir kelimenin palindrom olup olmadığını karşılaştırma operatöründen faydalanarak print() fonksiyonu ile ekrana yazdırınız. """
metin = input('Metin giriniz: ')
tersMetin = metin[::-1]
if tersMetin == metin:
    print('Metin palindromedur')
else:
    print('Metin palindrome değildir.')

"""Girilen bir metnin son 2 karakterini 4 defa çoğaltarak ekrana yazan Python programını yazınız. * aritmetik operatöründen faydalanabilirsiniz. """
metin = input('Metin giriniz: ')
print(metin[len(metin)-2:]*4)

""" 5 elemanlı bir liste oluşturunuz. Bu liste içerisindeki 2. elemanı 100 ile değiştiren python kodu yazınız. """
import random
randomList = random.sample(range(1, 100), 5)
print('önce: ', randomList)
randomList[2] = 100
print('sonra: ', randomList)

"""İki farklı listede tutulan verileri tek bir listede sırasıyla append,extend metodlarıyla ve "+" operatörü ile birleştiren python kodunu yazınız liste1 = [1,2,3] liste2 = [4,5,6] liste3 = ????? """
liste1 = [1,2,3]
liste2 = [4,5,6]
liste3 = []
liste1.append(liste2)
liste1.extend(liste2)
liste3 = liste1 + liste2
print(liste3)

"""Oluşturduğunuz 3 elemanlı bir liste içerisine ilk sıraya "Elma" kelimesini ekleyiniz. """
import random
randomList = random.sample(range(1, 100), 5)
print('önce: ', randomList)
randomList.insert(0, 'Elma')
print('sonra: ', randomList)

"""liste = [1,2,3,4,5,6,7,1,3,3,3,2,2,1,23] yukarıdaki listeden ilk 3 sayısını silip ekrana yazdırınız. """
liste = [1,2,3,4,5,6,7,1,3,3,3,2,2,1,23]
for i, x in enumerate(liste,1):
    if x == 3:
        liste.remove(i)
        break
print('sonra: ', liste)

""" liste1 = ["1",1,2,"3"] Yukarıdaki listenin bir kopyasını alarak 250 sayısını listenin sonuna ekleyiniz,her iki listeyi ekrana yazdırınız. Beklenen Çıktı: ["1",1,2,"3"] => Liste1 Çıktısı ["1",1,2,"3",250] => Liste2 Çıktısı """
liste1 = ["1",1,2,"3"]
liste2 = liste1.copy()
liste2.append(250)
print('Liste1 Çıktısı ', liste1)
print('Liste2 Çıktısı ', liste2)

"""Aşağıdaki üç farklı sözlüğü tek sözlükte birleştiren python kodunu yazınız dict1={1:10, 2:20} dict2={3:30, 4:40} dict3={5:50,6:60} Beklenen Çıktı : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60} """
dict1={1:10, 2:20} 
dict2={3:30, 4:40} 
dict3={5:50,6:60}
dict1.update(dict2)
dict1.update(dict3)
print(dict1)

"""sozluk ={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60} Sözlükteki en son elemanı silerek ekrana işlem sonucunu yazdırınız Beklenen Çıktı :(6,60) """
sozluk = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
del sozluk[len(sozluk)]
print(sozluk)

"""dict1={1:10, 2:20} Yukarıdaki sözlüğe bir eleman ekleyiniz. Beklenen Çıktı :{1:10, 2:20, 3:30} """
dict1={1:10, 2:20}
dict1[3] = 30
print(dict1)

"""liste=[1,2,3,4,5] a.Yukarıdaki listeden faydalanarak bir sözlük oluşturun 
b.sözlüğün her alamanının karşılığına değer olarak anahtarda bulunan sayısal değerin 10 katını eşitleyin. 
Beklenen Çıktı : a. {1:0,2:0,3:0,4:0,5:0} b. {1:10,2:20,3:30,4:40,5:50} """
liste = [1,2,3,4,5]
sozluk = dict((k,0) for k in liste)
print('a. ', sozluk)
yeniSozluk = {k: k*10 for k, v in sozluk.items()}
print('b. ', yeniSozluk)

"""sozluk={1:10,2:20,3:30,4:40,5:50} Sözlük içerisine 
6 sayısını anahtar olarak değeri 60 olacak şekilde setdefault fonksiyonunu kullanarak ekleyiniz
"""
sozluk={1:10,2:20,3:30,4:40,5:50}
sozluk.setdefault(6, 60)
print(sozluk)

""" Seven Segment Display https://en.wikipedia.org/wiki/Seven-segment_display
  *
  *
  *
  *
8 sayısı girildiğinde yukarıdaki çıktıyı veren python programını 0 dan 9 a kadar olan sayılar için yazalım
hex,bin,zfill, tek satırda if

"""
# İstenilen şekilde çözemedim.
""" Bir listeyi bir sözlükte sıralamak için bir Python programı yazın
Örnek Veri: num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]} """
num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
for k, v in num.items() : v.sort()
print(num)

"""sozluk = {'S 001': ['Math', 'Science'], 'S 002': ['Math', 'English']}
ilgili sözlükten anahtar kısımlarında bulunan boşlukları temizleyen python kodu yazınız. """
sozluk = {'S 001': ['Math', 'Science'], 'S 002': ['Math', 'English']}
yeniSozluk = dict((k.replace(' ', ''), v) for k, v in sozluk.items())
print(yeniSozluk)

""" liste1=[1,2,3] liste2=[4,5,6,7,8] iki listeyi liste3 ile birleştiriniz? """
liste1=[1,2,3] 
liste2=[4,5,6,7,8]
liste3 = []
liste3.extend(liste1)
liste3.extend(liste2)
print(liste3)

"""liste=[1,2,3,4,5,6] listesindeki 1. elemanı del komutu ile siliniz?
"""
liste = [1,2,3,4,5,6]
del liste[0]
print(liste)

""" liste=["elma" , "armut", "çilek"] listesine append komutu ile sona 3 elemanını ekleyiniz? """
liste=["elma" , "armut", "çilek"]
liste.append(3)
print(liste)

"""Girilen on sayı içerisinden en büyük üç sayıyı bulmak için bir Python fonksiyonu yazınız"""
yeniListe = []
def fonksiyon(*args):
    if len(args) != 10:
        print('10 eleman girin!')
        return False
    liste = list(args)
    yeniListe = list(set(liste)) # aynı elemanları içermesin
    yeniListe.sort(reverse=True)
    print(yeniListe[:3])

fonksiyon(1,2,3,4,5,6,2,4,2,4)

"""Bir metin içerisindeki büyük ve küçük harflerin listesini yazdıran python programını yazınız."""
metin = input('Metin giriniz: ')
upperList = []
lowerList = []
[upperList.append(m) if m.isupper() else lowerList.append(m) if m.islower() else False for m in metin]

print('Büyük harfler ', upperList)
print('Küçük harfler ', lowerList)

"""kullanıcıdan alınan 10 sayının çift ve tek sayıların sayısını ekrana yazdıran programı yazınız. """
def fonksiyon(*args):
    if len(args) != 10:
        print('10 eleman girin!')
        return False
    liste = list(args)
    a = sum(i % 2 == 0 for i in liste)
    b = sum(i % 2 != 0 for i in liste)
    print('Tek sayı sayısı: ', a)
    print('Çift sayı sayısı: ', b)

fonksiyon(1,2,3,6)