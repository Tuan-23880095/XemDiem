import csv
import hashlib
import json
import os

# Tạo thư mục chứa file điểm
output_folder = "diem_sinh_vien"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

with open('danh_sach_diem.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        mssv = row['MSSV'].strip()
        mat_khau = row['MatKhau'].strip()
        
        # Tạo chuỗi băm từ MSSV và Mật khẩu
        chuoi_bi_mat = f"{mssv}_{mat_khau}".encode('utf-8')
        hash_name = hashlib.sha256(chuoi_bi_mat).hexdigest()
        
        # Dữ liệu xuất ra file JSON
        student_data = {
            "MSSV": mssv,
            "HoTen": row['HoTen'],
            "DiemQT": row['DiemQT'],
            "DiemCK": row['DiemCK'],
            "NhanXet": row['NhanXet']
        }
        
        # Lưu file
        file_path = os.path.join(output_folder, f"{hash_name}.json")
        with open(file_path, 'w', encoding='utf-8') as json_file:
            json.dump(student_data, json_file, ensure_ascii=False, indent=4)

print("Đã tạo xong các file dữ liệu ẩn!")
