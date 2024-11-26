### Expiring QR Code Generator and Verifier : 

This Python project demonstrates how to generate QR codes that store encrypted data with an expiration time. The QR code contains encrypted data that is valid only for a specific period, after which it expires. The project uses the cryptography, qrcode, opencv, and pyzbar libraries.

### Features :

    1. QR Code Generation: Create QR codes that store encrypted data, with a specified expiration time.
    2. QR Code Verification: Verify if the QR code's data is still valid (not expired).
    3. Expiration Mechanism: Store the expiration time inside the QR code, ensuring the data becomes invalid after the set duration.

### Installation : 
    To use this project, you'll need to install the following dependencies:
        Install the necessary system library for handling QR codes:
             sudo apt-get install libzbar0
        Install the required Python packages:
            pip install pyzbar opencv-python cryptography qrcode
            
### How to Use
    1. Generate an Expiring QR Code
        The script will prompt you to enter the data you want to encode in the QR code.
        You can specify the expiration time (in minutes) after which the QR code will no longer be valid (default is 1 minute).
        The generated QR code will be saved as expiring_qr_code.png.
    2. Decode the QR Code
        After creating the QR code, you can scan or decode it to verify whether the QR code has expired.
        If the QR code is valid, the decrypted data will be displayed.
        If the QR code has expired, a message will inform you that the QR code is no longer valid.
        3. Run the Script
        python expiring_qr_code.py

### Example Workflow
    Creating the QR Code:
        The script will ask for input data.
        It will generate and display the QR code and save it as expiring_qr_code.png.
        
### Verifying the QR Code:
    The script will prompt you to decode the QR code by scanning it.
    If the code is scanned within the expiration time, the encrypted data is decrypted and displayed.
    After expiration, the script will inform you that the QR code is expired.    
    
### Code Breakdown
    Key Generation: The generate_key() function creates an encryption key using cryptography.fernet.
    
    QR Code Creation: The create_expiring_qr() function encrypts the data with an expiration timestamp and generates a QR code using the qrcode library.
    
    QR Code Decoding: The decode_qr_code() function reads and decodes the QR code image using pyzbar and OpenCV.


    Verification: The verify_qr_code() function decrypts the QR code data and checks if the expiration timestamp has passed.


### License
    This project is licensed under the MIT License.

### Tips for Improving or Extending This Project:

    1. Customize the expiration mechanism to include other factors, such as specific days or time ranges.
    2. Extend the script to allow batch generation and scanning of multiple QR codes.
    3. Integrate a user-friendly GUI or web interface to interact with the QR code generator and verifier.

