
# CRUD Application Documentation

Welcome to the documentation for our CRUD (Create, Read, Update, Delete) application. This documentation provides an overview of the CRUD operations, setup instructions for Windows, Linux, and macOS users, and includes a section on UML diagrams.

Here is a **[link](https://apholyrender.cleverapps.io/docs)** to a live version of this application.

## Setup

 Follow the instructions below to setup the application on your local machine.

### Windows

1. **Install Python:** Download and install Python from [python.org](https://www.python.org/downloads/).
2. **Clone the Repository:** Use `git clone` to clone the application [repository](https://github.com/Apholyrender/hngx-2-revision).

3. **Install Dependencies:** Navigate to the project directory and run the following command to install required packages:

            pip install -r requirements.txt

### Linux & macOS

1. **Install Python:** Most Linux distributions and macOS come with Python pre-installed. You can verify by running `python --version`.

2. **Clone the Repository:** Use `git clone` to clone the application [repository](https://github.com/Apholyrender/hngx-2-revision).

3. **Install Dependencies:** Navigate to the project directory and run the following command to install required packages:

          pip install -r requirements.txt

## Database Setup

The application uses SQLite as its database. You can download and install from [SQLite](https://www.sqlite.org/download.html).

After installing SQLite, you add the following environment variables to your system:

    FACTORY= FALSE  ( setting this to false typically means disabling the ability to create a new database file if it doesn't already exist)
    DATABASE_URL= The URI for your SQLite database


## Running the Application

After setting up the application, you can run it by running the following command in the project directory:

    python server.py

## Testing

You can run a test uisng using local host:

- After running the server, do a ctr + click on the localhost **[Localhost](http://localhost:8000/)** add docs after the / to take you to the swagger page where you can run your test.


## API Documentation

Click the **[link](https://github.com/Apholyrender/hngx-2-revision/blob/main/DOCUMENTATION.md)** to read the api documentation.


I have provided E-R diagrams for a high-level flowchart of API endpoints, interactions with the database, error handling, and response handling. You can find the E-R diagrams in the link below.

**[E-R Diagrams](https://drive.google.com/drive/folders/1zKCnxLs93sNTjjDFygSZXWQHX0J03nJU)**


## UML Diagrams

I have provided UML diagrams for a visual representation of our application's structure. You can find the UML diagrams in the link below.

**[UML Diagrams](https://drive.google.com/drive/folders/1zKCnxLs93sNTjjDFygSZXWQHX0J03nJU)**

## E-R Diagrams




