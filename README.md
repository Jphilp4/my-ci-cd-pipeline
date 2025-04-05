# My CI/CD Pipeline Project 🚀  
*A Journey from Scratch*

## 🧠 Overview  
In this project, I set out to create a **CI/CD pipeline** for a simple Flask application. The goal was to gain hands-on experience with:

- Version control  
- Code quality  
- Testing  
- Deployment automation  

---

## 🛠️ Key Steps Taken  

### 📁 Repository Creation  
Created a GitHub repository named `my-ci-cd-pipeline` to manage the project and track changes over time.

### 💻 Local Setup  
Cloned the repository locally, which generated a folder for my project files and version control.

### 📊 Code Quality Integration  
Integrated **SonarQube** for early and ongoing code quality monitoring by setting up a configuration file.

### 🌐 Flask Application Development  
Developed a basic Flask app with routes like:

- `/` → “Hello, World!”  
- `/about` → About page content  

This served as the core of the project.

### ✅ Testing Setup  
Wrote unit tests using `pytest` to validate that each route returned the expected messages and status codes.

### ⚙️ GitHub Actions Integration  
Configured a **GitHub Actions** workflow to automatically run tests on every push, ensuring code quality with each change.

---

## 🧩 Challenges Faced & Overcome  

### 🔐 Permission Issues  
Faced file access problems when working locally. Solved this by granting **Full Disk Access** to the terminal app.

### 🧪 Testing Environment Setup  
Installed dependencies (Flask, pytest), and used a **Python virtual environment** to manage project packages cleanly.

### 📦 Import Errors  
Python initially couldn't find my app files. Fixed it by restructuring folders and validating all imports and file paths.

### 🔧 CI Workflow Failures  
GitHub Actions initially failed due to a bad workflow config. Fixed it by:

- Installing Python properly  
- Specifying the correct dependencies  
- Ensuring tests ran in the right context  

### 📃 Dependency Management  
Created and maintained a `requirements.txt` to keep dependencies consistent across environments.

---

## 🏁 Key Achievements  

- ✅ **Successful local test execution** after import issues were resolved.  
- ✅ **CI pipeline success** on GitHub – all tests ran and passed (green tick!).  

---

## 🤔 Reflections & Lessons Learned  

- Set up and used GitHub for proper version control  
- Integrated **SonarQube** for automated code analysis  
- Practiced **test-driven development** with Flask and pytest  
- Managed dependencies using `venv` and `requirements.txt`  
- Built and debugged CI pipelines using GitHub Actions  
- Gained confidence in Python project structure and automation  

---
