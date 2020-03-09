abjad = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# kunci random huruf
kunci = 'qwertyuiopasdfghjklzxcvbnm'
print('Kunci : '+kunci)

pesan = input('Masukan Pesan : ')   # input pesan/plaint text
pesan = pesan.lower()   # pesan berupa huruf kecil
print('=== Enkripsi Monoalphabetic Cipher ===')
cipher = ''
for letter in pesan:    # perulangan sepanjang pesan
    if letter in abjad:     # jika pesan yg dimasukkan termasuk dalam abjad
        angkapesan = abjad.index(letter)    # mengubah pesan menjadi angka
        cipherhuruf = kunci[angkapesan]     # meng-enkripsi pesan dengan kunci
        cipher = cipher + cipherhuruf       # menggabungkan enkripsi
    else:
        cipher = cipher + letter            # menambahkan karakter selain huruf
print(cipher)


print('=== Dekripsi Monoalphabetic Cipher ===')
plaint = ''
for letter in cipher:       # perulangan sepanjang pesan enkripsi
    if letter in abjad:         # jika pesan enkripsi yg dimasukkan termasuk dalam abjad
        angkacipher = kunci.index(letter)   # mengubah pesan enkripsi menjadi angka
        plainthuruf = abjad[angkacipher]    # men-dekripsi pesan enkripsi
        plaint = plaint + plainthuruf       # menggabungkan huruf-huruf dekripsi
    else:
        plaint = plaint + letter            # menambahkan karakter selain huruf

print(plaint)