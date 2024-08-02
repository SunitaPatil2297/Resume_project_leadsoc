# importing modules 
from reportlab.pdfgen import canvas 
from reportlab.pdfbase.ttfonts import TTFont 
from reportlab.pdfbase import pdfmetrics 
from reportlab.lib import colors 
from reportlab.lib.pagesizes import letter
# initializing variables with values 
fileName = 'sample.pdf'
documentTitle = 'sample'
title = 'Technology'
subTitle = 'The largest thing now!!'
textLines = [ 
    'Technology makes us aware of', 
    'the world around us.', 
] 
image = r'leadsoc.jfif'
  
# creating a pdf object 
pdf = canvas.Canvas(fileName, image) 
  
# setting the title of the document 
pdf.setTitle(documentTitle) 
  
# registering a external font in python 
# pdfmetrics.registerFont( 
#     TTFont('abc', 'SakBunderan.ttf') 
# ) 
pdfmetrics.registerFont(TTFont('SakBunderan', r"C:\Users\Lead Soc\Downloads\sakbunderan-cufonfonts\SakBunderan.ttf"))

    # Set the custom font
pdf.setFont('SakBunderan', 12)
# creating the title by setting it's font  
# and putting it on the canvas 
# pdf.setFont('SakBunderan', 12)
# pdf.setFont('abc', 36) 
pdf.drawCentredString(300, 770, title) 
  
# creating the subtitle by setting it's font,  
# colour and putting it on the canvas 
pdf.setFillColorRGB(0, 0, 255) 
pdf.setFont("Courier-Bold", 24) 
pdf.drawCentredString(290, 720, subTitle) 
  
# drawing a line 
pdf.line(30, 710, 550, 710) 
  
# creating a multiline text using  
# textline and for loop 
text = pdf.beginText(40, 680) 
text.setFont("Courier", 18) 
text.setFillColor(colors.red) 
for line in textLines: 
    text.textLine(line) 
pdf.drawText(text) 
  
# drawing a image at the  
# specified (x.y) position 
pdf.drawInlineImage(image, 60, 2) 
  
# saving the pdf 
pdf.save() 
print("done")

# class MyCanvas(canvas.Canvas):
#     def __init__(self, *args, image_path=None, header_text=None, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.image_path = image_path
#         self.header_text = header_text

#     def showPage(self):
#         self.draw_image_and_header()
#         super().showPage()

#     def save(self):
#         self.draw_image_and_header()
#         super().save()

#     def draw_image_and_header(self):
#         if self.image_path:
#             self.drawImage(self.image_path, x=0, y=0, width=letter[0], height=letter[1], mask='auto')
#         if self.header_text:
#             self.setFont("SakBunderan", 12)
#             self.drawString(100, letter[1] - 50, self.header_text)

# def create_pdf_with_image_and_header(pdf_path, font_path, image_path, header_text, text):
#     pdfmetrics.registerFont(TTFont('SakBunderan', font_path))
#     c = MyCanvas(pdf_path, pagesize=letter, image_path=image_path, header_text=header_text)
#     c.setFont('SakBunderan', 12)

#     # Add some text to the first page
#     c.drawString(100, 700, text)
#     c.showPage()

#     # Add another page with text
#     c.drawString(100, 700, "Another page with the same image background and header.")
#     c.showPage()

#     c.save()

# font_path =  r"C:\Users\Lead Soc\Downloads\sakbunderan-cufonfonts\SakBunderan.ttf"
# image_path = "leadsoc.jfif"
# pdf_path = "output.pdf"
# header_text = "This is the header text"
# text = "Hello, World!"

# create_pdf_with_image_and_header(pdf_path, font_path, image_path, header_text, text)