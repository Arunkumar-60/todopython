# Flask To-Do App Setup Guide

This guide walks through setting up a full-stack To-Do application using:

- **Python** – Backend programming language
- **Flask** – REST API
- **SQLite** – Database
- **HTML5** – Frontend structure
- **CSS3** – Styling
- **JavaScript (ES6)** – Frontend functionality
- **Git** – Version control
- **Visual Studio Code** – Development environment

---

# Technology Stack

| Technology | Purpose |
|------------|---------|
| Python 3 | Backend programming language |
| Flask | REST API |
| SQLite | Database |
| HTML5 | Frontend structure |
| CSS3 | Styling |
| JavaScript | Client-side functionality |
| Git | Version control |
| VS Code | IDE |

---

# 1. Install Python

Download Python from:

https://www.python.org/downloads/

During installation:

- ✅ Add Python to PATH
- Click **Install Now**

Verify the installation:

```bash
python --version
```

---

# 2. Install Git

Download Git:

https://git-scm.com/downloads

Verify installation:

```bash
git --version
```

Configure Git:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

---

# 3. Install Visual Studio Code

Download:

https://code.visualstudio.com/

### Recommended Extensions

- Python
- Pylance
- SQLite Viewer
- Live Server (optional)
- GitLens (optional)
- Prettier
- HTML CSS Support

---

# 4. Create the Project Folder

```text
flask-todo-app
```

Open the folder in VS Code.

---

# 5. Initialise Git

```bash
git init
```

---

# 6. Create a Python Virtual Environment

Windows:

```bash
python -m venv .venv
```

macOS/Linux:

```bash
python3 -m venv .venv
```

---

# 7. Activate the Virtual Environment

### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

### Windows Command Prompt

```cmd
.venv\Scripts\activate.bat
```

### macOS/Linux

```bash
source .venv/bin/activate
```

---

# 8. Upgrade pip

```bash
python -m pip install --upgrade pip
```

---

# 9. Install Python Packages

Install Flask:

```bash
pip install flask
```
Save dependencies:

```bash
pip freeze > requirements.txt
```

SQLite is included with Python and does not require a separate installation.

---

# 10. Project Structure

```text
flask-todo-app/
│
├── app/
│   ├── app.py
│   ├── routes.py
│   ├── database.py
│   ├── models.py
│   ├── schema.sql
│   └── __init__.py
│
├── database/
│   └── todo.db
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   └── js/
│       └── app.js
│
├── templates/
│   └── index.html
│
├── .venv/
├── requirements.txt
├── .gitignore
├── README.md
└── run.py
```

---

# 11. Flask Project Layout

Flask automatically serves:

- **HTML** from the `templates/` folder
- **CSS, JavaScript and images** from the `static/` folder

Example:

```
templates/
    index.html

static/
    css/
        style.css

    js/
        app.js
```

---

# 12. Create the Flask Application

Create:

```
app/app.py
```

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
```

---

# 13. Create the Frontend

## HTML

Create:

```
templates/index.html
```

This page will contain:

- Application title
- Task input
- Add Task button
- Task list
- Delete/Edit buttons

---

## CSS

Create:

```
static/css/style.css
```

Use CSS to style:

- Layout
- Buttons
- Forms
- Task cards
- Colours
- Responsive design

---

## JavaScript

Create:

```
static/js/app.js
```

JavaScript will:

- Send API requests using `fetch()`
- Display tasks
- Add tasks
- Delete tasks
- Update tasks
- Refresh the task list

---

# 14. SQLite Database

SQLite is built into Python.

Check the version:

```bash
python
```

```python
import sqlite3
print(sqlite3.sqlite_version)
```

Create a database:

```
database/todo.db
```

The database will be created automatically the first time your application connects to it.

---

# 15. Running the Application

Start Flask:

```bash
python app/app.py
```

or

```bash
flask run
```

Open your browser:

```
http://127.0.0.1:5000
```

---

# 16. REST API Endpoints

| Method | Endpoint | Purpose |
|---------|----------|---------|
| GET | `/tasks` | Retrieve all tasks |
| GET | `/tasks/<id>` | Retrieve a specific task |
| POST | `/tasks` | Create a task |
| PUT | `/tasks/<id>` | Update a task |
| DELETE | `/tasks/<id>` | Delete a task |

The frontend JavaScript will communicate with these endpoints using the Fetch API.

---

# 17. Git Ignore

Create a `.gitignore` file:

```gitignore
.venv/
__pycache__/
*.py[cod]
*.db
.env
.vscode/
.DS_Store
```

---

# 18. First Git Commit

```bash
git status
git add .
git commit -m "Initial Flask To-Do App setup"
```

---

# 19. Connect to GitHub

Create an empty GitHub repository.

Then:

```bash
git remote add origin https://github.com/<username>/flask-todo-app.git
git branch -M main
git push -u origin main
```

---

# 20. Useful Git Commands

Check status:

```bash
git status
```

Commit changes:

```bash
git add .
git commit -m "Describe your changes"
```

Push changes:

```bash
git push
```

Pull changes:

```bash
git pull
```

Create a branch:

```bash
git checkout -b feature/new-feature
```

---

# 21. Useful Python Commands

Run the application:

```bash
python app/app.py
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Update requirements:

```bash
pip freeze > requirements.txt
```

Deactivate the virtual environment:

```bash
deactivate
```

---

# 22. Frontend Features

The frontend should include:

- Task input field
- Add Task button
- Display all tasks
- Mark tasks as completed
- Edit tasks
- Delete tasks
- Responsive layout
- Loading and error messages

---

# 23. Backend Features

The Flask API should provide:

- SQLite database connection
- CRUD operations
- JSON responses
- Input validation
- Error handling
- RESTful API endpoints

---

# 24. Learning Outcomes

By completing this project, you will gain experience with:

- Python programming
- Flask web development
- Building REST APIs
- SQLite databases
- HTML page structure
- CSS styling
- JavaScript DOM manipulation
- Fetch API
- Client-server communication
- Git version control
- GitHub collaboration
- Full-stack web application development
