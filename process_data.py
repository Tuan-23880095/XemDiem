import csv
import hashlib
import json
import os

output_folder = "diem_sinh_vien"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

with open('danh_sach_diem.csv', mode='r', encoding='utf-8-sig') as file:
    reader = csv.DictReader(file)
    for row in reader:
        mssv = row.get('MSSV', '').strip()
        mat_khau = row.get('MatKhau', '').strip()
        
        if not mssv or not mat_khau:
            continue
            
        chuoi_bi_mat = f"{mssv}_{mat_khau}".encode('utf-8')
        hash_name = hashlib.sha256(chuoi_bi_mat).hexdigest()
        
        # Hàm hỗ trợ lấy dữ liệu tránh lỗi nếu cột bị trống
        def get_val(key):
            return row.get(key, '').strip()
            
        student_data = {
            "Info": {
                "MSSV": mssv, "HoTen": get_val('HoTen'), "Nhom": get_val('Nhom'), "Lop": get_val('Lop')
            },
            "DiemQT": get_val('DiemQT'),
            "QT_ChuyenCan": {
                "Tong": get_val('DiemQT_01'),
                "T1": get_val('DiemQT_01_01'), "T2": get_val('DiemQT_01_02'), "T3": get_val('DiemQT_01_03'),
                "T4": get_val('DiemQT_01_04'), "T5": get_val('DiemQT_01_05'), "T6": get_val('DiemQT_01_06'),
                "T7": get_val('DiemQT_01_07'), "T8": get_val('DiemQT_01_08'), "T9": get_val('DiemQT_01_09'),
                "T10": get_val('DiemQT_01_10')
            },
            "QT_BaiTap": {
                "Tong": get_val('DiemQT_02'),
                "B1": get_val('DiemQT_02_01'), "B2": get_val('DiemQT_02_02'), "B3": get_val('DiemQT_02_03'),
                "B4": get_val('DiemQT_02_04'), "B5": get_val('DiemQT_02_05'), "B6": get_val('DiemQT_02_06'),
                "B7": get_val('DiemQT_02_07'), "B8": get_val('DiemQT_02_08'), "B9": get_val('DiemQT_02_09'),
                "B10": get_val('DiemQT_02_10')
            },
            "QT_DanhGiaCheo": {"Tong": get_val('DiemQT_03'), "T8": get_val('DiemQT_03_T8')},
            "QT_TimHieuKN": {
                "BC_Tong": get_val('DiemQT_04_A'),
                "BC_Nhom": get_val('DiemQT_04_A_01'),
                "BC_TuDG": get_val('DiemQT_04_A_02'),
                "ThuyetTrinh": get_val('DiemQT_04_B')
            },
            "CK_DuAn": {
                "BC_Tong": get_val('DiemCK_01'),
                "BC_Nhom": get_val('DiemCK_01_A'),
                "BC_TuDG": get_val('DiemCK_01_B'),
                "ThuyetTrinh": get_val('DiemCK_02')
            },
            "TongKet": get_val('TongKet'),
            "NhanXet": get_val('NhanXet')
        }
        
        file_path = os.path.join(output_folder, f"{hash_name}.json")
        with open(file_path, 'w', encoding='utf-8') as json_file:
            json.dump(student_data, json_file, ensure_ascii=False, indent=4)

print("Đã tạo xong dữ liệu phân cấp chi tiết!")
