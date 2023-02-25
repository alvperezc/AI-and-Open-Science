# AI-and-Open-Science

- Description
    This script is based on the Grobid text extraction tool.  It receives PDF files stored in the "resources" folder. It returns two images, stored in the figures folder, showing: a word cloud with the keywords of all the documents and a bar chart showing the number of images or figures that appear in each PDF document.

- Requirements
    There is a file: "pyproject.toml" where it is explained in more detail which dependencies and versions are required and supported. It is a script developed in python, using the libraries: requests, beautifulsoup, textblob and wordcloud.

- Installation instructions
    There is a docker file that will facilitate the installation. We will also have to manage in the "resources" folder the files from which we want to extract the data.
    Also there is a test that you can use before execute de main srcipt, to check that everything works.

- Execution instructions
    First it is assumed that grobid is running correctly on port 8070. Then just execute the file: "AI-and-Open-Science/nanosecurity/nanosecurity/__init__.py" to start the execution.

- Running example(s)
    Currently in the initial version there are some files loaded in "resources" about nanosafety and in the folder "figures" there are the images obtained after the execution.

- Preferred citation (who is the main author?)
    Álvaro Pérez

- Where to get help
    You can write to a.pcaceres@alumnos.upm.es, about any error or help you may need.

