import qrcode

# Define the URL you want to encode
url = "https://admissionsml-roufvjyxr45gbhtnmmqv4n.streamlit.app/"

# Generate the QR code
img = qrcode.make(url)

# Save the QR code as a PNG file
img.save("qr_code_example.png")