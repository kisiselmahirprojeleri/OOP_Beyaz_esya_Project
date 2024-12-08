from BeyazEsya import BeyazEsya

class Buzdolabi(BeyazEsya):
    def __init__(self,marka,model,enerji,fiyat,hacim,kapak_sayisi):
        super().__init__(marka,model,enerji,fiyat)
        self.hacim = hacim
        self.kapak_sayisi = kapak_sayisi

    def bilgileri_goster(self):
        super().__str__()   
        print(f"""
                Hacim:{self,hacim}
                Kapak_sayısı:{self.kapak_sayisi}
            """)
 buzdolabi = Buzdolabi('Beko','DN1233', 'A++', 30000, 350,2) 
 buzdolabi.bilgileri_goster()          

                
