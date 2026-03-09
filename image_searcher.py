from PIL import Image
import pytesseract
import os
import subprocess
import time
from multiprocessing import Pool

os.environ["TESSDATA_PREFIX"] = "/usr/share/tessdata"
folder = os.environ.get("SCREENSHOT_FOLDER", "/home/bern/Pictures/Screenshots/")
pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"
# OCR function for a single image
def text_for_image(file):
    try:
        image = Image.open(file)
        text = pytesseract.image_to_string(image)
        return file, text
    except:
        return file, ""  

# Sequential version
def search_sequential(files, search_text):
    for file in files:
        print("Looking at:", file)
        extracted_text = text_for_image(os.path.join(folder, file))[1]  
        if search_text in extracted_text.lower():
            print("Found in:", file)
            path = os.path.join(folder, file)
            process = subprocess.Popen(["gwenview", path])
            input("Press Enter to continue searching...")
            proces.terminate()
            time.sleep(0.5)

# Parallel version using Pool
def search_parallel(files, search_text):
    with Pool() as pool:
        results = pool.map(text_for_image, files)
    for file, extracted_text in results:
        print("Looking at:", file)
        if search_text in extracted_text.lower():
            print("Found in:", file)
            path = os.path.join(folder, file)
            process = subprocess.Popen(["gwenview", path])
            input("Press Enter to continue searching...")
            process.terminate()
            time.sleep(0.5)

if __name__ == "__main__":
    mode = input("Select mode: 1 = Sequential, 2 = Parallel (pooling): ").strip()
    search_text = input("Enter text to search for: ").lower()
    
    files = [os.path.join(folder, f) for f in os.listdir(folder) if f.lower().endswith((".png", ".jpg", ".jpeg"))]
    if mode == "2":
        search_parallel(files, search_text)
    else:
        search_sequential(files, search_text)
