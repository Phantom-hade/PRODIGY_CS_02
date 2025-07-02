# PRODIGY_CS_02 – Pixel Manipulation For Image Encryption

This project is part of the **Prodigy InfoTech Cyber Security Internship – Task 02**.

##  Description
A Python tool that encrypts and decrypts images using pixel manipulation.  
Each pixel's RGB values are shifted by a user-defined numeric key.

## How It Works
- **Encryption:** Adds the key to each pixel's R, G, B values.
- **Decryption:** Subtracts the key to restore the original image.
- Pixel values are kept between 0–255 using modulo 256.

## Requirements
- Python 3.x
- Pillow library  
  Install with:
pip install pillow

## How to Use
1. Run the script:
 ```bash
 python image_manipulation.py
 Choose to encrypt or decrypt.

Provide the input image, output name, and key.
