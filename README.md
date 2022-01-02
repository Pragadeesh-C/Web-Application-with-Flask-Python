<h1>Web Application With Flask </h1>
 <h3>Explanation of the Project</h3>
 
 <p>This project is about a basic/simple Web Application created with Flask,Python.
  <br>A simple website discussed about Gaming which has a contact page which gets information from the user regarding any queries/questions.<br>
<p>There is an Admin Panel which is quite simple,which has a login system,if you are logged in you can view the querries raised by user and their details collected from the form.</p> 
<h5>Login Details of Admin Panel:</h5>
<p>Username:admin</p>
<p>Password:password</p>
<h2>Initialization of project environment</h2> 
<p>Create a project folder</p>

<h5>On macOS/Linux</h5>
<p>$ mkdir myproject<br>
$ cd myproject<br>
$ python3 -m venv venv<br>
</p>

<h5>On Windows</h5>
<p>> mkdir myproject<br>
> cd myproject<br>
> py -3 -m venv venv<br>
  </p>
  <br>
 <h4>Activate the environment</h4>
 <h5>On macOS/Linux</h5>
 <p>$ . venv/bin/activate</p>
 
 <h5>On Windows</h5>
 <p>venv\Scripts\activate</p>
 <br>
 <h4>Installing Flask</h4>
 <p>pip install Flask</p>
 <br>
 <h3>To run the Application</h3>
 <h5>On PowerShell</h5>
 <p>
   $env:FLASK_APP = "main.py"<br>
   env:FLASK_ENV = "development"<br>
   flask run<br>
 </p>
 <h5>On CMD</h5>
 <p>set FLASK_ENV=development<br>
    set FLASK_APP=main<br>
    flask run
  </p><br>
