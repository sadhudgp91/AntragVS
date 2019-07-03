# Create a project environment Tutorial for Python - Django
In this section, you create a virtual environment in which Django is installed.

# macOS/Linux
sudo apt-get install python3-venv
python3 -m venv env

# Windows
> *  python -m venv env

In VS Code, open the Command Palette (View > Command Palette or (Ctrl+Shift+P)). Then select the Python: Select Interpreter command:

From the list, select the virtual environment in your project folder that starts with ./env or .\env:

Install Django in the virtual environment by running one of the following commands in the VS Code Terminal:

> * python -m pip install django

In the CMD window type: 
> * python manage.py runserver 127.0.0.1:7000

If you want to use a different port than the default 8000, specify the port number on the command line, such as 
> * python manage.py runserver 5000.

Ctrl+click the http://127.0.0.1:8000/ URL in the terminal output window to open your default browser to that address. If Django is installed correctly and the project is valid, you see the default landing page.

