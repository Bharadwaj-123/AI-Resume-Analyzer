from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(result, filename="Resume_Report.pdf"):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b>AI Resume Analyzer Report</b>", styles["Title"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph(f"<b>Resume Score:</b> {result['score']}/100", styles["Heading2"]))

    story.append(Paragraph(f"<b>ATS Score:</b> {result['ats']}%", styles["Heading2"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph("<b>Skills Found</b>", styles["Heading2"]))

    for skill in result["found"]:
        story.append(Paragraph("• " + skill, styles["BodyText"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph("<b>Missing Skills</b>", styles["Heading2"]))

    for skill in result["missing"]:
        story.append(Paragraph("• " + skill, styles["BodyText"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph("<b>Suggestions</b>", styles["Heading2"]))

    suggestions = [

        "Add GitHub Profile",

        "Add Certifications",

        "Improve Resume Summary",

        "Mention Internship Experience",

        "Add Quantified Achievements"

    ]

    for s in suggestions:
        story.append(Paragraph("• " + s, styles["BodyText"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph("<b>Recommended Roles</b>", styles["Heading2"]))

    roles = []

    if "Python" in result["found"]:
        roles.append("Python Developer")

    if "Machine Learning" in result["found"]:
        roles.append("Machine Learning Engineer")

    if "Artificial Intelligence" in result["found"]:
        roles.append("AI Engineer")

    if "SQL" in result["found"]:
        roles.append("Data Analyst")

    if not roles:
        roles.append("Software Developer")

    for r in roles:
        story.append(Paragraph("• " + r, styles["BodyText"]))

    doc.build(story)

    return filename