import random
from nhanvat import NguoiChoi, Quai

ten = input("Tên anh hùng: ")
hero = NguoiChoi(ten)
so_quai = 0

while hero.con_song():
    quai = Quai("Slime", random.randint(30, 50), 8)
    print(f"\nMột {quai.ten} xuất hiện! (Máu: {quai.mau})")

    while quai.con_song() and hero.con_song():
        print(f"\n[Bạn: {hero.mau} máu | {quai.ten}: {quai.mau} máu]")
        chon = input("1. Tấn công  2. Uống bình máu: ")

        if chon == "1":
            hero.tan_cong(quai)
        elif chon == "2":
            hero.dung_binh_mau()
        else:
            print("Lựa chọn không hợp lệ!")
            continue

        if quai.con_song():
            quai.tan_cong(hero)

    if hero.con_song():
        so_quai += 1
        print(f"Bạn hạ gục {quai.ten}! Tổng: {so_quai} quái.")

print(f"\nGame over! Bạn hạ được {so_quai} quái.")