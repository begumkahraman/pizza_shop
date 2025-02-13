def giris_kontrol(deger, secenekler, hata_mesaji):
    if not deger.upper() in secenekler:
        raise ValueError(hata_mesaji)
    
print("Pizzacımıza hoşgeldiniz!")

def boy():
    try:
        pizza_boy = input("Pizza boyutunuzu S mi, M mi, L mi tercih edersiniz? : ")
        giris_kontrol(pizza_boy, ["S", "M", "L"], "S, M ya da L harici bir şey tuşladınız")
        return pizza_boy.upper()
    except:
        print("S,M ya da L harici bir şey tuşladınız")
        return boy()

def peynir():
    try:
        extra_peynir = input("Ekstra peynir isterseniz E, istemezseniz H'ye basınız: ")
        giris_kontrol(extra_peynir, ["E", "H"], "E ya da H harici bir şey tuşladınız")
        return extra_peynir.upper()
    except:
        print("E ya da H harici bir şey tuşladınız")
        return peynir()

def iccek():
    try:
        icecek = input("İçecek isterseniz E, istemezseniz H'ye basınız: ")
        giris_kontrol(icecek, ["E", "H"], "E ya da H harici bir şey tuşladınız")
        return icecek.upper()
    except: 
        print("E ya da H harici bir şey tuşladınız")
        return iccek()

pizza_boy = boy()
extra_peynir = peynir()
icecek = iccek()
hesap = 0

if pizza_boy == "S":
    hesap += 25
elif pizza_boy == "M":
    hesap += 30
elif pizza_boy == "L":
    hesap += 35

if extra_peynir == "E":
    hesap += 3 if pizza_boy in ["M", "L"] else 2

if icecek == "E":
    hesap += 2

print(f"Siparişiniz için teşekkürler! Hesabınız : {hesap} TL")