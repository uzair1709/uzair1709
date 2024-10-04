import qrcode
import qrcode.constants
qr=qrcode.QRcode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=10,border=4)
img=qr.add_data("https://www.youtube.com/")
qr.make(fit=True)
img=qr.make_image(fill_color="black",back="white")
img.save("pin.png")