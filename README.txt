MyLibra

Mylibra is a web platform for managing personal book collections.

Motivation:
MyLibra is my personal project meant as way to challenge myself and to learn,
all while delivering a real solution to a real problem. It is a mean for book 
worms to share their love with others. Be it by lending books or sharing their
opinions on their favorite titles. It’s meant to be a solution for anyone who 
has a hard time keeping track of their books or want to find something 
interesting to read.

Build status:
This project is in development stage. It will gain additional 
functionality over time as well as a more pleasant and user-friendly UI.  
For now it provides most of the intended basic functionality. It allows 
users to create their accounts, adding and editing books in their 
collections, find books already existing in the database, customize 
their profiles, add friends, mark books and read, rate and review read 
books,  In future, MyLibra will be expanded with additional functionality,
according to road map, leading to it’s intended shape. 

Features:
- User account creation.
- Adding books to personal collection.
- Editing books in personal collection.
- Search functionality.
- Public profiles 
- Friend list
- Book reviews

Planed features:
- Book lending manager
- Viewing friend’s collections
- Searching for books via ISBN API
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
Please note, in settings.py file some critical information is decoupled to a 
external file, not added to public repository for security reasons.

For local installation:

1.Create a virtual environment.
2.Deploy a new Django project.
3.Replace files with the files from the repository.
4.In settings.py: Fill out the information that was decoupled. That is:

  SECRET_KEY
  DEBUG
  DB_NAME
  DB_USER
  DB_PASSWORD
  DB_HOST
  DB_PORT

  This can be done by directly assigning values to the variables in settings.py 
  or by adding a “.env” file in settings.py directory, with the information in 
  question.   

  Edit  DATABASES in settings.py in accordance with your local DB. MyLibra is 
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
