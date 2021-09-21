#kelas Bangun Datar
class BangunDatar :
    SegitigaSamaKaki = None
    Jajargenjang = None

#membangun instance/variable sebagai "objek nyata"
BD = BangunDatar()
SegitigaSamaKaki = None
Jajargenjang = None

#input panjang Segitiga Sama Kaki
rows = int (input("Masukan Panjang: "))
for i in range(rows + 1, 0, -1):
    #nested reverse loop
    for j in range(0, i-1):
        # display star
        print("*", end='  ')
    print("  ")

print("Jajar Genjang")
#input panjang jajargenjang
n = int (input("Masukan Panjang: "))
i = 1
a = n
while (i<=n):
    print(" "*(n-1) ,"*" * a)
    n = n-1