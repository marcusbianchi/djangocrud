# DJANGOCRUD
A REST api with interface

## Technologies used
* [Django](https://www.djangoproject.com/): The web framework for perfectionists with deadlines (Django builds better web apps with less code)
* [Docker](https://www.docker.com/): Docker is an open platform for developers and sysadmins to build, ship, and run distributed applications, whether on laptops, data center VMs, or the cloud.
* [Python3](https://www.python.org/): Python 3.0 (a.k.a. "Python 3000" or "Py3k") is a new version of the language. The language is mostly the same, but many details, especially how built-in objects like dictionaries and strings work, have changed considerably, and a lot of deprecated features have finally been removed. Also, the standard library has been reorganized in a few prominent places.


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

* #### Test It
    
    Test using this one simple command:
    ```bash
        $ python manage.py test
    ```

* #### Run It
    
    Fire up the server using this one simple command:
    ```bash
        $ python manage.py runserver
    ```
    You can now access the file api service on your browser by using
    ```
        http://localhost:8000/
    ```
    There you will be able to see and manage the people entity.

    To get use ir RESTFormat:
     ```bash
        curl -H "Content-Type: application/javascript" http://localhost:8000/people/
    ```