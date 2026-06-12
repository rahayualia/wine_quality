# 1. Gunakan image Python versi ringan (misalnya versi 3.10)
FROM python:3.10-slim

# 2. Tentukan folder kerja di dalam container server
WORKDIR /app

# 3. Copy file requirements.txt terlebih dahulu ke dalam container
COPY requirements.txt .

# 4. Install semua library yang ada di requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy seluruh file project (app.py, model.pkl, dll) ke dalam container
COPY . .

# 6. Jalankan aplikasi menggunakan gunicorn
# Railway secara dinamis memberikan port melalui variabel $PORT, 
# jadi kita harus memastikan Gunicorn mendengarkan port tersebut.
CMD gunicorn app:app --bind 0.0.0.0:$PORT