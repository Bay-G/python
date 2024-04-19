ad="emre"
print(ad[0],ad[3],ad[2],ad[1])

""" ULKE=’FRANSA  CUMHURİYETİ’  ataması ile ULKE adlı string bellekte aşağıdaki biçimde yerleşecektir: """
""" F   R   A   N   S   A       C   U   M   H   U   R   İ   Y   E   T   İ """
""" 0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17 """
""" -18 -17 -16 -15 -14 -13 -12 -11 -10 -9  -8  -7  -6  -5  -4  -3  -2  -1 """

""" Buna göre  ULKE[0]  ilk karakter ve ULKE[17] son karakterdir.Aynı şekilde ULKE[-1]  son karakter ve ULKE[-18]  ilk karakterdir. """

ülke = "FRANSA CUMHURİYETİ"
print(ülke)

print("ilk eleman: ",ülke[-18]," ve ",ülke[0])
print("son eleman: ",ülke[-1]," ve ",ülke[17])

print(ülke[0:5])
print(ülke[0:6])
print(ülke[6:9])
print(ülke[9:])
print(ülke[:10])
print(ülke[17])
print(ülke[13:])

""" BİR STRINGTEN BAŞKA BİR STRING OLUŞTURMA
Bir stringin bir parçasını başka bir stringe ekleyerek yeni bir string oluşturabilirsiniz.Stringler arasında ‘+’ işareti ‘ekleme’ anlamındadır.
 """

sehir="güzel istanbul"
yenisehir="izmir"

print(sehir)
print(yenisehir)

print(sehir[0:5]+' '+yenisehir)

# \t bir tab boşluk bırakır. \n yeni satıra geçer

print("ahmet\tve\tmehmet")

print("ahmet\tve\nmehmet")

""" STRINGLERİN KARŞILAŞTIRILMASI
İki string alfabetik sırada önce ya da sonra gelme bakımından ya da eşitlik bakımından karşılaştırılabilir.Karşılaştırma sonucu doğru ise True,yanlış ise False sabiti elde edilecektir.
 """

print("istanbul"=='istanbul')
print("A">"a")
print("a">"A")
print("A"=="a")

""" Büyük harflerin ASCII kodları küçük harflerin ASCII kodlarından daha küçük olduğu 
için(A-> 65,a->97) yukardaki sonuçlar elde edilmiştir.
Yani gerçekte string karşılaştırmalarında sayısal ASCII kodları kullanılmaktadır. """

print(">>>Büyük harflerin ASCII kodları küçük harflerin ASCII kodlarından daha küçük olduğu için(A-> 65,a->97) yukardaki sonuçlar elde edilmiştir.\nYani gerçekte string karşılaştırmalarında sayısal ASCII kodları kullanılmaktadır.<<<")

for i in ülke:
    print(i)

""" Stringi aynı satıra yazdırmanın çözümü de  da print  komutuna  end=” “ ifadesini ekleyerek sağlanabilir: """

for i in ülke:
    print(i,end=" ")


""" string.replace(ilk,ikinci,sayı)
şeklinde kullanılır.string içinde ilk alt stringini arar bulursa ikinci ile değiştirir.sayı parametresi kullanılırsa yer değiştirmelerin sayısını belirtir.Örneğin 2 kullanılmışsa,yer değiştirme en fazla 2 tane olabilir.
 """



yunus="bir ben vardır bende benden içeri"
print(yunus)
yunus.replace("ben","sen")
print(yunus)

yunus.replace("ben","sen",2)
print(yunus)

print("---------")

isim=input("isminiz: ")

isim=isim.lower()
isim=isim[0].upper()+isim[1:]

print("merhaba",isim)


isim="emre"

for i in range(0,len(isim)):
    print(isim[i])


sentence = "Bugün hava çok güzel."
new_sentence = sentence.replace("güzel", "harika")
print(new_sentence)

kelime="ben ve sen değil biz olmalıydık. sen istemedin bizi, bense istedim seni"
print(kelime)

print(kelime.replace("ben","sen",1))

metin="""

Emre, bugün Emre ile buluşacağız.
Emre'nin doğum günü partisine katılacak mısın?




"""


print(metin)

print(metin.replace("Emre","5"))

kel="5m"

if kel.isalpha():
    print("alfa")