from weasyprint import HTML
import markdown

def export_to_pdf(summary_md):
    html = markdown.markdown(summary_md)
    HTML(string=html).write_pdf("bias_report.pdf")
