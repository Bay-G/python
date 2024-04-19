# fonksiyonlarla for deyimi kullanrak faktoriyel hesabı yapmak
def fact(sayi):

    fact=1
    for i in range(1,(sayi+1)):
        fact*=i

    print(fact)

sayi=int(input("fact sayisi: "))
fact(sayi)

# fonksiyonlarla fibonacci hesabı

def fibon(sayi1):

    x1=1
    x2=1
    toplam=0
    sayaç=2 #çünkü zaten x1 ve x2 diyerek ilk iki elemanı hallettik

    if(sayi1==1 or sayi1==2):
        return print("1")

    while(sayaç<sayi1):
        toplam=x1+x2
        x1=x2
        x2=toplam
        sayaç+=1

    print(toplam)
    



sayi1=int(input("sayi gir"))
fibon(sayi1)