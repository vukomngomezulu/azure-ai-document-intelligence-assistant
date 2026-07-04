from pathlib import Path
import shutil

UPLOAD_FOLDER = Path("uploads")

UPLOAD_FOLDER.mkdir(exist_ok=True)


def save_file(file):

    destination = UPLOAD_FOLDER / file.filename

    with destination.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return destination