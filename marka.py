class Base:
    def __init__(self,urun_id = 0, ürün_ismi = ""):
        self.urun_id = urun_id
        self.urun_ismi = ürün_ismi

    def urun_kaydet(self):
        #kullanıcıdan ID ve isim bilgilerini alır ve sınıfın özelliklerini atar
        self.urun_id = int(input('Ürün ID:'))
        self.urun_ismi = input('Ürün İsmi: ')
class Urun(Base):
    def __init(self, urun_id = 0,ürün_ismi = "",ürün_fiyatı = 0):
        super()  .__init(urun_id,ürün_ismi)
        self.ürün_fiyatı = ürün_fiyatı 

    def urun_kaydet(self):
        super().urun_kaydet() 
        self.ürün_fiyatı = float(input('Ürün Fiyatı: '))   

    def ürün_silme(self, ürün_listesi:list):

        for i in ürün_listesi:
            print(f"{i.urun_id}  Id si olan ismi {i.urun_ismi}")
             #silmesini istediğimiz ürünlerin ID sini alalım
             id = int(input('Silinecek İd: '))
             #  Liste üzerinden silinecek ürünü bulup kaldıralım
             for i in ürün_listesi:
                if i.urun_id == id:
                    ürün_listesi.remove(i)
    def Update(self,ürün_listesi):
        #parametre olarak girilmiş ürün listesini görelim
        for i in ürün_listesi:
            print(f"{i.urun_id} olan Id li ürünün ismi  {i.urun_ismi}")    

            #güncellemek istediği ürün Id sini soralım
            id = int(input('Güncellenecek ID: ')) 

            #liste üzerinde gezinerek güncellenecek ürünün isim ve fiyatını kullanıcıdan alarak ürünü günceller
            for i in ürün_listesi:
                if i.urun_id == id:
                    i.urun_ismi = input('Yeni ürün ismi')
                    i.ürün_fiyatı = input('Güncel Fiyat: ')

class Kategori(Base):
    def __init__(self,ürün_tanımı = ""):
        self.ürün_tanımı = ürün_tanımı

    def urun_kaydet(self):
        super().urun_kaydet()
        self.urun_tanımı = input('Ürün Açıklaması: ') 

class Marka(Base):
    def __init__(self,ürün_markası = ""):
        self.ürün_markası = ürün_markası

     def urun_kaydet(self):
        super().urun_kaydet()
        self.ürün_markası = input('Ürün Markası: ')

#Ürün,kategori ve marka listelerini oluşruralım
ürünler = []
kategoriler = []
markalar = []

#örnek bir ürün oluşturalım ve bilgilerini kullanıcıdan alalım
ürün = Urun()
ürün.urun_kaydet()
ürünler.append(ürün)
for i in ürünler:
    print(f"Ürün ID: {i.urun_id}\ nÜrün İsmi: {i.urun_ismi}\nÜrün Fiyatı: {i.ürün_fiyatı}")

ürün.Update(ürünler) 

for i in ürünler:
    print(f"Ürün ID: {i.urun_id}\nÜrün İsmi: {i.urun_ismi}\nÜrün Fiyatı: {i.ürün_fiyatı}")
    
    



