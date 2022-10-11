import qrcode

qr_data = "www.naver.com"
qr_img = qrcode.make(qr_data)

save_path = "project-4\\qrcode_generator\\" + qr_data + ".png"
qr_img.save(save_path)
