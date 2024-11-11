#Muhammad Haikal Akbar
#2409474
#1B
username = "Daspro2023"
password_sistem = "Latihan"

def login ():
    print("Selamat datang di Login sistem")
    print("Anda mempunyai kesempatan 3 kali untuk memasukkan password")

    for i in range (3):
        username_input = input("Silahkan masukkan username: ")
        password_input = input("Silahkan masukkan password: ")
        
        if username_input == username:
            next
        if password_input == password_sistem: 
            print("login berhasil")
            return 
        else:
            print("Password salah silahkan ulang kembali")
    print("Anda telah salah memasukkan password lebih dari 3 kali, Akses ditolak!.")

login()
