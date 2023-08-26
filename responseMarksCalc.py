import pdfplumber
import re

pdf_path = "pdfName.pdf"

pdf = pdfplumber.open(pdf_path)
page = pdf.chars

pattern = re.compile(r'\d+(\.\d+)?')  # Regular expression pattern to match numbers

numbers = []

for char_info in page:
    non_stroking_color = char_info['non_stroking_color']
    if non_stroking_color == (0.251, 0.7765, 0.2941):
        text = char_info['text']
        match = pattern.match(text)
        if match:
            numbers.append(match.group())
            
chosen_option_pattern = re.compile(r'Chosen Option :(.+)')

chosen_options = []

pdf=pdfplumber.open(pdf_path)
for page in pdf.pages:
    text = page.extract_text()
    matches = chosen_option_pattern.findall(text)
    chosen_options.extend(matches)



pdf.close()
# print("Extracted Chosen Options:", chosen_options)
# print("Extracted Numbers:", numbers)


count=0
correct_options=0
wrong_options=0
unanswered=0
for i in range(0, len(chosen_options)):
    if(numbers[i]==chosen_options[i]):
        count+=1
        correct_options+=1
    elif (chosen_options[i]=='--'):
        unanswered+=1
    else:
        count-=0.25
        wrong_options+=1