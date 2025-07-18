# Bookstore-CRUD-Django
This is a Django CRUD web application that allows you to manage books and authors.
The project provides simple functionalities like adding, editing, deleting, and displaying books and authors with their images.

This project was built as part of an ITI training. 

✨ Features
- 📄 Books Management
- List all books.
- Add, edit, and delete books.
- View book details.
- Assign an author to each book.
- Upload book images.
- 👤 Authors Management
- List all authors.
- Add, edit, and delete authors.
- View author details.
- Upload author images.
- 🖼️ Image upload for both books and authors.
- 🗄️ PostgreSQL database.
- ♻️ Auto file cleanup using django-cleanup.

🛠️ Tech Stack
- Python
- Django
- PostgreSQL
- Bootstrap (for basic styling)
- django-cleanup
- Django Templates

🚀 Project Structure
```bash
├── bookstore
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── books
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates
│   └── static
├── authors
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates
│   └── static
├── media
│   ├── books
│   └── authors
├── db.sqlite3
├── manage.py
└── README.md
```
⚙️ Setup & Installation
1. Clone the Repository
```bash
git clone https://github.com/YourUsername/django-bookstore-crud.git
cd django-bookstore-crud
```
2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Install Requirements
```bash
pip install django psycopg2 django-cleanup
```
4. Configure Database
- Make sure your PostgreSQL server is running, then update the following in settings.py:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'djangodb',
        'USER': 'postgres',
        'PASSWORD': 'password123',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
```
5. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
6. Run the Server
```bash
python manage.py runserver
```
7. Access the Application
- Visit: http://127.0.0.1:8000/index

✅ Notes
- No authentication system is implemented.
- The project is focused on CRUD operations and basic media management.
- All images are saved locally under the media directory.