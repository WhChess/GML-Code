import pywhatkit
import asyncio
import intro

async def main():
    await asyncio.sleep(3)
    while(True):
        print("Yapmak istediğiniz işlemi seçin")
        print("""
        1 - Kişi kaydet (En fazla 3 kişi kaydedebilirsin)
        2 - Mesaj Gönder (DM)
        3 - Grup Mesajı gönder (grupta ADMIN rolüne sahip olmalısın.)
        """)
        secim = input()
        if(secim=="1"):
            print("Kaydetmek için kişinin ismini yaz, kaydetmek istemediğin numaraları boşluk tuşuna basarak geçebilirsin.")
            kisi1 = input("Kaydetmek istediğin 1.kişi : ")
            kisi2 = input("Kaydetmek istediğin 2.kişi : ")
            kisi3 = input("Kaydetmek istediğin 3.kişi : ")
            if(kisi1==" "):
                del kisi1
                kisi1 = "0"
            else:
                telno1 = input("1.Kişinin telefon numarasını buraya yaz. EX: 1234441255 -: ")
            if(kisi2==" "):
                del kisi2
                kisi2 = "0"
            else:
                telno2 = input("2.Kişinin telefon numarasını buraya yaz. EX: 1234441255 -: ")
            if(kisi3==" "):
                del kisi3
                kisi3 = "0"
            else:
                telno3 = input("3.Kişinin telefon numarasını buraya yaz. EX: 1234441255 -: ")
        elif(secim=="2"):
            await asyncio.sleep(0.2)
            print("""Göndermek istediğin kişi:
            1 - Numara ile
            2 - Kaydettiğim ad ile
            """)
            secim2 = input()
            if(secim2=="1"):
                numara = input("Lütfen kişinin numarasını giriniz. EX: 1234441255 => ")
                numara = "+90" + numara
                saniye = input("Lütfen kişiye göndermek istediğiniz mesajı whatsapp açıldıktan kaç saniye sonra göndermek istediğinizi seçin (EN AZ 8 OLABİLİR) : ")
                saat = input("Kişiye ne zaman mesaj göndermek istediğinizi yazın. EX: 13.30 => ")
                saat1 = saat[0] + saat[1]
                saat2 = saat[3] + saat[4]
                mesaj = input("Kişiye göndermek istediğin mesaj: ")
                pywhatkit.sendwhatmsg(numara, mesaj, int(saat1), int(saat2), int(saniye))
            elif(secim2=="2"):
                ad = input("Lütfen kişinin adını giriniz: ")
                if((ad == kisi1) ^ (ad == kisi2) ^ (ad == kisi3)):
                    if(ad == kisi1):
                        telno = telno1
                    elif(ad == kisi2):
                        telno = telno2
                    elif(ad == kisi3):
                        telno = telno3
                    telno = "+90" + telno
                    saniye = input("Lütfen kişiye göndermek istediğiniz mesajı whatsapp açıldıktan kaç saniye sonra göndermek istediğinizi seçin (EN AZ 8 OLABİLİR) : ")
                    saat = input("Kişiye ne zaman mesaj göndermek istediğinizi yazın. EX: 13.30 => ")
                    saat1 = saat[0] + saat[1]
                    saat2 = saat[3] + saat[4]
                    mesaj = input("Kişiye göndermek istediğin mesaj: ")
                    pywhatkit.sendwhatmsg(telno, mesaj, int(saat1), int(saat2), int(saniye))
                else:
                    return -1
        elif(secim=="3"):
            link = input("Whatsapp Grubu Davet linkini buraya yapıştırın: ")
            linkcikar = "https://chat.whatsapp.com/"
            if linkcikar in link:
                link2 = link.replace(linkcikar,'')
                saniye = input("Lütfen gruba göndermek istediğiniz mesajı whatsapp açıldıktan kaç saniye sonra göndermek istediğinizi seçin (EN AZ 8 OLABİLİR) : ")
                saat = input("gruba ne zaman mesaj göndermek istediğinizi yazın. EX: 13.30 => ")
                saat1 = saat[0] + saat[1]
                saat2 = saat[3] + saat[4]
                if(saat1 == "00"):
                    saat1 = "0"
                if(saat2 == "00"):
                    saat2 = "0"
                mesaj = input("gruba göndermek istediğin mesaj: ")
                pywhatkit.sendwhatmsg_to_group(link2, mesaj, int(saat1), int(saat2), int(saniye))
            else:
                return -1
            
        else:
            return -1
            

asyncio.run(main())