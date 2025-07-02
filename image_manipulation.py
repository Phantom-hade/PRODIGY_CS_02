"""
Title       : Pixel Manipulation For Image Encryption
Author      : Larona B. Kwae
Date        : June 2025
PRODIGY_CS  : 02
Description : A python program that encrypts and decrypts images using pixel manipulation. 
""" 

from PIL import Image      # For image handling and pixel access
import os                   #Checks if file path exists

# Function to Encrypt Image
def encrypt_image(input_path, encrypt_output, key):
    image = Image.open(input_path)
    encrypted = Image.new(image.mode, image.size)
    pixels = image.load()
    encrypted_pixels = encrypted.load()

      # Loop through every pixel in the image
    for x in range(image.width):
        for y in range(image.height):
            r, g, b = pixels[x, y]
            encrypted_pixels[x, y] = (
                (r + key) % 256,
                (g + key) % 256,
                (b + key) % 256
            )

    encrypted.save(encrypt_output)
    print(f" Image encrypted and saved to '{encrypt_output}'")

# Function to Decrypt Image
def decrypt_image(input_path, decrypt_output, key):
    image = Image.open(input_path)
    decrypted = Image.new(image.mode, image.size)
    pixels = image.load()
    decrypted_pixels = decrypted.load()

      # Loop through every pixel in the image
    for x in range(image.width):
        for y in range(image.height):
            r, g, b = pixels[x, y]
            decrypted_pixels[x, y] = (
                (r - key) % 256,
                (g - key) % 256,
                (b - key) % 256
            )

    decrypted.save(decrypt_output)
    print(f" Image decrypted and saved to '{decrypt_output}'")

#  Menu
print("\n Image Encryption Tool")
print("1. Encrypt Image")
print("2. Decrypt Image")

# Get user choice
choice = input("Choose an option (1 or 2): ").strip()

#Prompt user  for the input image file path
input_path = input("Enter path to the image file: ").strip()
# Check if the file actually exists
if not os.path.exists(input_path):
    print(" Error: File does not exist.")
    exit()

# Prompt user  for the output file names
encrypt_output = input("Enter name for encrypted output image file: ").strip()

decrypt_output = input("Enter name for decrypted output image file: ").strip()

# Prompt user  for the key and make sure it's a valid number
try:
    key = int(input("Enter encryption/decryption key (number): ").strip())
except ValueError:
    print(" Error: Key must be a number.")
    exit()

# Call the appropriate function based on the user's choice
if choice == '1':
    encrypt_image(input_path, encrypt_output, key)
elif choice == '2':
    decrypt_image(input_path, decrypt_output, key)
else:
    print(" Invalid choice. Please enter 1 or 2.")
