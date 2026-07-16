import segno

URL = "https://www.bullsandbearspdeu.com"

qr = segno.make(URL)

qr.save(
    "qrcode.png",
    scale=10,
    border=4,
    dark="black",
    light="white"
)

print("QR code generated successfully.")