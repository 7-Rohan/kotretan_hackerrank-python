# ========== Climbing The Leaderboard ==========
# link problem:
# https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem?isFullScreen=false

'''
cara kerja:
1.  menghilangkan elemen ganda di list
    proses menghilangkan elemen ganda di list kebetulan di bahas di w3school, berikut linknya:
    https://www.w3schools.com/python/python_howto_remove_duplicates.asp

2.  pemeriksaan dari belakang
    karena input ranked dan player selalu berurutan(ranked: dari besar ke kecil; player: dari kecil ke besar),
    maka bandingkan semua score di player ke ranked dari belakang sehingga proses loop tidak berulang. jika
    saat membandingkan score player masih lebih besar dari score di ranked, maka lanjutkan pemeriksaan elemen
    ranked ke depan. jika score player = score ranked maka rank posisi tersebut yang akan ditambahkan ke output.
    jika kondisi lainnya(else) maka rank posisi tersebut + 1 yang akan ditambahkan ke output.
    lanjutkan pemeriksaan score lain pada player.

3.  return output
'''

'''
studi kasus:
    input : 
        ranked : [100, 90, 90, 80, 75, 60]
        player : [50, 65, 77, 90, 102]
    
    proses 1:
        menghilangkan elemen ganda di ranked
    
    perubahan: ranked : [100, 90, 80, 75, 60]

    proses 2:
        periksa 50 : 50 < 60, maka tambahkan posisi 60 (yaitu 5) ditambah 1  yaitu 6 ke output
        periksa 65 : 65 > 60, maka lanjutkan pemeriksaan ke elemen ranked selanjutnya(ke depan) yaitu 75
                     65 < 75, maka tambahkan posisi 75 (yaitu 4) ditambah 1  yaitu 5 ke output
        periksa 77 : 77 > 75, maka lanjutkan pemeriksaan ke elemen ranked selanjutnya(ke depan) yaitu 80
                     77 < 80, maka tambahkan posisi 80 (yaitu 3) ditambah 1  yaitu 4 ke output
        periksa 90 : 90 > 80, maka lanjutkan pemeriksaan ke elemen ranked selanjutnya(ke depan) yaitu 90
                     90 = 90, maka tambahkan posisi 90 yaitu 2 ke output
        periksa 102 : 102 > 90, maka lanjutkan pemeriksaan ke elemen ranked selanjutnya(ke depan) yaitu 100
                     102 > 100, untuk kasus terakhir, posisi berubah ke posisi 0, maka sama dengan kondisi
                     lainnya(else) ditambah 1 yaitu 1 ke output
    
    output : [6, 5, 4, 2, 1]
'''

def climbingLeaderboard(ranked, player):
    output = []
    c_ranked = list(dict.fromkeys(ranked))

    i = len(c_ranked) - 1
    for score in player:
        while i >= 0 and score > c_ranked[i]:
            i -= 1
        if score == c_ranked[i]:
            output.append(i+1)
        else:
            output.append(i+2)
    return output

def Main_climbingLeaderboard():
    print(10*"="+"climbingLeaderboard"+10*"=")
    ranked = [100, 90, 90, 80, 75, 60]
    player = [50, 65, 77, 90, 102]
    output = climbingLeaderboard(ranked=ranked, player=player)
    print(f"input:")
    print(f"ranked\t: {ranked}")
    print(f"player\t: {player}\n")
    print(f"output: {output}\n")