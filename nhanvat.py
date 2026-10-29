import random

class NhanVat:
    def __init__(self, ten, mau, sat_thuong):
        self.ten = ten
        self.mau = mau
        self.sat_thuong = sat_thuong

    def con_song(self):
        return self.mau > 0

    def tan_cong(self, muc_tieu):
        dame = random.randint(self.sat_thuong - 3, self.sat_thuong + 3)
        muc_tieu.mau -= dame
        print(f"{self.ten} đánh {muc_tieu.ten}, gây {dame} sát thương!")

class NguoiChoi(NhanVat):
    def __init__(self, ten):
        super().__init__(ten, mau=100, sat_thuong=15)
        self.binh_mau = 2

    def dung_binh_mau(self):
        if self.binh_mau > 0:
            self.binh_mau -= 1
            self.mau = min(100, self.mau + 30)
            print(f"Bạn hồi máu! Máu: {self.mau}. Còn {self.binh_mau} bình.")
        else:
            print("Hết bình máu!")

class Quai(NhanVat):
    pass