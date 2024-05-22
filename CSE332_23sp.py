from requests import get
from bs4 import BeautifulSoup
import json
import re
from urllib.parse import urljoin


response = get('https://courses.cs.washington.edu/courses/cse332/23sp/calendar/calendar.html')

soup = BeautifulSoup(response.text, 'html.parser')

lecture_divs = soup.find_all("div", class_="lecture")

lecture_data = []

base_url = "https://courses.cs.washington.edu/courses/cse332/23sp/"

for div in lecture_divs:

    description_span = div.find("span", class_="description")
    
    # Check if the <span> element exists
    if description_span:
        # Extract lecture description
        description = description_span.get_text()
    else:
        # If <span> element is not found, set description to None or handle the case accordingly
        description = None

    materials_span = div.find("span", class_="materials")
    if materials_span:
        links = [urljoin(base_url, "lecture/" + a["href"]) for a in materials_span.find_all("a")]
    else:
        links = []
    
    # Combine lecture description and links into a dictionary
    lecture_info = {"lecture description": description, "links": links}

    # Append dictionary to list
    lecture_data.append(lecture_info)

# Convert list of dictionaries to JSON format
json_data = json.dumps(lecture_data, indent=4)

# Print or save JSON data
print(json_data)

# Save JSON data to file
with open("CSE332_23sp_lecture.json", "w") as file:
    file.write(json_data)

#find all links that contain "lecture" in the link
#print(soup.find_all(href=re.compile("lecture")))
#find all links that contain "pdf" in the text
#print(soup.find_all("a", string="pdf")) or 
#print(soup.find_all("a", string=["pdf", "pptx"]))



#for link in soup.find_all('a'):
#links_json = json.dumps(link.get('href'))
#print(links_json)



#with open('cse312.json', 'w', encoding='utf-8') as f:
#    f.write(response.text)