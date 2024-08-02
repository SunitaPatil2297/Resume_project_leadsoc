

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem


class Txt_to_PDF:
    
    def txt_to_pdf(txt_file_path, output_pdf_path):

        # output_pdf_path = 
        
        doc = SimpleDocTemplate(output_pdf_path, pagesize=letter)
        
        
        styles = getSampleStyleSheet()
        title_style = styles['Title']
        heading_style = styles['Heading1']
        subheading_style = styles['Heading2']
        bullet_style = ParagraphStyle(name='Bullet', fontName='Helvetica', fontSize=12, spaceAfter=10)
        
        
        content = []

        
        with open(txt_file_path, 'r') as file:
            lines = file.readlines()
                                                                                                                                                           
        
        def add_paragraph(text, style):
            content.append(Paragraph(text, style))
        
        
        for line in lines:
            line = line.strip()
            if line.startswith('## '):
                
                add_paragraph(line[3:], title_style)
                content.append(Spacer(1, 12))
            elif line.startswith('### '):
                
                add_paragraph(line[4:], heading_style)
                content.append(Spacer(1, 12))
            elif line.startswith('**'):
                
                add_paragraph(line[2:-2], subheading_style)
                content.append(Spacer(1, 12))
            elif line.startswith('*'):
                
                content.append(ListFlowable([ListItem(Paragraph(line[1:], bullet_style))], bulletType='bullet'))
            else:
                
                add_paragraph(line, styles['Normal'])
        
        
        doc.build(content)


    txt_to_pdf("1.txt", "y.pdf")