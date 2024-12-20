import cv2
import pytesseract
import os


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_speed_and_distance(image_path):

    if not os.path.exists(image_path):
        print("Image file not found. Check the path.")
        return


    img = cv2.imread(image_path)


    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)


    extracted_text = pytesseract.image_to_string(thresh)


    print("Extracted Text from Image:")
    print(extracted_text)

    #varbl to hold speed and distance
    speed = None
    distance = None
    for line in extracted_text.split("\n"):
        if "speed" in line.lower():

            try:
                speed = int([word for word in line.split() if word.isdigit()][0])
            except IndexError:
                pass
        if "distance" in line.lower():

            try:
                distance = int([word for word in line.split() if word.isdigit()][0])
            except IndexError:

              if speed is not None:
                   print(f"Speed: {speed} km/h")
            else:
                print("Speed information not found.")

               if distance is not None:
                    print(f"Distance: {distance} km")
                else:
                    print("Distance information not found.")


extract_speed_and_distance("images/speed.png")