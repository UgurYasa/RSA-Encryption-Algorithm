import constdata
import degiskenuret
import islem

dosya_adi = input("Dosya adını giriniz: ")
customFile = dosya_adi + ".txt"
def son_harfı_sil(dosya_adi):
    try:
        with open(customFile, "r+") as dosya:
            icerik = dosya.read()
            dosya.seek(0, 2)  # Dosyanın sonuna git
            dosya.truncate(dosya.tell() - 1)  # Son karakteri sil
    except FileNotFoundError:
        with open(customFile, "w") as dosya:
            dosya.write("[")  # Dosya oluşturulduğunda içeriği "[" ile başlat

def metni_txtye_yaz(metin):
    son_harfı_sil(customFile)
    with open(customFile, "a") as dosya:
        dosya.write(metin + ",\n]")

#FOR LOOP
for i in constdata.data:
    open_text = i["sifrelenecek_sayi"]
    for j in i["data"]:
        #VARIABLES
        p = j["p"]
        q = j["q"]
        e = j["Açık Anahtar (E)"]
        n,n_time,n_text = degiskenuret.n_uret(p,q)
        phi,phi_time,phi_text = degiskenuret.phi_uret(p,q)

        #CHECKS
        if(islem.isPrime(p) == False or islem.isPrime(q) == False):
            print("p or q is not prime")
        elif e < 1 or e > phi:
            print("Invalid key")
        else:

            #OPERATIONS
            D,d_time,Dtext = degiskenuret.gizli_anahtar_uret(e,phi)
            cipher_text,cipher_time,cipherText = degiskenuret.sifreli_metin_uret(open_text,e,n)
            found_open_text,open_time,openText = degiskenuret.acik_metin_uret(cipher_text,D,n)   
            
            #WRITING TO FILE
            metni_txtye_yaz(f"{"{"} numberToEncrypt: {open_text}, p: {p}, q: {q}, E: {e}, N: {n}, NTime: {n_time}, Phi: {phi}, PhiTime: {phi_time}, D: {D}, DTime: {d_time}, CipherText: {cipher_text}, CipherTime: {cipher_time}, OpenText: {found_open_text}, OpenTime: {open_time}{"}"}")