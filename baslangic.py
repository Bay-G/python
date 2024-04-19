print(10/3)
print(10%3)
print(divmod(10,3))
print(int(10/3))
print(10//3)
print(1.5e3)

a=16
print(a)
a=-5
print(a)
a='istanbul'
print(a)

#Değişkenin tipi type() fonksiyonu ile ,değeri print() fonksiyonu ile adresi de
#id() fonksiyonu ile öğrenilebilir.

örnek="kelime"

print(type(örnek))
print(örnek)
print(id(örnek))

karmasiksayi=3+5j

#karmaşık sayılar normalde "i" ile gösterilirken python da "j" ile temsil edilir

print(karmasiksayi)
print("gerçek kısmı: ",karmasiksayi.real)
print("sanal kısmı: ",karmasiksayi.imag)

x=input("bir sayi girin: ") #burda input ve output bir sayı olabilir ama aslında bu int değil bir string türünde tutuluyor
print("girdiginiz sayi ",x)

int(x) #burda stringden integer'a değiştirdik
print(x)

sicil=1234
ad="emre"
soyad="genckan"

#    persbilgi=ad+soyad+sicil

# burda hata alırız çünkü ad ve soyad str türünde iken sicil int türünde

persbilgi=ad+soyad+str(sicil)
print(persbilgi)

print(len(ad))
adad="emre emre"
print(len(adad)) # boşlukları da sayıyor

print(abs(-6)) # abs() mutlak değer alır

import math

x=9
print(math.sqrt(x)) # kök alıyor
print(math.pow(x,2))    #kuvvet alıyor

y=4.0987654321

#round(a,b) yuvarlama yapar. a yuvarlancak sayıdır. b ise virgülden sonraki yuvarlanacak basamak sayısı 

print(round(y,1))
print(round(y,2))
print(round(y,3))
print(round(y,4))

print(math.factorial(5))

a=1
b=0

print(a is a)
print(a is b)
print(a is not a)
print(a is not b)

if(a<b):
    print(a,", ",b,"'den küçüktür")

else:
    print(a,", ",b,"'den büyüktür")


for i in range(1,9):
    print(i)

for i in range(1,9,2):
    print(i)


for i in "emre":
    print(i)

isim=["emre","ayşe","ahmet","mehmet"]

for i in isim:
    print(i)