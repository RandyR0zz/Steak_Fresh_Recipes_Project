# Steak Fresh Recipe Project

The project is a basic website was created by Django Framework and was developed for the end of courses at the IT-Academy. The functionality of the site is based on the logic of adding recipes of steaks by the user with the possibility of moderating recipes by the administrator.

Was implemented:
<ul type='square'>
  <li>functionality for creating/retrieving data from the Post entity using relation with Author</li>
  <li>some templates and css files for the decoration</li>
  <li>several model tests</li>
  <li>CI/CD pipeline by using GitHub Actions</li>
</ul>

The programming language used for the project: <code>python 3.10.5</code>.

---
<a name='return'></a>
## How to install?

<ul type='square'>
  <li><a href='#create'>Сreate and activate virtual local-environment</a></li>
  <li><a href='#clone'>Clone repository</a></li>
  <li><a href='#install'>Install packages from the requirements.txt file</a></li>
  <li><a href='#start'>Get started with the project</a></li>
</ul>

---
<a name='create'></a>
### Сreate and activate virtual local-environment

To create virtual local-enviroment use the command below:

**For macOS or Linux**:

<code>python -m venv name_of_venv</code>

*Note. If your system provides with Python 2 and you have installed Python 3, don't forget to use the ```python3``` command instead of ```python```.*

**For Windows**

<code>py -m venv name_of_venv</code>

To acivate virtual local-enviroment use the next command:

**For macOS or Linux**:

<code>source name_of_venv/bin/activate</code>

**For Windows**

<code>.\name_of_venv\Scripts\activate</code>

*Note. If you are using Windows you may get an error related to Execution Policies. To solve the problem open PowerShell as a Administrator and paste a command <code>Set-ExecutionPolicy RemoteSigned</code>. If you get a question type <code>A</code>.*

If you did everything right the name of the active virtual environment will appear in parentheses before the name of the current directory:

<code>(name_of_venv) your_local_directory</code>

*Note. To deacivate virtual local-enviroment use the command <code>deactivate</code>.* 

<a href='#return'>Return</a>

---
<a name='clone'></a>
### Clone repository

You can clone repostitory just a few steps:

1. Above the list of files, click Code
2. Copy the URL of the repository
3. Open Terminal
4. Change the current working directory to the location where the cloned directory should be
5. Type <code>git clone</code> and paste the <code>URL you copied earlier</code>

Example:
```bash
git clone https://github.com/your-username/your-repository
```

6. Press Enter to create a local clone.

*Note. For more details: https://docs.github.com/ru/repositories/creating-and-managing-repositories/cloning-a-repository?tool=webui*

<a href='#return'>Return</a>

---
<a name='install'></a>
### Install packages from the requirements.txt file

From the active virtual environment navigate to the directory of the cloned repository and type:

**For macOS, Linux, Windows**

<code>pip install -r requirements.txt</code>

<a href='#return'>Return</a>

---
<a name='start'></a>
### Get started with the project

For run some model tests use:

<code>python manage.py test</code>

For run server:

<code>python manage.py runserver</code>

*Note. Starting development server at http://127.0.0.1:8000/.*

<a href='#return'>Return</a>

---
