# CrazyPassword
A password validation game with ridiculous requirements, built with Django. 

The core code for matching the input password with regular expressions exists
at [/CrazyPasswordApp/validators.py](/CrazyPasswordApp/validators.py)

### Building a local version
- Clone the repository and change into the directory
```
git clone https://github.com/PROTechThor/CrazyPassword
cd CrazyPassword
```
- Create new virtual environment and activate
```
python3 -m venv env
source env/bin/activate
```
- Install Django
```
pip install django
```
- Finally, to run the app
```
python manage.py runserver
```
  The site should now be available at http://127.0.0.1:8000/
