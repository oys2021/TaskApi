# 📝 TaskTrackr API

A simple Django REST API for user authentication and task management, featuring:

- User registration
- Authenticated user profile access
- Task creation, retrieval, and updating
- Task status listing
- Swagger/OpenAPI documentation

---

## 🚀 Technologies Used

- Python 3.13
- Django 5.2
- Django REST Framework
- drf-yasg (for Swagger UI)
- SQLite (default, can be changed)

---




## 🚀 Technologies Used

- Python 3.13
- Django 5.2
- Django REST Framework
- drf-yasg (for Swagger UI)
- SQLite (default, can be changed)

---

## 📦 Installation

1. **Clone the Repository**

```bash
git clone https://github.com/oys2021/TaskApi.git
cd TaskApi


2. **Create & Activate a Virtual Environment**

```bash
python -m venv venv
venv\Scripts\activate 

2. **Create & Activate a Virtual Environment**

```bash
python -m venv venv
venv\Scripts\activate 

3.**Install Dependencies**
pip install -r requirements.txt

4.**Apply Migrations**

python manage.py migrate


📘 Swagger Docs
Visit http://localhost:8000/docs/ for interactive Swagger documentation.

To enable Swagger, make sure you've installed and configured drf-yasg.

5. **Running Tests**
pytest