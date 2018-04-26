# DJANGOCRUD
A REST api with interface

## Technologies used
* [Django](https://www.djangoproject.com/): The web framework for perfectionists with deadlines (Django builds better web apps with less code)

## Installation
* If you wish to run your own build, first ensure you have python3 globally installed in your computer. If not, you can get python [here](https://www.python.org").
* After doing this, confirm that you have installed virtualenv globally as well. If not, run this:
    ```bash
        $ pip install virtualenv
    ```
* Then, Git clone this repo to your PC
    ```bash
        $ git clone https://github.com/marcusbianchi/djangocrud.git
    ```

* #### Dependencies
    1. Cd into your the cloned repo as such:
        ```bash
            $ cd djangocrud
        ```
    2. Get docker-compose and run to start the database:
        ```bash
            $ docker-compose up -d
        ```
    3. Create and fire up your virtual environment:
        ```bash
            $ virtualenv  venv -p python3
            $ source venv/bin/activate
        ```
    4. Install the dependencies needed to run the app:
        ```bash
            $ pip install -r requirements.txt
        ```
    5. Make those migrations work
        ```bash
            $ python manage.py makemigrations
            $ python manage.py migrate
            $ python manage.py createsuperuser
        ```

* #### Run It
    
    Fire up the server using this one simple command:
    ```bash
        $ python manage.py runserver
    ```
    You can now access the file api service on your browser by using
    ```
        http://localhost:8000/admin/
    ```
    There you will be able to see and manage the people entity.

* #### Run It
    To get using RESTFormat:
     ```bash
        http://localhost:8000/admin/
    ```