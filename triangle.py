

satir = int(input("Enter Number: "))
space = satir
spc=1

for i in range(satir):
    print((" "*space)+"* "*i)
    space-=1

for i in range(satir):
    print((" "*spc)+"* "*(satir-1))
    spc+=1
    satir-=1