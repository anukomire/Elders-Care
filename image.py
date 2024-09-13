import pytesseract
from PIL import Image
import re
from datetime import datetime

# Function to extract text from image using pytesseract
def extract_text_from_image(image_path):
    # Load the image
    image = Image.open('adhar4.jpeg')
    # Use pytesseract to do OCR on the image
    text = pytesseract.image_to_string(image)
    return text

# Function to find date of birth in the extracted text
def find_date_of_birth(text):
    # Define a regex pattern to match dates (assuming format is DD-MM-YYYY or similar)
    date_pattern = r'\b(?:\d{1,2}[-/th|st|rd|nd\W]\d{1,2}[-/th|st|rd|nd\W]\d{2,4})\b'
    matches = re.findall(date_pattern, text)
    if matches:
        # If matches are found, return the first one
        return matches[0]
    return None

# Function to calculate age from date of birth
def calculate_age(date_of_birth):
    # Parse the date of birth
    try:
        dob = datetime.strptime(date_of_birth, '%d-%m-%Y')
    except ValueError:
        # Try another common format if needed
        dob = datetime.strptime(date_of_birth, '%d/%m/%Y')

    # Get the current date
    today = datetime.today()
    # Calculate age
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    return age

# Main function to process image and calculate age
def main(image_path):
    # Extract text from image
    text = extract_text_from_image(image_path)
    print(f"Extracted Text: {text}")
    
    # Find date of birth in the text
    date_of_birth = find_date_of_birth(text)
    if date_of_birth:
        print(f"Date of Birth Found: {date_of_birth}")
        # Calculate age
        age = calculate_age(date_of_birth)
        print(f"Age: {age} years")
    else:
        print("Date of Birth not found in the image")

# Example usage
image_path = 'path_to_your_image.jpg'  # Replace with your image path
main(image_path)
