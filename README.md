# urlshortener
=======
````markdown
# 🔗 Django URL Shortener API

[![GitHub Repo](https://img.shields.io/badge/source-GitHub-blue?logo=github&style=flat-square)](https://github.com/Swapiano-Studio/urlshortener)

Sebuah API RESTful berbasis Django yang memungkinkan pengguna untuk memendekkan URL panjang menjadi URL pendek. Proyek ini mendukung operasi CRUD dan menyediakan statistik akses untuk setiap URL pendek. Siap digunakan di layanan cloud [Render](https://render.com) dan terhubung dengan basis data MySQL.

---

## 🚀 Fitur

- ✅ Buat URL pendek dari URL panjang
- 🔁 Pengalihan otomatis dari URL pendek ke URL asli
- 📊 Statistik akses (berapa kali URL diakses)
- 🧰 Operasi CRUD penuh (Create, Retrieve, Update, Delete)
- 📦 Konfigurasi via file `.env`
- 🛠 Dukungan basis data MySQL
- 🌐 Siap dideploy ke Render

---

## 🧰 Teknologi yang Digunakan

- Python 3.10+
- Django 4.x
- Django REST Framework
- MySQL
- python-dotenv

````

## 📦 Langkah Instalasi

### 1. Kloning Repositori
```bash
git clone https://github.com/Swapiano-Studio/urlshortener.git
cd urlshortener
````

### 2. Buat Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Instalasi Dependensi

```bash
pip install -r requirements.txt
```

### 4. Buat File `.env`

Contoh isi file `.env`:

```env
SECRET_KEY=django-secret-key-anda

DB_NAME=nama_database
DB_USER=user_database
DB_PASSWORD=password_database
DB_HOST=localhost
DB_PORT=3306

```

### 5. Migrasi Basis Data

```bash
python manage.py migrate
```

### 6. Jalankan Server Lokal

```bash
python manage.py runserver
```

---

## 📬 Daftar Endpoint API

| Metode | Endpoint           | Deskripsi                          |
| ------ | ------------------ | ---------------------------------- |
| POST   | `/api/urls/`       | Membuat URL pendek baru            |
| GET    | `/api/urls/`       | Menampilkan semua URL pendek       |
| GET    | `/api/urls/{id}/`  | Menampilkan detail URL tertentu    |
| PUT    | `/api/urls/{id}/`  | Memperbarui URL tertentu           |
| DELETE | `/api/urls/{id}/`  | Menghapus URL tertentu             |
| GET    | `/r/{short_code}/` | Redirect ke URL asli dan hit stats |

---

## 📄 Lisensi

Proyek ini menggunakan lisensi MIT. Silakan gunakan, modifikasi, dan distribusikan dengan bebas.

---

## ✨ Kredit

Dikembangkan oleh [Swapiano Studio](https://github.com/Swapiano-Studio) dengan ❤️
>>>>>>> 36c0e76 (init deploy)
