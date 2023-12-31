# MyLibrary Project

-[MyLibrary site](https://mouline-lab.tech/mylibrary/)

-[See the projec Blog post](https://medium.com/@elmahdi.mouline/mylibrary-project-a-journey-in-code-26233a9ca015)

## Introduction

Welcome to MyLibrary, a student project for ALX SE program aimed at creating a web library for free books.

## Installation
To get started with MyLibrary on your local machine, follow these steps:

1. Clone the repository:
```bash
git clone https://github.com/moulineE/MyLibrary.git
```
2. Navigate to the project directory:
3. Install the project dependencies:
```bash
sudo apt intall mysql-server
sudo apt install python3-pip
sudo apt install python3-venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
4. set up the database:
set up the databese in the Backup folder by:
```bash
modifiy the create_database_and_user.sql file with your own credentials
cat create_database_and_user.sql | sudo mysql
sudo mysql < MyLibrary_dev_db.sql
```
5. Run the application:
```bash
python3-m flask run
```
## Usage

MyLibrary provides a user-friendly interface to explore and enjoy a vast collection of books. Here are some key functionalities:

    Search: Utilize the search bar to find your favorite books.
    Navigation: Seamlessly navigate through chapters and pages.
    Bookmarks: Bookmark your favorite pages for easy access.
