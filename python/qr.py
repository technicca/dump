# This script generates a QR code from a given text using the 'qrcode' Python library.
# It can be used to encode URLs or other data into a QR code that is saved as an image.
import qrcode


def generate_qr(text):
    # This function takes a string input 'text' to generate a QR code.
    # A QRCode object is created with specified version, error correction, box size, and border.
    # The text data is added to this QRCode object.
    # The 'fit=True' parameter allows the QR code to fit within the given constraints.
    # The QR code is then converted into an image with specified fill and background colors.
    # Lastly, the image is saved to a file 'output/qr.png'.
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=15,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save('output/qr.png')


url = input('Enter your url: ')
generate_qr(url)