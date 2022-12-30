_-Capstone-_
________________
| Readme KEY    |
| Category 🟡   |
| Subcategory⚫ |
| Instruction 🔴|
|_______________|

🟡Distinctiveness and Complexity

    ⚫What is it?
        My task manager web application. Its purpose it to
        provide a user with ability to create, edit, delete and view
        tasks for a given set of days (eg. Monday through to Sunday).

        There is also added functionality to plan ahead more-so than a
        week. With a month view availble, users are able to select 
        between different months to create tasks in advance.

    ⚫What's the difference between this and a calender or to-do list?
        I have tried to differentiate my task manager from a 
        traditional calender application such that my application
        focuses on day to day tasks and orginisation rather than a 
        traditional calender application which focuses more on the over 
        arching month and year. Although, a month mode is availble for 
        users who need to plan that far ahead.

        I also differentiate my task manager from a to-do list. Most
        to-do list applications focus on an over arching task. My 
        application subsequintelly is an amalgamation of these two 
        type of orginisational tools and creates a to-do list per day.

        My application focuses on day to day life, I can provide
        a more streamlined interface. I have personally felt that most
        of the calender applications on the market have too many options.
        I prefer a more mininalist design, its less to think about,
        focusing more on tasks, and reminding me of things I have to
        throughout the day.

        Thus these core values of minimalist, and ease of use transfer to
        my task application. Easy to create, delete and edit tasks makes
        this a tool for anyone, for anyday.
        
    ⚫How does this differ from previous CS50 projects?
        The task application I have developed differs in several ways
        compared to the previous project in both complexity and
        functionality. My application implements a Django framework for
        front-end asynchoronus functionality called Django-Unicorn. Which
        uses a class base system with its own Django tags, to avoid the
        need to write over encombered ajax requests to Django.
        This front-end makes the application far more different in logic
        alone to vary it from previous projects. While implementing 
        everthing I have learned throughout the course, none of the 
        general topics of, social media; encyclopedias; eccommerce, are
        similair to my task application.
        
    ⚫Why did I build the application like this?
        A list of the complexitites:
        o-> Django
        o-> Javascript, Jquery
        o-> Django-Unicorn
        o-> Django-Webpush
        -Why Django?
            Django is a requirement for the CS50 course, and for this 
            projects backend.
        -Why Javascript, Jqeury?
            Javascript is a requirement for the CS50 course. I subsequintelly
            chose a library, Jqeury, to minimize and optimize the code I 
            write. Plus Jquery comes with extremely useful functions that 
            make Ajax request more pleasing to write.
        -Why and what is Django-Unicorn?
            Even with Jqeury's built in Ajax function its a hassel to have to 
            write my HTML in either a seperate file directly in Javascript.
            This makes troubleshooting obsenely difficult and tedious.
            Not to mention the inability to imbed Django Template language
            into the HTML.
            This is where Django-Unicorn comes in. It is a front-end framework
            for Django that comunnicates with backend without the need for me
            to write delarious lines of Ajax requests.
            It also comes with a 'component' tool, that allowes in to talk with
            and control Django Templates. This means that I can include external
            Django templates within the Unicorn Component. It also means I can 
            write my HTML as HTML and not have to pass it to the DOM as a string
            injection. It has a listener for events to the DOM and automatically
            sends Ajax requests to the backend.
            It also provides aditional security with a checksum value, and a few
            more operations, such as polling, and partial loading. I do not 
            incorporate these into my application as it does not need it, but 
            Django-Unicorn is so awesome I could help but talk about it.
        -Why and what is Django-Webpush
            Django-Webpush is a push notification plugin for Django. It provides
            a way for the Django server to send notifications to users who opt-in
            to the messaging. It is required for my application to notify you 
            on tasks you have queued. It however does not work on mobile, given
            the time contraint I have decided not to include this feature on mobile
            devices. It only works on desktop browsers.

🔴Install instructions
    I will do my best to have a one stop shop instruction list, however it may not
    be enough or may become outdated.
    
    ⚫Setting Up Git
        Depending on the operating system, setting up Git will vary.
        A link to Git page setup:
        https://git-scm.com/downloads
    
    ⚫Cloning the repository
        In order to clone a repository, you will have to create and login to your 
        GitHub account. As of writing this GitHub requires you to create an 
        authorisation token.
        A link to authorisation token creation:
        https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token

    ⚫Intalling Python
        Depending on the operating system, you're installation will vary. On window
        machines that run windows 10 or above, you can download python from the
        windows store. For my application I am using 3.11.1
        A link to the Python download page:
        https://www.python.org/downloads/
    
    ⚫Setting Up a Python Enviroment
        You're welcome to skip this step and install all of the packages globally,
        I would recommened that you setup the virtual enviroment.
        Python comes with VENV installed.
        Running this command will create a virtual enviroment:
        ```
        python3 -m venv /path/to/new/virtual/environment
        ```
        A link to virtual enviroment python page:
        https://docs.python.org/3/library/venv.html
    
    ⚫
    