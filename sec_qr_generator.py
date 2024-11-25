!apt-get install libzbar0
!pip install pyzbar opencv-python
import qrcode
import time
from datetime import datetime, timedelta
from cryptography.fernet import Fernet
import cv2
from pyzbar.pyzbar import decode

def generate_key():
    return Fernet.generate_key()

def create_expiring_qr(data, expiration_minutes, key):
    expiration_time = datetime.now() + timedelta(minutes=expiration_minutes)
    expiration_timestamp = int(expiration_time.timestamp())

    data_with_expiration = f"{data}|{expiration_timestamp}"

    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data_with_expiration.encode()).decode()

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(encrypted_data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    img.save("expiring_qr_code.png")

    print(f"QR code created. It will expire at: {expiration_time}")
    return img

def verify_qr_code(encrypted_data, key):
    fernet = Fernet(key)

    decrypted_data = fernet.decrypt(encrypted_data.encode()).decode()

    data, expiration_timestamp = decrypted_data.split("|")
    expiration_timestamp = int(expiration_timestamp)

    if int(time.time()) > expiration_timestamp:
        print("The QR code has expired.")
    else:
        print(f"The QR code is valid.Decrypted Data: {data}")

def decode_qr_code(image_path):
    img = cv2.imread(image_path)

    decoded_objects = decode(img)
    if len(decoded_objects) > 0:
        for obj in decoded_objects:
            qr_data = obj.data.decode('utf-8')
            print(f"Data in QR: {qr_data}")
            return qr_data
    else:
        print("No QR code found.")
        return None

if __name__ == "__main__":
    key = generate_key()

    data = input("Enter the data to store in QR: ")
    expiration_minutes = 1

    img = create_expiring_qr(data, expiration_minutes, key)

    img.show()

    decoded_data_fromqr = decode_qr_code("expiring_qr_code.png")
    while True:
      x=input("do you want to decode the qr y/n")
      if x=='y':
        decoded_data_fromqr = decode_qr_code("expiring_qr_code.png")
        verify_qr_code(decoded_data_fromqr, key)
        break
      else:
        break
    '''if decoded_data:
        verify_qr_code(decoded_data, key)
'''
