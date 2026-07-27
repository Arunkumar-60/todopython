# todopython

Code Network's Python To-Do app project.

A full-stack To-Do application built with Flask and SQLite on the backend, and plain HTML, CSS, and JavaScript on the frontend.

## Technology stack

| Technology | Purpose |
| ---------- | ------- |
| Python 3 | Backend programming language |
| Flask | REST API |
| SQLite | Database |
| HTML5 | Frontend structure |
| CSS3 | Styling |
| JavaScript (ES6) | Client-side functionality |

## Requirements

- [Python 3](https://www.python.org/downloads/) (tick "Add Python to PATH" during the Windows installer)
- [Git](https://git-scm.com/downloads)

SQLite ships with Python, so there is nothing extra to install for the database.

Verify both are available:

```bash
python --version
git --version
```

## Getting started

### 1. Clone the repository

```bash
git clone https://github.com/willisepic21/todopython.git
cd todopython
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv .venv
```

macOS/Linux:

```bash
python3 -m venv .venv
```

### 3. Activate it

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Windows Command Prompt:

```cmd
.venv\Scripts\activate.bat
```

macOS/Linux:

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Run the app

```bash
python app/app.py
```

Then open <http://127.0.0.1:5000> in your browser. The SQLite database is created automatically the first time the app connects to it.

To stop the server, press `Ctrl+C`. To leave the virtual environment, run `deactivate`.

## Project structure

```
todopython/
│
├── app/
│   ├── __init__.py
│   ├── app.py          # Flask entry point
│   ├── routes.py       # API routes
│   ├── database.py     # Database connection helpers
│   ├── models.py       # Data models
│   └── schema.sql      # Table definitions
│
├── database/
│   └── todo.db         # Created on first run (not committed)
│
├── static/
│   ├── css/style.css
│   └── js/app.js
│
├── templates/
│   └── index.html
│
├── requirements.txt
├── run.py
├── LICENSE
└── README.md
```

Flask serves HTML from `templates/` and CSS, JavaScript, and images from `static/`.

## API endpoints

| Method | Endpoint | Purpose |
| ------ | -------- | ------- |
| GET | `/tasks` | Retrieve all tasks |
| GET | `/tasks/<id>` | Retrieve a specific task |
| POST | `/tasks` | Create a task |
| PUT | `/tasks/<id>` | Update a task |
| DELETE | `/tasks/<id>` | Delete a task |

The frontend talks to these endpoints using the Fetch API.

## Contributing

```bash
git checkout -b feature/your-feature
git add .
git commit -m "Describe your changes"
git push -u origin feature/your-feature
```

Then open a pull request. If you add a package, update the dependency list:

```bash
pip freeze > requirements.txt
```

## Licence

Licensed under the GPL-3.0 licence. See [LICENSE](LICENSE) for details.
