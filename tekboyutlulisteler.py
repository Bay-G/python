x=[4,2,27,45,34]

for i in range(0,5): #5 e kadar gidecek ama 5'i almayacak
    print(x[i])

print("en küçük: ",min(x))
print("en büyük: ",max(x))
print("ilk eleman: ",x[:1])
print("indisi 3 olan elemana kadar: ",x[:3])
print("indisi 3 olandan sona doğru olan elemanlar: ",x[3:])

a=[2,7,9,1,5,10,6,11,9]
print(a)
a[4]=10
a[-1]=-44
a[3]=a[0]+a[4]
print(a)

sehir=["istanbul","izmir","ankara"]
print(sehir)
# insert(indis,nesne) nesneyi indisi girilen yere ekler
sehir.insert(1,"bursa") 
print(sehir)
# pop() son elemani siler
print("silinen şehir: ",sehir.pop())
print(sehir)

#reverse() listeyi kendi içinde ters çevirir

sehir.reverse()

print("şehirlerin ters sırayla yazılımı: ",sehir)

#Dizi elemanlarını küçükten büyüğe sıralar.Büyükten küçüğe sıralamak içinse sort metodundan sonra reverse metodunu kullanabilirsiniz.

x.sort()
print(x)

# extend() listeleri birbirine ekler

kızlar=["ayşe","fatma","melis"]
erkekler=["ahmet","mehmet","kunter"]

print(kızlar)
print(erkekler)

kızlar.extend(erkekler)
kızlar.extend(["ahmet"])
print(kızlar)


# index() Belirli bir nesnenin listede mevcut ise,indis değerini gönderir.

print("kunter kaçıncı index'de: ",kızlar.index("kunter"))

# count()  Verilen bir nesnenin bir liste içindeki tekrar sayısını bulur.

print("ahmet ismi kaç kere tekrar etti: ", kızlar.count("ahmet"))

# len()  Bir listedeki eleman sayısını bulur.

print("listenin uzunlugu: ",len(kızlar))

# sum()  Sayısal veri içeren bir listede liste elemanlarının toplamını hesaplar.

print(a," listesinin toplami: ",sum(a))

print(a," listesinin aritmetik ortalaması: ",sum(a)/len(a))
print(a," listesinin aritmetik ortalaması(tam sayıya yuvarlanmış hali): ",int(sum(a)/len(a)))

