szlk={
    
    "ad":"",
      "soyad":"",
      "cinsiyet":"",
      "yaş":""
  
      }


szlk["ad"]=input("adınız:")
szlk["soyad"]=input("soyadınız:")
szlk["cinsiyet"]=input("cinsiyetiniz:")
szlk["yaş"]=input("yaşınız:")

print(szlk["ad"] , szlk["soyad"], " (" ,szlk["yaş"] , "," , szlk["cinsiyet"] , ")")

del szlk["yaş"]
print(szlk["ad"] , szlk["soyad"], " (" ,szlk["yaş"] , "," , szlk["cinsiyet"] , ")")

szlk.clear()
print(szlk["ad"] , szlk["soyad"], " (" ,szlk["yaş"] , "," , szlk["cinsiyet"] , ")")