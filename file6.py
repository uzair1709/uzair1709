import pyqrcode
qr=pyqrcode.create("https://www.youtube.com/")
qr.svg("fan",scale=8)