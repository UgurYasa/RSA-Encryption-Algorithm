import constdata
import generate_variable
import process

dosya_adi = input("Dosya adını giriniz: ")
customFile = dosya_adi + ".txt"
def son_harfı_sil(dosya_adi):
    try:
        with open(customFile, "r+") as dosya:
            icerik = dosya.read()
            dosya.seek(0, 2)  # Go to the end of the file
            dosya.truncate(dosya.tell() - 1)  # Delete last character
    except FileNotFoundError:
        with open(customFile, "w") as dosya:
            dosya.write("[")  # Initialize content with “[” when file is created

def metni_txtye_yaz(metin):
    son_harfı_sil(customFile)
    with open(customFile, "a") as dosya:
        dosya.write(metin + ",\n]")

#FOR LOOP
for i in constdata.data:
    open_text = i["number_to_encrypt"]
    for j in i["data"]:
        #VARIABLES
        p = j["p"]
        q = j["q"]
        e = j["Open Key (E)"]
        n,n_time,n_text = generate_variable.n_generate(p,q)
        phi,phi_time,phi_text = generate_variable.phi_generate(p,q)

        #CHECKS
        if(process.isPrime(p) == False or process.isPrime(q) == False):
            print("p or q is not prime")
        elif e < 1 or e > phi:
            print("Invalid key")
        else:

            #OPERATIONS
            D,d_time,Dtext = generate_variable.generate_secret_key(e,phi)
            cipher_text,cipher_time,cipherText = generate_variable.generate_encrypted_text(open_text,e,n)
            found_open_text,open_time,openText = generate_variable.generate_plain_text(cipher_text,D,n)   
            
            #WRITING TO FILE
            metni_txtye_yaz(f"{"{"} numberToEncrypt: {open_text}, p: {p}, q: {q}, E: {e}, N: {n}, NTime: {n_time}, Phi: {phi}, PhiTime: {phi_time}, D: {D}, DTime: {d_time}, CipherText: {cipher_text}, CipherTime: {cipher_time}, OpenText: {found_open_text}, OpenTime: {open_time}{"}"}")