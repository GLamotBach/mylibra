# base image  
FROM python:3.9   

# setup environment variables 
ENV PIP_DISABLE_PIP_VERSION_CHECK 1  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

# where your code lives  
WORKDIR /code 

# run this command to install all dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt  

# copy whole project to your docker home directory. 
COPY . .

