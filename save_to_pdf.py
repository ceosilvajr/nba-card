from reportlab.lib.pagesizes import legal
import re
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_LEFT


def save(player_name: str, card_content: str):
    """
    Generates and saves the NBA player card content to a PDF file in portrait orientation
    with adjusted margins.

    Args:
        player_name (str): The name of the NBA player, used for the filename and PDF title.
        card_content (str): The text content of the NBA player card.
    """
    # Sanitize player name for filename (replace spaces with underscores, remove special chars)
    safe_player_name = "".join(c for c in player_name if c.isalnum() or c.isspace()).replace(" ", "_").lower()
    filename = f"{safe_player_name}_card.pdf"  # Changed filename to reflect portrait

    # Define margins (left, right, top, bottom)
    # These margins will now apply to a portrait page.
    left_margin = 0.75 * inch
    right_margin = 0.75 * inch
    top_margin = 0.75 * inch
    bottom_margin = 0.75 * inch

    # Create a SimpleDocTemplate with portrait orientation (just 'letter') and custom margins
    doc = SimpleDocTemplate(
        filename,
        pagesize=legal,  # Changed back to portrait
        leftMargin=left_margin,
        rightMargin=right_margin,
        topMargin=top_margin,
        bottomMargin=bottom_margin
    )
    styles = getSampleStyleSheet()
    story = []

    # Define custom bullet style
    bullet_style = ParagraphStyle(
        name='Bullet',
        parent=styles['Normal'],
        fontSize=10,
        leading=12,
        leftIndent=0.25 * inch,  # Indent the bullet point
        firstLineIndent=-0.25 * inch,  # Make the bullet character hang left
        spaceBefore=6,
        spaceAfter=0,
        bulletIndent=0,
        bulletFontSize=10,
        bulletFontName='Helvetica-Bold',  # Use a bold font for the bullet character
        alignment=TA_LEFT
    )

    # Process each line of the card content for formatting
    lines = card_content.splitlines()
    for line in lines:
        stripped_line = line.strip()

        # Handle bold text: replace **text** with <font name="Helvetica-Bold">text</font>
        # This regex looks for **...** and replaces it with ReportLab's XML-like bold tag
        formatted_line = re.sub(r'\*\*(.*?)\*\*', r'<font name="Helvetica-Bold">\1</font>', stripped_line)

        if formatted_line.startswith('- '):
            # If it's a bullet point, remove the '- ' and use the custom bullet style
            bullet_text = formatted_line[2:].strip()
            story.append(Paragraph(bullet_text, bullet_style, bulletText='• '))  # Use a solid bullet character
        elif formatted_line:  # Only add non-empty lines
            # For regular paragraphs, use a standard style
            paragraph_style = styles['Normal']
            paragraph_style.fontSize = 10
            paragraph_style.leading = 12
            story.append(Paragraph(formatted_line, paragraph_style))
        else:
            # Add a small space for empty lines to maintain paragraph separation
            story.append(Spacer(1, 0.1 * inch))

    try:
        doc.build(story)
        print(f"Successfully generated and saved '{filename}' in the current directory.")
    except Exception as e:
        print(f"Error saving PDF file '{filename}': {e}")
