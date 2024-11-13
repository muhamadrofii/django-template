

## Struktur folder

Berikut adalah struktur folder yang digunakan:

````
myproject/
│
├── myproject/                # Folder utama proyek Django
│   ├── settings.py           # Konfigurasi proyek Django
│   ├── urls.py               # URL routing untuk proyek utama
│   └── wsgi.py               # WSGI untuk server
│
├── smartbeez/                # Aplikasi utama smartbeez
│   ├── migrations/           # Folder untuk migrasi database
│   ├── templates/            # Template HTML
│   │   └── index.html        # File HTML
│   ├── admin.py              # Konfigurasi admin Django
│   ├── apps.py               # Konfigurasi aplikasi smartbeez
│   ├── models.py             # Definisi model untuk aplikasi smartbeez
│   ├── views.py              # Views untuk aplikasi smartbeez
│   └── urls.py               # Routing URL untuk aplikasi smartbeez
│
├── static/                   # Folder untuk file statis (CSS, JS, Images)
│   ├── css/                  # Folder CSS
│   ├── images/               # Folder gambar
│   └── js/                   # Folder JavaScript
│
└── manage.py                 # Skrip untuk menjalankan perintah Django
````

## Instalasi dan Persiapan

### 1. Membuat Virtual Environment

Pastikan Anda menggunakan virtual environment untuk proyek ini. Anda dapat membuat dan mengaktifkan virtual environment dengan perintah berikut:

```bash
python -m venv venv
source venv/bin/activate  # Untuk Linux/MacOS
venv\Scripts\activate     # Untuk Windows
```

### 2. Instalasi Dependensi

masuk ke direktori:

```bash
cd myproject
```

Instal semua dependensi yang diperlukan menggunakan `pip`:

```bash
pip install -r requirements.txt
```


### 3. Menjalankan Proyek

Untuk menjalankan proyek, gunakan perintah berikut:

```bash
python manage.py runserver
```

Aplikasi dapat diakses di `http://127.0.0.1:8000/`.

## URL Routing

- **Halaman Index:** `http://127.0.0.1:8000/`  
  Halaman ini akan menampilkan halaman utama proyek.
  
- **Halaman Allauth:**  
  Paket **django-allauth** sudah terintegrasi, Anda bisa mengakses halaman login, register, atau akun pengguna melalui URL berikut:
  
  - `http://127.0.0.1:8000/accounts/login/` - Halaman login.
  - `http://127.0.0.1:8000/accounts/signup/` - Halaman registrasi.
  - `http://127.0.0.1:8000/accounts/logout/` - Halaman logout.
  - `http://127.0.0.1:8000/accounts/profile/` - Halaman profil pengguna (setelah login).

## Folder Statis

- **Static Folder:** Folder `static/` berisi file-file yang digunakan untuk tampilan (CSS, JS, Gambar).
  - `static/css/` untuk file CSS.
  - `static/js/` untuk file JavaScript.
  - `static/images/` untuk file gambar.
Untuk membuat superuser di proyek Django, Anda dapat mengikuti langkah-langkah berikut:

### 4. Jalankan Perintah untuk Membuat Superuser

Setelah Anda memastikan bahwa server Django sedang berjalan (menggunakan perintah `python manage.py runserver`), jalankan perintah berikut di terminal:

```bash
python manage.py createsuperuser
```

### 5. Isi Informasi Superuser

Setelah menjalankan perintah tersebut, Django akan meminta Anda untuk memasukkan informasi berikut:

- **Username:** Nama pengguna untuk superuser.
- **Email address:** Alamat email untuk superuser.
- **Password:** Kata sandi untuk superuser (akan diminta dua kali untuk konfirmasi).

Contoh promptnya:

```bash
Username: admin
Email address: admin@example.com
Password: ********
Password (again): ********
```

### 6. Menjalankan Server

Setelah superuser berhasil dibuat, jalankan server Django jika belum berjalan:

```bash
python manage.py runserver
```

### 7. Akses Admin

Sekarang Anda bisa mengakses halaman admin Django di:

```
http://127.0.0.1:8000/admin/
```

Masukkan username dan password yang Anda buat sebelumnya untuk login ke dashboard admin Django.
