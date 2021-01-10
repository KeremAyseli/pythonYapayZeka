import sqlite3

class veriler(object): 
        def sorgu(self,kelime):
         baglantı=sqlite3.connect('./pyyapay_zeka.db')
         komut=baglantı.cursor()
         liste=[]
         for gelen_degerler in komut.execute("select kelime FROM Tablo1 WHERE id=(SELECT id FROM Tablo1 WHERE kelime='"+kelime+"')"):
                liste.append(gelen_degerler)
                print(gelen_degerler)
         return liste
                  
