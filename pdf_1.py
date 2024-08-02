from weasyprint import HTML

html_content = """
<html>
  <head>
    <style>
      body { font-family: Arial, sans-serif; }
      h1 { text-align: center; }
      p { font-size: 16px; }
    </style>
  </head>
  <body>
    <h1>Title</h1>
    <h2>Subtitle</h2>
    <p>Here is some content for the PDF.</p>
  </body>
</html>
"""

# Create PDF from HTML
HTML(string=html_content).write_pdf("sample.pdf")