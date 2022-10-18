import qrcode
from PIL import Image

qr_data = "Some Sample QR Data"
margin_size = 1
version = 3

for i in range(1,11):
    qr = qrcode.QRCode(
        version=1,
        box_size=i,
        border=i)
    qr.add_data('Sample data')
    qr.make()
    img = qr.make_image()
    img.save('sample'+str(i)+'.png')
    im = Image.open('sample'+str(i)+'.png')
    rgb_im = im.convert("RGB")
    rgb_im.save('sample'+str(i)+'.jpg')

