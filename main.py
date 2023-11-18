import os
import csv
from PIL import Image
import pytesseract
import re
# extract eden scores
# @black P1F 292
# yes I am a pirate, 200 years too late. 

image_directory = '~/.code/lss/ocr_eden/scores/'
output_csv_path = 'extracted_scores.csv'

patterns_contribution = {
    'user_id': re.compile(r'\[.*?\] (\w+)'),
    'contribution': re.compile(r'Contribution.*?([\d,]+)'),
    'ranking': re.compile(r'Ranking\s+(\d+)'),
    'season_points': re.compile(r'Season points\s+(\d+,\d+)'),
    'eden_demolition': re.compile(r'Eden Demolition\s+(\d+,\d+)'),
    'eden_feat': re.compile(r'Eden Feat\s+([\d,]+)'),
    'occupy_enemy_territory': re.compile(r'Occupy Enemy Territory\s+(\d+)')
}
def extract_numeric(value):
    return int(value.replace(',', '')) if value.replace(',', '').isdigit() else value

with open(output_csv_path, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=list(patterns_contribution.keys()))
    writer.writeheader()
    for filename in os.listdir(image_directory):
        if filename.endswith('.jpeg'):
            file_path = os.path.join(image_directory, filename)
            try:
                with Image.open(file_path) as img:
                    text = pytesseract.image_to_string(img)
                    extracted_data = {field: None for field in patterns_contribution.keys()}
                    for field, pattern in patterns_contribution.items():
                        match = pattern.search(text)
                        if match:
                            extracted_data[field] = extract_numeric(match.group(1))
                    writer.writerow(extracted_data)
            except IOError as e:
                print(f"Cannot open {file_path}. Error: {e}")
print(f"I hope it worked... {output_csv_path}")
