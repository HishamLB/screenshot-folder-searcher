This tiny script will search a directory for a specific search keyword.
Supports 2 modes: 
- Sequential: each image is scanned for the word in order.
- Parallel: this uses pooling and first scans all the images and gets result, then opens one-by-one.

### Gwenview is required (probably will add option to change image viewer later)

### Pytesseract and Pillow are required: 
- pip install Pillow pytesseract

### Specify path by: 
- export SCREENSHOT_FOLDER="enter/your/path/here/"
