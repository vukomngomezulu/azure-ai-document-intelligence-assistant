import os
import docx


def extract_text(file_path: str) -> str:
    """
    Extract text from PDF, DOCX or TXT without Azure.
    """

    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".txt":
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()

    elif extension == ".docx":
        doc = docx.Document(file_path)
        return "\n".join(
            paragraph.text
            for paragraph in doc.paragraphs
        )

    elif extension == ".pdf":
        try:
            import pypdf
        except ImportError:
            raise Exception(
                "Please install pypdf:\n\npip install pypdf"
            )

        reader = pypdf.PdfReader(file_path)

        text = ""

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

        return text

    else:
        raise Exception("Unsupported file type.")