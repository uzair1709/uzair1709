import qrcode
import qrcode.constants
qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=20,border=2)
img=qr.add_data("https://meet.google.com/pgk-fcvh-pdq")
qr.make(fit=True)
img=qr.make_image(fill_colour="black",back="white")
img.save("uzair test .png")