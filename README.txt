_-Capstone-_
________________
| Readme KEY    |
| Category 🟡   |
| Subcategory⚫ |
| Instructions🔴|
|_______________|

🟡Distinctiveness and Complexity

    ⚫What is it?
        My task manager web application. Its purpose is to
        provide a user with the ability to create, edit, delete and view
        tasks for a given set of days (eg. Monday through to Sunday).

        There is also added functionality to plan more so than a
        week. With a month view available, users can select 
        between different months to create tasks in advance.

    ⚫What's the difference between this and a calendar or to-do list?
        I have tried to differentiate my task manager from a 
        traditional calender application such that my application
        focuses on day-to-day tasks and organisation rather than a 
        traditional calendar application which focuses more on the over 
        arching month and year. Although, a monthly mode is available for 
        users who need to plan that far ahead.

        I also differentiate my task manager from a to-do list. Most
        to-do list applications focus on an overarching task. My 
        application subsequently is an amalgamation of these two 
        types of organisational tools and creates a to-do list per day.

        My application focuses on day-to-day life, I can provide
        a more streamlined interface. I have personally felt that most
        of the calendar applications on the market have too many options.
        I prefer a more minimalist design, it's less to think about,
        focuses more on tasks, and reminds me of things I have to
        throughout the day.

        Thus these core values of minimalism, and ease of use transfer to
        my task application. Easy to create, delete and edit tasks makes
        this a tool for anyone, for any day.
        
    ⚫How does this differ from previous CS50 projects?
        The task application I have developed differs in several ways
        compared to the previous project in both complexity and
        functionality. My application implements a Django framework for
        front-end asynchronous functionality called Django-Unicorn. Which
        uses a class base system with its own Django tags, to avoid the
        need to write over encumbered ajax requests to Django.
        This front end makes the application far more different in logic
        alone to vary it from previous projects. While implementing 
        everything I have learned throughout the course, none of the 
        general topics of, social media; encyclopedias; eCommerce, are
        similar to my task application.
        
    ⚫Why did I build the application like this?
        A list of the complexities:
        o-> Django
        o-> Javascript, Jquery
        o-> Django-Unicorn
        o-> Django-Webpush
        o-> POSTGRESQL
        -Why Django?
            Django is a requirement for the CS50 course and this 
            projects backend.
        -Why Javascript, Jquery?
            Javascript is a requirement for the CS50 course. I subsequently
            chose a library, Jquery, to minimize and optimize the code I 
            write. Plus Jquery comes with extremely useful functions that 
            make Ajax requests more pleasing to write.
        -Why and what is Django-Unicorn?
            Even with Jqeury's built-in Ajax function, it's a hassle to have to 
            write my HTML in either a separate file directly in Javascript.
            This makes troubleshooting obscenely difficult and tedious.
            Not to mention the inability to embed Django Template language
            into the HTML.
            This is where Django-Unicorn comes in. It is a front-end framework
            for Django, which communicates with the backend without the need for me
            to write delirious lines of Ajax requests.
            It also comes with a 'component' tool, that allows it to talk with
            and control Django Templates. This means that I can include external
            Django templates within the Unicorn Component. It also means I can 
            write my HTML as HTML and not have to pass it to the DOM as a string
            injection. It has a listener for events to the DOM and automatically
            sends Ajax requests to the backend.
            It also provides additional security with a checksum value, and a few
            more operations, such as polling, and partial loading. I do not 
            incorporate these into my application as it does not need them, but 
            Django-Unicorn is so awesome I could help but talk about it.
        -Why and what is Django-Webpush
            Django-Webpush is a push notification plugin for Django. It provides
            a way for the Django server to send notifications to users who opt-in
            to the messaging. It is required for my application to notify you 
            of tasks you have queued. It, however, does not work on mobile, given
            the time constraint I have decided not to include this feature on mobile
            devices. It only works on desktop browsers.
        -Why PostgreSQL
            For my application, I wanted to implement an industry-level database 
            management system. I did not know exactly what my database structure
            would look like when starting the project, and SQLite3 does not allow
            for an array model. PostgreSQL does support Array fields for my database.
    ⚫Summary
        Given all of the points listed above, my task application is different from all
        of the previous projects.

🟡 What's in the box?

    ⚫Primary / 'Capstone' Directory
        In the primary directory, you will find a few new files and folders excluding 
        the git files and the default Django files such as the views.py or settings.py.
        New Folders -> media; theme;
        The media directory is a storage location for user profile images.
        The theme directory includes the base template design for my application, 
        as well as all the styling information generated by Tailwind
    
    ⚫'Main' Directory
        You will notice 3 new .py files, utilities; threads; 
        forms;
        The forms.py file has user registration and login, this is done for security
        purposes as Django provides automatic form validation when forms are built like
        this.
        The threads.py file contains a threaded function to call a query search every 
        minute to look for current tasks and notify users.
        The utility file contains the push notification function, this function is 
        called from the threads.py file.
    
    ⚫'Main/components'
        There are 2 files here. showtasksweekly; showtasksmonthly; 
        It is necessary to have 2 files as the weekly and monthly views on my application
        work differently. These 2 files are controlled by Django-Unicorn and therefore 
        follow the Django-Unicorn class functions to update the DOM elements.

    ⚫'Main/templates/unicorn'
        The templates here have Django-Unicorn components. The components interact with 
        Django and the files within the main components folder with Ajax requests that
        are handled by the Django-Unicorn API.

    ⚫'Main/templates/main'
        Templates contained within this folder provide a view of the URL pattern map.
        They incorporate the Django-Unicorn component template to render them.
    

🔴Install instructions
    I will do my best to have a one-stop shop instruction list, however, it may not
    be enough or may become outdated.
    
    ⚫Setting Up Git
        Depending on the operating system, setting up Git will vary.
        
        A link to the Git page setup:
        https://git-scm.com/downloads
    
    ⚫Cloning the repository
        To clone a repository, you will have to create and log in to your 
        GitHub account. As of writing this GitHub requires you to create an 
        authorisation token.
        
        A link to authorisation token creation:
        https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token

    ⚫Intalling Python
        Depending on the operating system, your installation will vary. On window
        machines that run windows 10 or above, you can download python from the
        windows store. For my application, I am using 3.11.1
        
        A link to the Python download page:
        https://www.python.org/downloads/
    
    ⚫Setting Up a Python Environment
        You're welcome to skip this step and install all of the packages globally,
        I would recommend that you set up the virtual environment.
        Python comes with VENV installed.
        Running this command will create a virtual environment:
            $python3 -m venv /path/to/new/virtual/environment
        
        After the installation, start the environment. This depends on the installation. This
        is a general location. 
        Windows:
            $yourinstall\Scripts\activate
        
        Linux and macOS:
            $source yourinstall\bin\activate

        To know that it worked, the name of the install folder for VENV will be at
        the beginning of the terminal line.

        All of the python dependencies will be installed on the virtual environment

        A link to the virtual environment python page:
        https://docs.python.org/3/library/venv.html
    
    ⚫Install POSTGRES:
        To install PostgreSQL you have to follow the following 
        guides

        Download Link for PostgreSQL:
        https://www.postgresql.org/download/

        Connecting to PostgreSQL on windows
        https://linuxhint.com/connect-to-postgresql-database-command-line-windows/

        Once connected to the PostgreSQL database, run these commands:

        postgres=# CREATE DATABASE calendarapp;
        postgres=# CREATE USER calendarappuser WITH PASSWORD 'password';
        postgres=# ALTER ROLE calendarappuser SET client_encoding TO 'utf8';
        postgres=# ALTER ROLE calendarappuser SET client_encoding TO 'utf8';
        postgres=# ALTER ROLE calendarappuser SET default_transaction_isolation TO 'read committed';
        postgres=# ALTER ROLE calendarappuser SET timezone TO 'UTC';
        postgres=# GRANT ALL PRIVILEGES ON DATABASE calendarapp TO calendarappuser;
        postgres=# \q

        Django PostgreSQL install:
        https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-20-04
    
    ⚫Installing all the dependencies
        ⚫Intalling from requirements.text:
            Windows:
                $py -m pip install -r requirements.txt
            
            Linux and macOS:
                $python -m pip install -r requirements.txt

        OR MANUALY
        ⚫Django installation, run this command:
            Windows:
                $py -m pip install Django

            Linux and macOS:
                $python -m pip install Django

            A link to the Django installation guide:
            https://docs.djangoproject.com/en/4.1/topics/install/

        ⚫Tailwind installation, run this command:
            $python -m pip install django-tailwind

            A link to the Tailwind installation guide:
            https://django-tailwind.readthedocs.io/en/latest/installation.html

        ⚫Psycopg2 installation, run this command:
            $pip install psycopg2-binary

            A link to psycopg2:
            https://pypi.org/project/psycopg2/

        ⚫Webpush installation, run this command:
            $pip install django-webpush

            A link to Django-Webpush:
            https://github.com/safwanrahman/django-webpush
        
        ⚫Six installations, run this command:
            $pip install six:

            A link to six:
            https://pypi.org/project/six/
            
        ⚫Django-Unicorn installation, run this command:
            $pip install Django-unicorn

            A link to Django-Unicorn:
            https://www.django-unicorn.com/docs/installation/

        ⚫Schedule installation, run this command:
            $pip install schedule

            A link to the schedule:
            https://pypi.org/project/schedule/

        ⚫Schedule installation, run this command:
            $pip install pillow

            A link to the pillow:
            https://pypi.org/project/Pillow/

    ⚫Running Everything
        You have made it this far, let's run it now!
        Migrate commands:
        Windows:
            $py manage.py makemigrations
            $py manage.py migrate

        Linux and MacOS:
            $python manage.py makemigrations
            $python manage.py migrate

        To run the project, run:
        Windows:
            $py manage.py runserver

        Linux and MacOS:
            $python manage.py runserver

        And... we are in. If everything went according to the plan your Django server
        should be up and running.

🟡Attributions
    Huge shout out to everyone who works on these projects. My application
    would have taken a lot longer and probably not work as well as it does
    without these.❤️
    
    Jquery Clock plugin provided by:
        https://github.com/loebi-ch/jquery-clock-timepicker
    
    Date calendar provided by:
        https://jqueryui.com/ 
    
    Django-Unicorn:
    https://github.com/adamghill/django-unicorn
    
    Django-Webpush:
    https://github.com/safwanrahman/django-webpush