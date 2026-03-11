from reportlab.pdfgen import canvas

def generate_pdf(text):

    file = "AI_Report.pdf"

    c = canvas.Canvas(file)

    c.setFont("Helvetica", 12)

    y = 800

    for line in text.split("\n"):
        c.drawString(50, y, line)
        y -= 20

    c.save()

    return file