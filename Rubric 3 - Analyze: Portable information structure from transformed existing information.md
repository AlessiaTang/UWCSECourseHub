# The new information structure is different from the existing information in a substantial way, including:

## information itself/the structure/ the format:

For existing information, the information is in HTML format, composed of a bunch of elements with different HTML tags and attributes. The needed information (lecture resource links) are covered by many layers of unrelated information.
For the new information structure: each API endpoint returns a JSON file, clearly composed by lectore contains an array of objects, each representing a lecture. Each lecture object has two properties:

- "lecture description": this property contains a string describing the lecture.
- "links": this property contains an array of URLs representing the links to various resources related to the lecture.

Here's the information schema of the JSON file:

{
"lecture description": "String",
"links": ["String", "String", ...]
}

## The access methodology:

For existing information: Access to the data is typically through web browser and search engine – first find the UW CSE course website, then the single course page, then the single course calendar HTML pages
For the new information structure: The UW CSE Course Resource API is accessed in this process:

- Open the Chrome browser;
- Homepage will show the usage of the product, and also display all the courses that already supported by the product.
- Input the course name (such as /CSE312) as the API endpoint, get the introduction of a certain course;
- Input the course name and course quarter (such as /CSE312/23sp) as the API endpoint, get all the lecture resource links of a certain course in a certain quarter;
- Input the course name, course quarter, and the interested topic keyword (such as /CSE312/23sp/counting) as the API endpoint, get all the lecture resource links of a certain course in a certain quarter, while the corresponding lecture descrption include the topic keyword;
- Click on the resources to view or download.

# Also, the new information structure clearly meets the requirements identified in the information story, according to the demo and Read.me.
