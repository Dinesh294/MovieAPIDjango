<h1>Movie REST API built using Django, Django REST Framework, psycopg2</h1>

<h2>About: </h2>
   <ul>
   <li>Can do CURD operations on the movie data</li>
   <li>Implemented Token based authentication to call the api endpoint</li>
    <li>Get all the movie data (/api)</li>
    <li>Get single movie data (/api/id)</li>
    <li>Post movie data (/api)</li>
    <li>Put movie data (/api/id)</li>
    <li>Patch movie data (/api/id)</li>
    <li>Delete movie data (/api/id)</li>
   </ul> 

<h2>Screenshot:</h2>


<h3> GET TOKEN API</h3>

![getauthtoken](https://github.com/Dinesh294/MovieAPIDjango/assets/84972612/748a2512-03cd-40ce-a5e1-656a0ea3219e)


<h3> GET API</h3>

![allapi](https://github.com/Dinesh294/MovieAPIDjango/assets/84972612/6476f2b0-dac1-413b-a5ab-82dfc4137b12)


<h2>Steps:</h2>
    <ul>
    <li>clone the project and install the requirements <br>
        &emsp; python -m pip install -r requirements.txt </li>
    <li>Install Postgresql and configure postgres in settings.py</li>
        &emsp; python -m pip install psycopg2
    <li>do the migrations to migate the models <br>
        &emsp; python manage.py makemigrations <br>
        &emsp; python manage.py migrate </li>
    <li>to run the django server <br>
        &emsp; python manage.py runserver </li>
    <li>Create superuser</li>
    <li>get auth token from http://127.0.0.1::8000/get-token/id</li>    
    <li>provide auth token in header and access movie api in  http://127.0.0.1:8000/api </li>
    </ul>
