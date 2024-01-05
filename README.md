# Note-App

Note App is a web application where users can easily save and organize their notes.

# **Installation**

**1. Installation of Requirements**


- Ensure that Python 3.10 or a newer version is installed.

- To run the project, install Flask and other dependencies using the following command:

      pip install -r requirements.txt

**2. Configuration of the Database**
-----

- **Creating the Database:**

Create a database named 'noteapp':

    CREATE DATABASE noteapp;




    


- **Creating Tables:**

 Use the 'noteapp' database and create a table named 'users':

    USE noteapp;
    CREATE TABLE users (
        id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
        name TEXT,      
        email TEXT,
        username TEXT,
        password TEXT
    );

    

- Complete the installation of the MySQL database and define the necessary connection information in the 'config.py' file.

**3. Starting the Application**
-
- Navigate to the root directory of the project in the terminal and start the Flask server using the following command:

      flask run

- You can view the application by going to http://localhost:5000 in your browser.




# Technologies Used

- **Python**: The programming language behind the web application.

- **Flask**: A Python-based web framework used for the web application structure and database management.

- **Flask-MySQLdb**: An extension that enables the connection between Flask and MySQL database.

- **WTForms**: A library used to create and validate forms.

- **Passlib**: A library used for password hashing and authentication.


# Site Images

![Screenshot from 2023-07-13 16-07-15](https://github.com/PrarieComamile/Note-App/assets/101043132/e1b636b2-cb73-47e0-888e-9b785bd2f3f3)
![Screenshot from 2023-07-13 16-07-24](https://github.com/PrarieComamile/Note-App/assets/101043132/bdaca5f8-6065-449b-997e-5c94be44abd0)
![Screenshot from 2023-07-13 16-07-47](https://github.com/PrarieComamile/Note-App/assets/101043132/4eaf639c-c743-42f8-8c81-ac543ae2f9e0)


# Lisans 
  The section with the screenshots is referred to in the original text but isn't provided [here](https://github.com/PrarieComamile/Note-App/blob/main/LICENSE).



