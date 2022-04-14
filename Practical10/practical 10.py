
import img2pdf
from PIL import Image
import os

imp_path = "E:\\Unviversity Result\\s- 3.png"

pdf_path = "E:\\Unviversity Result\\s- 3.pdf"

image = Image.open(imp_path)

pdf_bytes = img2pdf.convert(image.filename)

file = open(pdf_path, "wb")

file.write(pdf_bytes)

image.close()

file.close()
print()
print("Yay!, Your pdf was created successfully! :)")
print()