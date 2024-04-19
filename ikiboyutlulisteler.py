t=[[12,4,6,21,5],[5,3,2,4,11],[3,13,5,8,7]]
print(t)

print(t[0])
print(t[1])
print(t[2])

# TUPLE(SATIR YA DA DEMET) VERİ YAPISI
# Tuple veri yapısı listeye benzer ancak liste yapısında değişikliğe müsaade edildiği halde(mutable) tuple yapısında değişikliğe müsaade edilmez(immutable).Örneğin t1 adlı tuple aşağıdaki gibi tanımlanabilir:
# t1 = 'm', 'n', 'p', 'q', 'r',’z’
# Zorunlu olmamakla birlikte bir tuple parantezler içine de alınabilir:
# t1 =( 'm', 'n', 'p', 'q', 'r',’z’)
# Tek elemanlı bir tuple oluşturulmak istenirse elemanın sonuna bir virgül konmalıdır:

t1=('e','m','r','e')
print(type(t1))
print(t1)

# t1[0]=t1[2]   burda tuple türünde olduğu için elemanları değiştiremicez ve denersek hata verecek
#   print(t1)

"""
TUPLE YARDIMI İLE İKİ DEĞİŞKENE YER DEĞİŞTİRTME(SWAP) İŞLEMİ
Bilgisayar biliminin klasik problemlerinden biri de swap işlemidir.Bu problem,basit olarak a değişkeninin değerini b’ye b değişkeninin değerini de a’ya aktarmak şeklinde ifade edilebilir.
SWAP’TEN ÖNCE
a=5
b=7
SWAP’TEN SONRA
a=7
b=5
Bu işlem bütün bilgisayar dillerinde yardımcı bir değişken kullanılarak yapılır:
t=a
a=b
b=t
Ancak Pythonda tuple notasyonu yardımı ile yardımcı değişken kullanmadan bu işlemi gerçekleştirmek mümkündür.Aşağıdaki örneği inceleyiniz:

"""

a=5
b=7
print("SWAP öncesi")
print("a= ",a)
print("b= ",b)

a,b=b,a
print("SWAP sonrası")
print("a= ",a)
print("b= ",b)

""" İkiden fazla değişken için de swap işlemi yaptırılabilir.Aşağıdaki örneği inceleyiniz: """

a=1
b=2
c=3
d=4
print("SWAP öncesi")

print("a= ",a)
print("b= ",b)
print("c= ",c)
print("d= ",d)

a,b,c,d=d,c,b,a
print("SWAP sonrası")

print("a= ",a)
print("b= ",b)
print("c= ",c)
print("d= ",d)