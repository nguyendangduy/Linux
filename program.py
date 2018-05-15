from SinhVien import sinhvien

sv = sinhvien("duy","97","57")
ten = raw_input("nhap ten sinh vien : ")
namsinh = raw_input("nhap nam sinh : ")
khoa = raw_input("nhap khoa : ")
sv.setTEN(ten)
sv.setNAMSINH(namsinh)
sv.setKHOA(khoa)
sv.toString()
