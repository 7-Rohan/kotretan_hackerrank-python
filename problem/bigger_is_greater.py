# ========== Bigger Is Greater ==========
# link problem:
# https://www.hackerrank.com/challenges/encryption/problem?isFullScreen=false

'''
cara kerja:
1.  pengubahan input ke array
    ubah input yang berupa string ke array berisi char agar bisa melakukan proses swap elemen. jika input 
    hanya terdiri dari 1 char, return no answer.

2.  pemeriksaan dari belakang
    periksa elemen kedua dari belakang bergerak ke depan. tinjau elemen sebelah kanan(arah ke belakang) dari
    elemen yang diperiksa, apakah ada elemen yang lebih besar dari elemen yang diperiksa. jika ada lebih dari
    satu, pilih paling kecil lalu swap dengan elemen yang diperiksa tadi. jika tidak ada maka ulang pemeriksaan
    ke elemen selanjutnya(bergerak ke depan). jika memang tidak ada semua maka return no answer.
    jika sudah dilakukan swap, maka proses 2 selesai (break).

3.  merapihkan bagian belakang
    setelah melakukan proses 2, dengan menggunakan posisi elemen yang sebelumnya digunakan, periksa elemen
    dan bergerak ke belakang. tinjau elemen sebelah kanan(arah ke belakang) dari elemen yang diperiksa, apakah
    ada elemen yang lebih kecil dari elemen yang diperiksa. jika ada lebih dari satu, pilih paling kecil lalu
    swap dengan elemen yang diperiksa tadi. jika sudah tidak ada maka ulang pemeriksaan ke elemen selanjutnya
    (bergerak ke belakang). lakukan proses tiga hingga akhir dari array.

4.  return
    gabungkan semua elemen di array menjadi string. lalu return.
'''

'''
studi kasus:
    input : "dkhc"
    proses 2:
        periksa h : di belakang h tidak ada elemen yang lebih besar dari h, maka lanjut periksa yang lain
        periksa k : di belakang k tidak ada elemen yang lebih besar dari k, maka lanjut periksa yang lain
        periksa d : di belakang d terdapat k dan h yang lebih besar dari d, maka pilih yang paling kecil
                    yaitu h, swap h dengan d
        karena sudah melakukan swap sekali maka proses 2 selesai (break).
    
    perubahan: "hkdc"

    proses 3:
        pada posisi elemen terakhir di proses 2, periksa elemen dibelakang elemen tersebut
        periksa k : di belakang k terdapat d dan c yang lebih kecil dari k, maka pilih yang paling kecil
                    yaitu c, swap k dengan c. lanjutkan proses, bergerak ke belakang
    perubahan: "hcdk"
        periksa d : dibelakang d tidak ada elemen yang lebih kecil dari d, maka lanjut periksa yang lain
        preiksa k : dibelakan k tidak ada elemen, proses 3 selesai.
    
    output : "hkdc"

'''

def biggerIsGreater(w):
    # Write your code here
    arr_str = []
    for huruf in w:
        arr_str.append(huruf)
    
    len_arr = len(arr_str)
    i = len_arr - 2
    while i >= 0:
        j = i+1
        min_swap = "z"
        i_swap = 0
        while j < len_arr:
            if arr_str[j] > arr_str[i] and arr_str[j] <= min_swap:
                min_swap = arr_str[j]
                i_swap = j
            j += 1
        if i_swap != 0:
            arr_str = swap(arr_str, i, i_swap)
            break
        if i == 0:
            return "no answer"
        i -= 1
    
    i += 1
    while i < len_arr:
        j = i+1
        min_swap = "z"
        i_swap = 0
        while j < len_arr:
            if arr_str[j] < arr_str[i] and arr_str[j] <= min_swap:
                min_swap = arr_str[j]
                i_swap = j
            j += 1
        if i_swap != 0:
            arr_str = swap(arr_str, i, i_swap)
        i += 1

    return "".join(arr_str)


def swap(arr, i, j):
    a = arr[i]
    b = arr[j]
    arr[i] = b
    arr[j] = a
    return arr

def Main_biggerIsGreater():
    print(10*"="+"biggerIsGreater"+10*"=")
    str = "dkhc"
    output = biggerIsGreater(str)
    print(f"input:")
    print(f"str\t: {str}\n")
    print(f"output: {output}\n")
