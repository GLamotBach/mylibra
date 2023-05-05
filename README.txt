MyLibra

Mylibra is a web platform for managing personal book collections.

Motivation:
MyLibra is my personal project meant as a means of learning, all while 
delivering a real solution to a real problem. 

Build status:
This project is in a very early stage of development. For now it provides 
the bear minimum to be considered functional. It allows users to create their
accounts, adding and editing books in their collections. In future, MyLibra 
will be expanded with additional functionality, according to road map, leading 
to it’s intended shape. 

Features:
- User account creation.
- Adding books to personal collection.
- Editing books in personal collection.

Planed features:
- Search functionality
- Public profiles 
- Book lending manager
- Friend list
- Viewing friend’s collections
- Searching for books via ISBN API
- Book reviews
- And more

Tech and frameworks:
Python
Django
HTML
PostgreSQL
Bootstrap 5

Installation:
MyLibra is meant to (and in time will) be deployed on a PaaS platform to gain 
it's online functionality. It can by deployed locally. 
Please note, settings.py file is NOT added to public repository for security 
reasons.
For local installation:
1.Create a virtual environment.
2.Deploy a new Django project.
3.Replace files with the files from the repository.
4.Add project apps and bootstrap 5 in your local settings.py, add:

INSTALLED_APPS = [
    # My apps
    'personal_collection',
    'public_profile',
    'users',
    # Other company apps
    'django_bootstrap5',

# Media settings

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")

5.Edit  DATABASES in settings.py in accordance with your local DB. MyLibra is 
  intended to work with PostgreSQL but SHOULD work with other SQL databases.
6.Make migrations with database
7.Run a development server
8.MyLIbra will be available locally at “localhost:8000/” (by default)

LICENSE:
MIT License

Copyright (c) 2023 GLamotBach

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
