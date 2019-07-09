# Creating a New Python Django Web App

1. Create a new **Python Web Project** in Visual Studio 2019 from Files Menu
2. Use Search and Filter option to get to the option **Django Web Project**
3. Open the project folder location. Ex. <font color='red'>C:\Users\ac131128\source\repos\DjangoWebProject1</font>
4. Open CMD window in that project folder location and type: **pip install Django**
5. Go to Visual Studio Project Explorer and right click on the **Python Environments**
6. Click Add Environment
7. Right click on the project name and select Python -> Django Create SuperUser
8. Click on Run Project - Web Server (Chrome) and you should see <font color='red'> **http://localhost:<port_number>** </font> with a default webpage open up.

- The Python Environments directory contains all the necessary packages for your application to be deployed. You can add more packages and dependencies if needed.
(click on Manage Python Packages)
python manage.py runserver - to run python server

# Manage URLS

mysite/urls.py¶
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]


# Publishing an existing project to GitHub

1. Open Project Solution in Visual Studio.
2. Right click on project and select **Source Control**
3. Add github and enter your login credentials
4. A new repo will be created - local GIT repositories with a certain Name.
5. Double click on the repo name and select Sync
6. Add the URL of Git Repo created in GitHub ex. https://github.com/sadhudgp91/antragvs19.git
7. Click Publish to Github
8. Done!

