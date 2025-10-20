# GestorDeTarefas 🐸

This is my simple task manager built with Django, allowing users to register, log in, and manage their tasks.

----------------------------------------

🐸 Features
- User registration and login system  
- Add, edit, and delete tasks  
- Task completion mark
- Protected routes (login required)
  
----------------------------------------

🐸 Technologies Used
- **Python 3**
- **Django 5**
- **HTML5, CSS3**
- **SQLite3 (default Django database)**

----------------------------------------

⚙️ Installation

1️⃣ Clone the repository

----------------------------------------

git clone https://github.com/yourusername/GestorDeTarefas.git
cd GestorDeTarefas

----------------------------------------

2️⃣ Create a virtual environment
python -m venv venv

source venv/bin/activate   # On macOS/Linux

venv\Scripts\activate      # On Windows

----------------------------------------

3️⃣ Install dependencies
pip install -r requirements.txt

----------------------------------------

4️⃣ Install on Vscode
* **Django:**
* **SQLite Viewer:**

----------------------------------------

5️⃣ Run migrations
python manage.py migrate

----------------------------------------

6️⃣ Start the server
python manage.py runserver

----------------------------------------

Then open your browser:
👉 http://127.0.0.1:8000/

----------------------------------------
🐸Project Structure🐸
 Gestor-de-tarefas/
│
├── manage.py
├── db.sqlite3
│
├── GestorDeTarefas/                
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py                 
│   ├── urls.py                    
│   └── wsgi.py
│
├── tarefas/                       
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py                   
│   ├── migrations/
│   │   └── __init__.py
│   ├── models.py                 
│   ├── tests.py
│   ├── urls.py                     
│   └── views.py                   
│
├── static/                       
│   ├── global.css
│   ├── index/
│   │   └── index.css
│   ├── home/
│   │   └── home.css
│   └── img/
│       └── logo.png                 
│
└── tarefas/templates/tarefas/      
    ├── index.html                
    ├── cadastro.html             
    ├── home.html                 
    ├── teste.html                 
    └── ...                         
