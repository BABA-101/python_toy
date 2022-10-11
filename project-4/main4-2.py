# 웹 사이트 통해서도 qrcode 생성 가능하나, 파이썬으로 하는 이유는 "자동화"라는 장점 때문
# 여러 데이터를 자동으로 코드화 가능
import qrcode

file_path = r"project-4\qrcode_generator\qr코드모음.txt"
with open(file_path, "r") as f:
    readlines_file = f.readlines()

    for line in readlines_file:
        line = line.strip()  # 앞뒤공백삭제
        print(line)

        qr_data = line
        qr_img = qrcode.make(qr_data)

        save_path = "project-4\\qrcode_generator\\" + qr_data + ".png"
        qr_img.save(save_path)
