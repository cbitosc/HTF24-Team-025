from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.pdfgen import canvas

def add_header(canvas, header_text):
    # Set the color for the header
    header_color = colors.lightblue
    canvas.saveState()
    canvas.setFillColor(header_color)
    
    # Draw a colored rectangle for the header
    canvas.rect(0, 750, 600, 50, fill=1)  # Adjust the coordinates and size as needed
    
    # Set the text color for the header
    canvas.setFillColor(colors.black)
    canvas.drawString(10, 765, header_text)  # Adjust position for header text
    canvas.restoreState()

def format_content(content):
    """
    Format content by adding bullet points and line breaks after every 3-4 sentences.
    """
    # Split the content into sentences using '. ' as the delimiter
    sentences = content.split('. ')
    formatted_paragraphs = []

    for i in range(len(sentences)):
        # Ensure each sentence ends with a period
        sentence = sentences[i].strip()
        if sentence and not sentence.endswith('.'):
            sentence += '.'  # Add period if missing
        
        # Create bullet point for each sentence
        formatted_paragraphs.append(f'• {sentence}')  # Bullet point
        
        # Add a double line break after every 4 sentences
        if (i + 1) % 4 == 0:  # Add space after every 4 sentences
            formatted_paragraphs.append('')  # This will add a blank line in the final PDF
            formatted_paragraphs.append('')  # Add another blank line for double spacing
            
    return formatted_paragraphs

def create_pdf(filename, heading, content):
    document = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()

    # Create a list to hold the content
    pdf_content = []

    # Add the heading to the document
    pdf_content.append(Paragraph(heading, styles['Heading1']))
    pdf_content.append(Spacer(1, 12))  # Space after heading

    # Format the content to add bullet points and line breaks
    formatted_content = format_content(content)

    # Add formatted content to the document
    for paragraph in formatted_content:
        if paragraph:  # Only add non-empty paragraphs
            pdf_content.append(Paragraph(paragraph, styles['Normal']))
        pdf_content.append(Spacer(1, 6))  # Space after each sentence/paragraph

    # Build the PDF
    document.build(pdf_content, 
                   onFirstPage=lambda c, d: add_header(c, "PDF Conversion"), 
                   onLaterPages=lambda c, d: add_header(c, "PDF Conversion"))

# Heading and content
# heading = "PDF Conversion"
# content = """Industrialization is the process that takes an agricultural economy and transforms it into a manufacturing one. Mass production and assembly lines replace manual and specialized laborers. The process has historically led to urbanization by creating economic growth and job opportunities that draw people to cities.Urbanization typically begins when a factory or multiple factories are established within a region, creating a high demand for factory labor. Other businesses such as building manufacturers, retailers, and service providers then follow the factories to meet the product demands of the workers. This creates even more jobs and demands for housing and establishes an urban area.Manufacturing facilities like factories are often replaced by technology-industry hubs in the modern era. These technological hubs draw workers from other areas in the same way factories did, contributing to urbanization.Key TakeawaysIndustrialization transforms an agricultural economy into a manufacturing economy.Urbanization is characterized by the growth of cities.Industrialization ushered in a shift from farming to agribusiness.People began moving into urban centers as mechanization and production increased.Urbanization continues as areas go through cycles of economic and social reform.Urbanization Occurs Near Bodies of WaterUrbanization patterns have been the strongest throughout history when they're near large bodies of water. This was initially to meet the food and water needs of large populations. The need for water became increasingly important as humans moved from hunter-gatherers to cultivators. People began to rely on cultivated crops rather than looking for their food.This led to the use of land as a resource. People could produce food through the cultivation of crops so the need for water became even more pronounced. Humans began using water systems such as wells and runoff systems to meet their needs. A rise in demand for cultivated crops ushered in newer technologies in the irrigation system. People developed canals, dams, and storage facilities to help transfer and store the water they needed. content = Industrialization is the process that takes an agricultural economy and transforms it into a manufacturing one. Mass production and assembly lines replace manual and specialized laborers. The process has historically led to urbanization by creating economic growth and job opportunities that draw people to cities.Urbanization typically begins when a factory or multiple factories are established within a region, creating a high demand for factory labor. Other businesses such as building manufacturers, retailers, and service providers then follow the factories to meet the product demands of the workers. This creates even more jobs and demands for housing and establishes an urban area.Manufacturing facilities like factories are often replaced by technology-industry hubs in the modern era. These technological hubs draw workers from other areas in the same way factories did, contributing to urbanization.Key TakeawaysIndustrialization transforms an agricultural economy into a manufacturing economy.Urbanization is characterized by the growth of cities.Industrialization ushered in a shift from farming to agribusiness.People began moving into urban centers as mechanization and production increased.Urbanization continues as areas go through cycles of economic and social reform.Urbanization Occurs Near Bodies of WaterUrbanization patterns have been the strongest throughout history when they're near large bodies of water. This was initially to meet the food and water needs of large populations. The need for water became increasingly important as humans moved from hunter-gatherers to cultivators. People began to rely on cultivated crops rather than looking for their food.This led to the use of land as a resource. People could produce food through the cultivation of crops so the need for water became even more pronounced. Humans began using water systems such as wells and runoff systems to meet their needs. A rise in demand for cultivated crops ushered in newer technologies in the irrigation system. People developed canals, dams, and storage facilities to help transfer and store the water they needed."""

# # Create the PDF
# create_pdf("industrialization_text_conversion.pdf", heading, content)

# print("PDF created successfully.")
