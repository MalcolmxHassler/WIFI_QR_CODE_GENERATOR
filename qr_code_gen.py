import wifi_qrcode_generator as qr #importing the module
import configparser #to read the ini file
import matplotlib.pyplot as plt  # to display the QR code
from PIL import Image  # to handle image conversion

#reading the ini file
config = configparser.ConfigParser()
config.read('conf.ini')
wifi_name=config['WIFI_SETTINGS']['WIFI_NAME'].strip()
wifi_password=config['WIFI_SETTINGS']['PASSWORD'].strip()
security_type=config['WIFI_SETTINGS']['SECURITY'].strip()

# Validate the security type
valid_security_types = ['WPA', 'WPA2', 'WEP', 'nopass']
if security_type not in valid_security_types:
    raise ValueError(f"Unknown authentication_type: {security_type}")

#the qr code function
def wifi_qrcode(wifi_name, wifi_password, security_type):
    # Generate QR code and get the image directly
    qr_image=qr.wifi_qrcode(wifi_name, False, security_type, wifi_password)
    
    # Display the QR code using matplotlib
    plt.imshow(qr_image, cmap='gray')
    plt.axis('off')  # Hide the axis
    plt.show()
if __name__ == "__main__":
    wifi_qrcode(wifi_name,wifi_password,security_type)
    
