# Organizes files from the downloads folder into images and pdfs folders

import os
import shutil

source = "downloads"

for file in os.listdir(source):
    if file.endswith(".jpg"):
        shutil.move(source + "/" + file, "images/" + file)
    elif file.endswith(".pdf"):
        shutil.move(source + "/" + file, "pdfs/" + file)
