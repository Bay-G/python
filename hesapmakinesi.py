import math as m

System=True
ikinci_sayfa=False

def toplama(s1,s2):
    s1=float(s1)
    s2=float(s2)
    return print(s1+s2)

def çıkarma(s1,s2):
    s1=float(s1)
    s2=float(s2)
    return print(s1-s2)

def çarpma(s1,s2):
    s1=float(s1)
    s2=float(s2)
    return print(s1*s2)

def bölme(s1,s2):
    s1=float(s1)
    s2=float(s2)
    return print(s1/s2)

def kuvvetal(s1,s2):
    s1=float(s1)
    s2=float(s2)
    return print(m.pow(s1,s2))

def fakt(s1):
    sayaç=1
    if s1==1 or s1==0:
        return print("1")
    
    for i in range(1,s1+1):
        sayaç*=i
    
    return print(sayaç)

def fib(s1):
    if s1==2:
        return print("1")
    elif s1==1:
        return print("0")
    bir=0
    iki=1
    top=0

    for i in range(1,s1):
        top=bir+iki
        bir=iki
        iki=top

    return print(top)

    
def tribo(s1):
    bir=0
    iki=0
    üç=1
    top=0

    for i in range(1,s1-2):
        if s1==1 or s1==2:
            return print("0")
        elif s1==3:
            return print("1")
        top=bir+iki+üç
        bir=iki
        iki=üç
        üç=top
    return print(top)



    



while System:
    
    def birinci_sayfa():
        print()
    
    print("\n")
    print("\t1.SAYFA\n------------------------")
    print("1-Toplama")
    print("2-Çıkarma")
    print("3-Çarpma")
    print("4-Bölme")
    print("5-Kuvvet Al")
    print("6-Faktöriyel Hesapla")
    print("7-Fibonacci Hesapla")
    print("8-Tribonacci Hesapla")
    print("9-Sonraki Sayfa")
    print("0-Çıkış")

    seçim=eval(input(">>"))



        

        
    
    match seçim:
        case 1:
            s1=float(input("1. Sayı: "))
            s2=float(input("2. Sayı: "))
            toplama(s1,s2)

        case 2:
            s1=float(input("1. Sayı: "))
            s2=float(input("2. Sayı: "))
            çıkarma(s1,s2)

        case 3:
            s1=float(input("1. Sayı: "))
            s2=float(input("2. Sayı: "))
            çarpma(s1,s2)

        case 4:
            s1=float(input("1. Sayı: "))
            s2=float(input("2. Sayı: "))
            bölme(s1,s2)

        case  5:
            s1=float(input("1. Sayı: "))
            s2=float(input("2. Sayı: "))
            kuvvetal(s1,s2)

        case 6:
            s1=int(input("Hesaplanacak Sayı: "))
            fakt(s1)

        case 7:
            s1=int(input("Hesaplanacak Eleman: "))
            fib(s1)

        case 8:
            s1=int(input("Hesaplanacak Eleman: "))
            tribo(s1)

       
        case 9:
            ikinci_sayfa=True

            while ikinci_sayfa:
                
                print()
                print()
                print("\n\t2.SAYFA\n------------------------")
                print("1-Cos Hesapla")
                print("2-Sin Hesapla")
                print("3-Tan Hesapla")
                print("4-Cot Hesapla")
                print("5-Sec Hesapla")
                print("6-Csc Hesapla")
                print("7- ")
                print("8-Önceki")
                print("9-Sonraki")
                print("0-Çıkış")
            
                seçim=eval(input(">>"))

                match seçim:

                    case 1:
                        açı=float(input("Hesaplanacak Açı: "))
                        rad=m.radians(açı)
                       
                        print(m.cos(rad))

                    case 2:
                        açı=float(input("Hesaplanacak Açı: "))
                        rad=m.radians(açı)
                        print(m.sin(rad))

                    case 3:
                        açı=float(input("Hesaplanacak Açı: "))
                        rad=m.radians(açı)
                        if açı % 180 != 90:
                            print(m.tan(rad))
                        else:
                            print("Tanjant hesaplanamaz: Tanjant 90 derecede tanımsızdır.")

                    case 4:
                        açı=float(input("Hesaplanacak Açı: "))
                        rad=m.radians(açı)
                        if açı % 180 != 0:
                            print(1/m.tan(rad))
                        else:
                            print("Kotanjant hesaplanamaz: Kotanjant 0 derecede tanımsızdır.")

                    case 5:
                        açı=float(input("Hesaplanacak Açı: "))
                        rad=m.radians(açı)
                        sec=1/m.cos(rad)
                        if m.cos(rad) != 0:
                            print(sec)
                        else:
                            print("Sekant hesaplanamaz: Tanımsız")

                    case 6:
                        açı=float(input("Hesaplanacak Açı: "))
                        rad=m.radians(açı)
                        csc=1/m.sin(rad)
                        if m.sin(rad)!=0:
                            print(csc)
                        else:
                            print("Kosekant hesaplanamaz: Tanımsız")

                    


                    case 0:
                        exit(0)
                       
                
                    case 9:
                        print("Yeni Sayfalar Çok Yakında")
                        
                    

                    case 8:
                        ikinci_sayfa=False


        case 0:
            exit(0)
        
    
    