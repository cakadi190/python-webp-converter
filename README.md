## Python WebP Converter

Proyek ini adalah sebuah aplikasi sederhana yang menggunakan Python untuk mengkonversi berkas gambar ke format WebP. Pengguna dapat mengonversi gambar PNG, JPEG, atau format lain yang didukung menjadi WebP dengan mudah menggunakan antarmuka baris perintah (CLI).

### Fitur Utama:

- Mengonversi gambar PNG ke WebP.
- Mengonversi gambar JPEG ke WebP.
- Mendukung konversi batch untuk beberapa berkas sekaligus.
- Menyediakan opsi untuk mengatur kualitas kompresi WebP.
- Mudah diintegrasikan dengan skrip Python atau dijalankan secara langsung dari terminal.

### Instalasi:

1. Clone repositori ini:

   ```
   git clone https://github.com/cakadi190/python-webp-converter.git
   ```

2. Instal dependensi (jika ada):

   ```
   pip install -r requirements.txt
   ```

### Penggunaan:

Untuk mengonversi gambar tunggal:

```
python convert.py input_image.jpg -o output_image.webp
```

Untuk konversi batch:

```
python convert.py --batch input_folder/ -o output_folder/
```

### Kontribusi:

Kontribusi dan saran sangat dialuarkan! Silakan buat *pull request* untuk menyarankan perbaikan atau tambahan fitur.

### Lisensi:

Proyek ini dilisensikan di bawah MIT License. Lihat `LICENSE` untuk informasi lebih lanjut.
