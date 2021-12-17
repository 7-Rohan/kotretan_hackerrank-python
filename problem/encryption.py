import math

# ========== Encryption ==========
# link problem:
# https://www.hackerrank.com/challenges/encryption/problem?isFullScreen=false


'''
cara kerja pada problem ini cukup jelas dijelaskan di link problem diatas, saya hanya mengubah proses
enkripsi dengan tidak menggunakan grid, hanya menggunakan pola fungsi. jadi langsung studi kasus saja.
'''

'''
studi kasus:
    input : 
        str : "feed the dog"
    
    1. hilangkan spasi:
        menggunakan loop pada str, jika menemukan spasi maka sambungkan str sebelum spasi dan sesudah spasi.
        jika kondisi lain(else) maka lanjutkan pemeriksaan di posisi selanjutnya.
    
    perubahan : str : "feedthe dog" lalu "feedthedog"

    2. proses enkripsi
        setelah mendapatkan str tanpa spasi, tentukan len yaitu 10 dan columnnya(digunakan untuk menjadi periode)
        yaitu 4. lalu dengan fungsi posisi i+j*col selama i+j*col < len(str), masukkan ke output
        str : "(f)eed(t)hed(o)g"
        output : "fto"
        lalu tambahkan spasi diakhir loop dan ulang proses diatas
        str : "f(e)edt(h)edo(g)"
        output : "fto ehg"
        lanjut
        str : "fe(e)dth(e)dog"
        output : "fto ehg ee"
        lanjut
        str : "fee(d)the(d)og"
        output : "fto ehg ee dd"

    output : "fto ehg ee dd"
'''

def encryption(s):
    # Write your code here
    # clearing the spaces
    i = len(s) - 1
    while i >= 0:
        if s[i] == " ":
            s = s[:i] + s[i+1:]
        else:
            i -= 1
    
    len_s = len(s)
    col = math.ceil(math.sqrt(len_s))

    # encrypting process
    i = 0
    output = ""
    while i < col:
        j = 0
        while i+j*col < len_s:
            output = output + s[i+j*col]
            j += 1
        output = output + " "
        i += 1
    
    return output

def Main_encryption():
    print(10*"="+"encryption"+10*"=")
    str = "feed the dog"
    output = encryption(s=str)
    print(f"input:")
    print(f"str\t: {str}\n")
    print(f"output: {output}\n")
