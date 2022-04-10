# Django Project Station
A Django application that allows a user to post a project he/she has created and get it reviewed by his/her peers. API endpoints are provided. Only logged in user can review or post a project

![landing](https://user-images.githubusercontent.com/53782607/162636021-a71daa26-d76d-4b2a-a2ce-f5263fe753a9.png)
![Landin2](https://user-images.githubusercontent.com/53782607/162636039-a00091e8-1406-4b49-8ac4-b7023a8ddc41.png)

![Api1](https://user-images.githubusercontent.com/53782607/162636072-ad00ef9e-854f-4b36-a882-2ee4f11681ea.png)


## Requirements
The user can perform the following functions:

- A user can view posted projects and their details
- A user can post a project to be rated/reviewed
- A user can rate/ review other users' projects
- A user can search for projects 
- A user can view projects overall score
- A user can view my profile page

## Installation / Setup instruction
The application requires the following installations to operate:
- pip
- gunicorn
- django
- postgresql

## Technologies Used
- python 3.9.6

## Project Setup Instructions
1) git clone the repository 
```
https://github.com/verowangari/DjangoAwwards.git
```
2. cd into DjangoAwwards-Clone
```
cd DjangoAwwards-Clone
```
3. create a virtual env
```
py -m venv env
```
4. activate env
```
env\scripts\activate
```
5. Open CMD & Install Dependancies
```
pip install -r requirements.txt
```
6. Make Migrations
```
py manage.py makemigrations
```
7. Migrate DB
```
py manage.py migrate
```
8. Run Application
```
py manage.py runserver
```

## Known Bugs
- There are no known bugs currently but pull requests are allowed incase you spot a bug

## Contact Information
If you have any question or contributions, please find me on [LinkedIn]www.linkedin.com/in/veronica-m-230470174

© 2022 Veronica Wangari

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
