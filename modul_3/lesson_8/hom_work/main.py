
import pandas as pd

# class Pandas_read():
#     def read_csv(self):


# import fitz
#
# def extract_images_from_pdf(pdf_file):
#     try:
#         pdf_document = fitz.open(pdf_file)
#         for page_num in range(len(pdf_document)):
#             page = pdf_document.load_page(page_num)
#             image_list = page.get_images(full=True)
#
#             for img_index, img in enumerate(image_list):
#                 xref = img[0]
#                 base_image = pdf_document.extract_image(xref)
#                 image_data = base_image["image"]
#
#                 image_format = base_image["ext"]
#
#                 with open(f"image_{page_num + 1}_{img_index + 1}.{image_format}", "wb") as image_file:
#                     image_file.write(image_data)
#
#         print(f"Rasmlar dan olingan '{pdf_file}' va jildga saqlangan..")
#
#     except Exception as e:
#         print(f"Xatolik yuz berdi: {str(e)}")
#
#
# pdf_file_path = "/home/shokhake/PycharmProjects/P17group/modul_3/lesson_8/hom_work/Untitled design.pdf"
# extract_images_from_pdf(pdf_file_path)


from pypdf import PdfReader

reader = PdfReader("/home/shokhake/PycharmProjects/P17group/modul_3/lesson_8/hom_work/Untitled design.pdf")
for page in reader.pages:
    for image in page.images:
        with open(image.name, "wb") as f:
            f.write(image.data)

