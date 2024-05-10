# pip install mysql-connector
import mysql.connector

def buat_koneksi():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="myapps"
    )

def cek_koneksi(db):
    if db.is_connected():
        print("Berhasil terhubung ke database")
    else:
        print("Error ege")

def buat_database(db):
    exec = db.cursor()
    exec.execute("CREATE DATABASE IF NOT EXISTS myapps")
    print("Database berhasil terbuat!")

def hapus_database(db):
    exec = db.cursor()
    if (input("Apakah kamu benar benar ingin menghapus Database 'Myapps'? (y/n)") == "y"):
        exec.execute("DROP DATABASE myapps")
        print("Database berhasil Terhapus!")
    else:
        print("Oke gajadi")

def buat_tabel(db):
    exec = db.cursor()
    nama_tabel = input("Masukkan nama tabel yang ingin dibuat : ")
    query = "CREATE TABLE " + nama_tabel + " ("

    jumlah_kolom = int(input("Masukan jumlah kolom :"))
    for i in range(0, jumlah_kolom):
        nama_kolom = input(f"Masukan nama dari kolom ke-{i} : ")
        if i == 0:
            query = query + f"{nama_kolom} INT AUTO_INCREMENT PRIMARY KEY,"
        else:
            jenis = int(input("Masukan Jenis Data\n1. INT\n2. VARCHAR\n3. TEXT\n4. DATE\n :"))
            if jenis == 1:
                panjang = input("Masukan panjang data :")
                query = query + f"{nama_kolom} INT({panjang}),"
            elif jenis == 2:
                panjang = input("Masukan panjang data :")
                query = query + f"{nama_kolom} VARCHAR({panjang}),"
            elif jenis == 3:
                panjang = input("Masukan panjang data :")
                query = query + f"{nama_kolom} TEXT({panjang}),"
            elif jenis == 4:
                query = query + f"{nama_kolom} DATE,"

    exec.execute(query[:-1] + ")")

def hapus_tabel(db):
    exec = db.cursor()
    nama_tabel = input("Masukkan nama table yang ingin dihapus: ")
    if (input(f"Apakah kamu benar benar ingin menghapus {nama_tabel}? (y/n)") == "y"):
        exec.execute(f"DROP TABLE {nama_tabel}")
        print("Database berhasil Terhapus!")
    else:
        print("Oke gajadi")

def input_data(db):
    exec = db.cursor(buffered=True)
    baca = "SELECT * FROM login"
    exec.execute(baca)
    baca = "INSERT INTO login ("
    for x in exec.column_names:
        baca = baca + f"{x},"
    baca = baca[:-1] + ") VALUES ("
    banyak_data = int(input("Masukan banyak data : "))
    data = []
    for y in range(len(exec.column_names)):
        baca = baca + "%s,"
    for x in range(banyak_data):
        data_collom = []
        for x in exec.column_names:
            a = input(f'Masukan data untuk kolom {x} :')
            data_collom.append(a)
        data.append(data_collom)
    baca = baca[:-1] + ")"
    print(data)
    for val in data:
        print(f"{baca}{val}")
        exec.execute(baca, tuple(val))
        db.commit()
    print("data berhasil ditambahkan.")

def baca_data(db):
    exec = db.cursor(buffered=True)
    baca = "SELECT * FROM login"
    exec.execute(baca)
    hasil = exec.fetchall()
    listdata = []
    for data in hasil:
        listdata.append(data)
    return listdata

def hapus_data(db):
    exec = db.cursor(buffered=True)
    baca = "SELECT * FROM login"
    exec.execute(baca)
    baca = f"DELETE FROM login WHERE {exec.column_names[0]}=%s"
    id = int(input('Masukkan id Data : '))
    val = (id, )
    exec.execute(baca, val)
    db.commit()
    print(f"{id} data dihapus")

def update_data(db):
    exec = db.cursor(buffered=True)
    data_ubah = input("Masukkan kolom yang ingin diubah: ")
    jadi_apa = input("Masukkan perubahan data: ")
    bagian_siapa = input("Masukkan baris yang ingin diubah: ")
    yang_mana = input("Masukkan data bagiannya: ")
    uppy = f"UPDATE login SET {data_ubah} = %s WHERE {bagian_siapa} = %s"
    exec.execute(uppy, (jadi_apa, yang_mana))
    db.commit()
    print("data dari database myapps tabel login sudah di update")

