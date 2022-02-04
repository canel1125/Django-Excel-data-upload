
# Upload Excel spreadsheet information to Django



## Documentation content
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
This project is an exercise where I make a page who lets upload data stored in a Excel file into the database using Django, SQLite3 and VueJs. 

	
## Technologies
Project uses the following dependencies:

#### Frontend 
* Axios: 0.25.0
* Bootstrap: 5.1.3
* Convert-excel-to-json: 1.7.0
* Vue: 3.0
* Xlsx: 0.18.0
#### Backend
* Django: 4.0.1
* Django_cors_headers=: 3.11.0
* Django_environ: 0.8.1
* Djangorestframework: 3.13.1
* Environ: 1.0
* SQLite3


	
## Setup

#### Install necessary software

* #### Node.js.

    You can get Node.js clicking this button
    [![Nodejs](https://img.shields.io/badge/Node.js-v16.13.1-brightgreen)](https://nodejs.org/es/)
    or here: https://nodejs.org/es/

    If you already have Node.js installed in your device, just make sure that it is a version higher than 16.13.1.


* #### Python.

    You can get Python clicking this button
    [![Python](https://img.shields.io/badge/Python-%5E3.10%20-blue)](https://www.python.org/downloads/)
    or here: https://www.python.org/downloads/

* Execute file dependency_installer.sh

    It will install all necessary dependencies, modules and make migrations.

## Run App
To run the application you must execute this two files:
* #### start_backendserver.sh
&emsp; this file run the backend server with Django.


* #### start_frontendserver.sh
&emsp; this file run the frontend server with Vuejs.

And go to http://localhost:8080/ or http://192.168.0.14:8080/