# Full Stack Web Developer Exercise 4: Item Catalog

## Objective
Create an application to demonstrate CRUD functionality and OAUTH support for Google + Login and authentication/authorization.

## Instructions

1. Be sure the required dependencies are installed by running the following in your terminal:

    * Install Flask: `pip install Flask`
    * Install Sqlalchemy: `pip install SQLAlchemy`

2. Clone this repository to a folder containing your Vagrant file: `git clone https://github.com/jazztbone2b/udacity_catalog_fullstack.git`

3. Open a terminal window and navigate to the folder containing this project

4. Run `vagrant up` then `vagrant ssh` to start the virtual machine and ssh into it

5. Navigate to the project directory in the virtual machine by running `cd /vagrant/`

6. Confirm the existence of all required files by typing `ls`

7. Type the following commands (in order) to create the database, populate the database, and run the application:

    * `python database_setup.py`
    * `python database_populate.py`
    * `python project.py`

8. Once the app is running, go to `http://localhost:5000` in your browser

9. Click `Login` button on Right side of Navigation Bar to login to application using Google credentials

10. Click `Logout` button on Right side of Navigation Bar to subsequently log out of application

## JSON API Endpoints

* http://localhost:5000/category/JSON
* http://localhost:5000/category/<category_id>/item/JSON
* http://localhost:5000/category/<category_id>/item/<item_id>/JSON
