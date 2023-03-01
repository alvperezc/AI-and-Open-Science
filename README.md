# AI-and-Open-Science

## Description
This script is based on the Grobid text extraction tool.  It receives PDF files stored in the "resources" folder. It returns two images, stored in the figures folder, showing: a word cloud with the keywords of all the documents and a bar chart showing the number of images or figures that appear in each PDF document.

## Requirements
There is a file: "pyproject.toml" where it is explained in more detail which dependencies and versions are required and supported. It is a script developed in python, using the libraries: requests, beautifulsoup, textblob and wordcloud.

## Installation instructions
There is a docker file that will facilitate the installation. 
        
In order to run the program correctly, you have to follow these first installation steps:

1) Clone the repository can be done using the command: 

```bash
git clone https://github.com/alvperezc/AI-and-Open-Science.git
```

2) Create a network to be able to run Grobid and this connecter correctly and synchronously: 

```bash
docker network create <network_name>
```
where <network_name> is the name you want to give to the network.

3)Download Grobid(In case it is not downloaded and it is necessary, or in case you have problems with other versions):

```bash 
docker pull lfoppiano/grobid:0.7.2
```

4)Run Grobid: 

```bash
docker run --name grobid --network <network_name> -t --rm -p 8070:8070 lfoppiano/grobid:0.7.2
```
where <network_name> is the previous name given to the network

5)Create a build of the dockerfile:

```bash
docker build -t dockerfile . 
```
is run from "." as direct root when cloning the repository, if it is found in another directory replace with the directory where you moved the file to

6)Run the container with the script and files:

```bash
docker run --rm -it --network <network_name> -v <mount_directory>:/ExtractText/resources dockerfile
```
again in <network_name> replace with the same name assigned above. In <mount_directory> replace with a local directory where all the PDFs you want to extract information from are located.

You are now inside the container to start executing


## Execution instructions
To start running the program first we will have to activate the poetry environment installed by means of:

```bash
poetry shell
```

Before starting, it is recommended to first run the tests found in the tests folder:
1) Go to the directory using:

```bash
cd tests
```

2) Once inside, run the file with python through the envarioment created with poetry:

```bash
poetry run python3 __init__.py
```

3) Once we have passed the tests we can return to the main directory and go to the textextraction folder where the executable will be, we can initialize it using the following command:

```bash
poetry run python3 __init__.py
```

Once executed, it will start working showing on screen all the links it has found from the different texts analyzed. And now in the local folder, which was previously configured as <mount_directory> a new folder called "figures" will appear with the two images where the word cloud and the graph with the number of images per PDF will be displayed.


## Running example(s)
Currently in the initial version there are some files loaded in "resources" about nanosafety and in the folder "figures" there are the images obtained after the execution.

## Preferred citation 
Álvaro Pérez Cáceres

## Where to get help
You can write to a.pcaceres@alumnos.upm.es, about any error or help you may need.

