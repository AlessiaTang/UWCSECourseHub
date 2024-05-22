# How to Access the UW CSE Course Resource API

## About

This repository is for the UW CSE Course Resource API. The target users are people outside of the UW CSE School who want to query and get the online resources of various CSE courses at various quarters of various topis at one step. By calling the API, user can input the course number (such as CSE312), course quarter (such as 23sp), and the course topic keyword (such as counting), then the API will return all the related lecture resource links (including .pptx and .pdf formats) of the corresponding request.

## Methodology

The UW CSE Course Resource API is built in this process:

- Object Targeting: find the resource webpage of a CSE Course of a certain quarter, for example, the [calender page of CSE312 in 23 spring quarter](https://courses.cs.washington.edu/courses/cse312/23sp/calendar/calendar.html).
- Web Scraping: uss python and BeautifulSoup to scrape all the lecture resource links from the resource webpage above.
- Data Manipulation: use python to extract the required data from the scraped html element. For example, using `lecture_divs = soup.find_all("div", class_="lecture")` to extract all "div" elements with the class "lecture". Then extracting the lecture description as well as lecture links, combining each lecture description and links into a dictionary, and appending all dictionaries to a list. Last, converting the list of dictionaries to a JSON format, and exporting it to a JSON file.
- Flask API Building: use Flask and Python to create routes to build the API. For example, for the '/CSE312/23sp/' route, let the API return all the content in the JSON file exported above. For the '/CSE312/23sp/<keyword>' route, where users can input the lecture keyword that interests them, the API will return related value from the JSON file.
- Resource and Function Generalizing: enrich the course resources supported by the API, by taking more web scraping and more API routes building. Lastly, use nGrok to make it public.

## Access

The UW CSE Course Resource API is accessed in this process:

- Open the Chrome browser;
- Input the course name (such as /CSE312) as the API endpoint, get all the lecture resource links of a certain course;
- Input the course name and course quarter (such as /CSE312/23sp) as the API endpoint, get all the lecture resource links of a certain course in a certain quarter;
- Input the course name, course quarter, and the interested topic keyword (such as /CSE312/23sp/counting) as the API endpoint, get all the lecture resource links of a certain course in a certain quarter, while the corresponding lecture descrption include the topic keyword;
- Click on the resources to view or download.

## Structure

The information schema of each lecture resource JSON file contains an array of objects, each representing a lecture. Each lecture object has two properties:

- "lecture description": this property contains a string describing the lecture.
- "links": this property contains an array of URLs representing the links to various resources related to the lecture.

Here's the information schema of the JSON file:

{
"lecture description": "String",
"links": ["String", "String", ...]
}

## Example

Example request:

http://127.0.0.1:5000/CSE312/23sp/prob

Example response:

[
{
lecture description: "Discrete Probability",
links: [
"https://courses.cs.washington.edu/courses/cse312/23sp/lecture/05-probability.pptx",
"https://courses.cs.washington.edu/courses/cse312/23sp/lecture/05-probability.pdf",
"https://courses.cs.washington.edu/courses/cse312/23sp/lecture/05-activity.pdf",
"https://courses.cs.washington.edu/courses/cse312/23sp/lecture/05-probability-a.pdf",
"https://courses.cs.washington.edu/courses/cse312/23sp/lecture/05-probability-b.pdf"
]
},
{
lecture description: "Continuous Probability",
links: [
"https://courses.cs.washington.edu/courses/cse312/23sp/lecture/15-continuous.pptx",
"https://courses.cs.washington.edu/courses/cse312/23sp/lecture/15-continuous.pdf",
"https://courses.cs.washington.edu/courses/cse312/23sp/lecture/15-activity.pdf",
"https://courses.cs.washington.edu/courses/cse312/23sp/lecture/15-continuous-a.pdf",
"https://courses.cs.washington.edu/courses/cse312/23sp/lecture/15-continuous-b.pdf"
]
}
]

## TODOs

rerun CSE414_24sp.py

## Index

CSE312: Foundations of Computing II
https://courses.cs.washington.edu/courses/cse312/23sp/calendar/calendar.html

CSE 332: Data Structures and Parallelism
https://courses.cs.washington.edu/courses/cse332/23sp/calendar/
