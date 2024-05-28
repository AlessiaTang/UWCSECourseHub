# The new information structure -- The UW CSE Course Resource API is built in this process:

- Object Targeting: find the resource webpage of a CSE Course of a certain quarter, for example, the [calender page of CSE312 in 23 spring quarter](https://courses.cs.washington.edu/courses/cse312/23sp/calendar/calendar.html).
- Web Scraping: uss python and BeautifulSoup to scrape all the lecture resource links from the resource webpage above.
- Data Manipulation: use python to extract the required data from the scraped html element. For example, using `lecture_divs = soup.find_all("div", class_="lecture")` to extract all "div" elements with the class "lecture". Then extracting the lecture description as well as lecture links, combining each lecture description and links into a dictionary, and appending all dictionaries to a list. Last, converting the list of dictionaries to a JSON format, and exporting it to a JSON file.
- Flask API Building: use Flask and Python to create routes to build the API. For example, for the '/CSE312/23sp/' route, let the API return all the content in the JSON file exported above. For the '/CSE312/23sp/<keyword>' route, where users can input the lecture keyword that interests them, the API will return related value from the JSON file.
- Resource and Function Generalizing: enrich the course resources supported by the API, by taking more web scraping and more API routes building. Up to presentation, the supported courses and quarters include:
  <br> CSE312 23sp 24sp<br>
  <br> CSE332 23sp 24sp<br>
  <br> CSE333 24sp<br>
  <br> CSE401 24sp<br>
  <br> CSE414 24sp<br>
  <br> CSE417 24wi<br>

Therefore, it is possible to access the information as described in the Ideate documentation, and the information provided is correct and complete as described in the information story.
