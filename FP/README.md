# Membuat Storage Server

Dengan spesifikasi sebagai berikut:
1. Bisa melihat isi file dari sebuah storage (spesifik)
2. Bisa melihat isi file dari semua storage yg aktif
3. Bisa mengupload file ke storage. Penentuan storage yg mana yg akan jadi tujuan upload bebas.
4. Bisa mengupload file ke storage secara spesifik.
5. Bisa mengunduh file dari storage
6. Bisa berpindah direktori
7. Bisa mengcopy file di dalam storage itu sendiri
8. Bisa mengcopy file ke storage lain
9. Bisa mengcopy directory di dalam storage itu sendiri
10. Bisa mengcopy directory ke storage lain
11. Bisa memindahkan file di dalam storage itu sendiri
12. Bisa memindahkan file ke storage lain
13. Bisa memindahkan directory di dalam storage itu sendiri
14. Bisa memindahkan directory ke storage lain
15. Bisa menghapus file
16. Bisa menghapus directory
17. Bisa membuat file kosong (touch)
18. Saat demo storage dijalankan lebih dari 1 
19. Jumlah storage harus bisa dinamis
20. Ada tampilan GUI pake Tkinter


## Pembagian Tugas
Client:
* Nahda Fauziyah Zahra (5115100141)

Middleware:
* M. Faris Didin Andiyar (5115100118) 
* Hafara Firdausi (5115100043)
* Satria Aryawan (5115100066)

Worker:
* Rohana Qudus (5114100045)


## Langkah Testing

1. Ubah ```sharing_folder['base']```pada masing-masing worker sesuai dengan PC dimana worker tersebut dijalankan. Worker bekerja sebagai server

    p.s. Cara penulisan diakhir full path tidak perlu diberi slash '/'. Contoh: ```'/home/mocatfrio/Documents/SistemTerdistribusi/FP/worker1'```

2. Ubah **nameserver** pada ```def main()```

    ```python
    def main()
        # Pyro4.config.HOST="10.151.253.198:9000"
        Pyro4.Daemon.serveSimple(
            {
                Worker: "worker"
            },
            ns=False, host="10.151.253.198", port=9000)
    ```

    * Uncomment ```Pyro4.config.HOST="10.151.253.198:9000"``` dan sesuaikan dengan IP masing-masing PC. Boleh menggunakan port yang sama antar worker
    * Sesuaikan ```host``` sesuai dengan IP PC dan port-nya bebas, asal sama dengan ```Pyro4.config.HOST```

3. CEMUNGUD