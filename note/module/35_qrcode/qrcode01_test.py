import qrcode

def test1():
    #建立條碼圖片
    img = qrcode.make('4E0200173')
    print(type(img))  # qrcode.image.pil.PilImage
    img.save("test.png")

def test2():
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data('Some data')
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("test2.png")

if __name__ == '__main__':
    test1()
    print('ok')