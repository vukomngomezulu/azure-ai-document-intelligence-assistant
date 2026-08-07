import os


def extract_document(path: str):
    """
    Local document extractor.
    Currently supports .txt files.
    """

    extension = os.path.splitext(path)[1].lower()

    if extension == ".txt":
        with open(path, "r", encoding="utf-8") as f:
            return f.read()

    raise Exception(
        f"{extension} files are not supported yet."
    )


def get_document_text(result):
    return result