MyLibra

Mylibra is a web platform for managing personal book collections and a social
platform for book lovers.

Motivation:
MyLibra is my personal project meant as way to challenge myself and to learn,
all while delivering a real solution to a real problem. It is a mean for book 
worms to share their love with others. Be it by lending books or sharing their
opinions on their favorite titles. It’s meant to be a solution for anyone who 
has a hard time keeping track of their books or want to find something 
interesting to read.

Build status:
The base functionality of the project is finished. Some additional features 
are planed to be added in time.

Features:
- User account creation.
- Adding books to personal collection.
- Editing books in personal collection.
- Search functionality.
- Public profiles. 
- Friend list.
- Book reviews.
- Book rating.
- Book lending manager.
- Viewing friend’s collections.

Planed features:

- Book Club.
- Unified notifications.
- Friends activity feed.
- Searching for books via ISBN API
- And more

Tech and frameworks:
Python
Django
HTML
PostgreSQL
Bootstrap 5

Installation:
Please note, in settings.py file some critical information is decoupled to a 
external file, not added to public repository for security reasons.

For local installation:Their are two options. 
Virtual Environment and Docker Containers. 

Option 1: Virtual Environment:

1.Create a virtual environment.
2.Deploy a new Django project.
3.Replace files with the files from the repository.
4.In settings.py: Edit  DATABASES in settings.py in accordance with your local DB.
  MyLibra is intended to work with PostgreSQL but SHOULD work with other SQL 
  databases.
6.Make migrations with database
7.Run a development server
8.MyLIbra will be available locally at “localhost:8000/” (by default)

Option 2: Docker Containers:

1.Must have Docker installed on your local machine.
1.Download mylibra container from DockerHub. 
  At: https://hub.docker.com/r/glamotbach/mylibra
3.Download docker-compose.yml file from repository
4.In console, go to the location of docker-compose.yml and run:
  $ docker-compose up -d --build
  It may need to download postgres DB, container image.
5.Migrate database using:
  $ docker-compose exec web python manage.py migrate
6.Create superuser using:
  $ docker-compose exec web python manage.py createsuperuser 
  And provide information with accordance to the given prompts.
7.Go to: http://127.0.0.1:8000/admin and log in using the credentials, given in 
  previous point.
8.In admin panel go to: PUBLIC_PROFILE > Add and create o profile for your admin 
  account. 
9.The app can be accessed at: http://127.0.0.1:8000/ 

WARNING ! This version of MyLibra is meant for demonstration purposes only ! 
It is not safe for deployment !

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
