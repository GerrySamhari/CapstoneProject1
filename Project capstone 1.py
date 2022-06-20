# project stock gudang

daftar_barang = [
    ['Aqua botol',20],
    ['aqua gelas',30],
    ['rokok super',50],
    ['mie instan',40],
    ['minuman soda',30],
    ['makanan ringan',50] 
]
barang_diambil =[]

def read():

    print('Daftar barang \n')
    print('Index\t|Nama barang\t|Stock\t|')
    for i in range(len(daftar_barang)):
        print('{}\t|{}\t|{}\t'.format(i,daftar_barang[i][0],daftar_barang[i][1]))

def menambah_barang():
    nama_barang = input('masukkan nama barang: ')
    stock_barang = int(input('masukkan stock barang: '))
    daftar_barang.append([nama_barang,stock_barang])
    print('Daftar barang \n')
    print('Index\t|Nama barang\t|Stock\t|')
    for i in range(len(daftar_barang)):
        print('{}\t|{}\t|{}\t'.format(i,daftar_barang[i][0],daftar_barang[i][1]))

def hapus_barang():
    print('Daftar barang \n')
    print('Index\t|Nama barang\t|Stock\t|')
    for i in range(len(daftar_barang)):
        print('{}\t|{}\t|{}\t'.format(i,daftar_barang[i][0],daftar_barang[i][1]))
    index_barang = int(input('Masukkan index dari barang yang ingin dihapus: '))
    del daftar_barang[index_barang]
    print('Daftar barang \n')
    print('Index\t|Nama barang\t|Stock\t|')
    for i in range(len(daftar_barang)):
        print('{}\t|{}\t|{}\t'.format(i,daftar_barang[i][0],daftar_barang[i][1]))

def ambil_barang():
    while True:
        print('Daftar barang \n')
        print('Index\t|Nama barang\t|Stock\t|')
        for i in range(len(daftar_barang)):
            print('{}\t|{}\t|{}\t'.format(i,daftar_barang[i][0],daftar_barang[i][1]))
        while True:
            index_barang = int(input('Pilih index barang yang ingin diambil: '))
            jumlah_barang = int(input('Masukkan jumlah barang yang ingin diambil: '))
            if(jumlah_barang > daftar_barang[index_barang][1]):
                print('stock tidak cukup')
            else:
                barang_diambil.append([daftar_barang[index_barang][0], jumlah_barang])
            print('barang yang diambil: ')
            print('nama barang\t|jumlah barang\t|')
            for i in barang_diambil:
                print('{}\t|{}\t'.format(i[0],i[1]))
            cek_barang = input('ingin mengambil barang lagi ? (ya/tidak) : ')
            if (cek_barang == 'tidak'):
                print('\ndaftar barang diambil')
                print('nama \t|stock \t')
                for i in barang_diambil:
                    print('{} \t|{} \t'.format(i[0],i[1]))
                print('\n Terima kasih')
                break

        break

    

def start():

    while True:
        menu_utama = input ('''\n====== Stock Gudang ======
    
        List Menu:
        1. Menampilkan stock barang
        2. Menambahkan stock barang
        3. Menghapus stock barang
        4. Mengambil stock barang
        5. Exit
    
        Masukkan angka Menu yang ingin dijalankan: ''')
        if (menu_utama == '1'):
            read()
        elif (menu_utama =='2'):
            menambah_barang()
        elif (menu_utama == '3'):
            hapus_barang()
        elif (menu_utama == '4'):
            ambil_barang()
        elif (menu_utama == '5'):
            break
start()