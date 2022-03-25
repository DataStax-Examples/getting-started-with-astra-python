<!--- STARTEXCLUDE --->
# Getting Started with Apache Cassandra™ and Python using DataStax Astra DB
*50 minutes, Intermediate, [Start Building](https://github.com/DataStax-Examples/getting-started-with-astra-python#prerequisites)*

This sample Python backend provides a REST API service that is used with the [Getting Started with Astra UI](https://github.com/DataStax-Examples/getting-started-with-astra-ui) to show a
simple example of how to connect to and query DataStax Astra DBs.
<!--- ENDEXCLUDE --->

![image](https://raw.githubusercontent.com/DataStax-Examples/sample-app-template/master/screenshots/astra-sample-app-default.png)

## Astra DB Quick Start
<!--- STARTEXCLUDE --->
* [Signup for DataStax Astra](https://dtsx.io/38B5JGj), or login to your already existing account. 
* [Create an Astra DB Database](https://github.com/DataStax-Examples/sample-app-template/blob/master/GETTING_STARTED.md#create-an-astra-db) if you don't already have one.
<!--- ENDEXCLUDE --->
* [Create an Astra DB Keyspace](https://github.com/DataStax-Examples/sample-app-template/blob/master/GETTING_STARTED.md#create-an-astra-db-keyspace) called `sag_netflix` in your database.
* [Generate an Application Token](https://github.com/DataStax-Examples/sample-app-template/blob/master/GETTING_STARTED.md#create-an-application-token) with the role of `Database Administrator` for the Organization that your Astra DB is in.

## Running on your local machine
If you are familiar with Python, then you've likely gotten your hands on Python virtual environments.
We'll be leveraging pyenv while setting up this backend, which will serve our
Spacecraft frontend that will have you flying through the stars.

If you aren't familiar with Python, hop over to our [official documentation](https://helpdocs.datastax.com/aws/dscloud/astra/dscloudPythonDriver.html#Installingpyenv,Python,andvirtualenv)
for setting that up on your machine, and come back here after you have it installed ( specifically after Step 5 of the Procedure ).

Now that we have that out of the way, we'll use pyenv to install Python 3.6.9
```sh
pyenv install 3.6.9
```

Next create a new virtualenv using that Python version we just installed.
```sh
pyenv virtualenv 3.6.9 astra-venv
```

Almost off to the races, go ahead and activate that virtualenv
```sh
pyenv activate astra-venv
```

Woot, now 3 quick dependencies ( Flask, Flask CORS,  and the DataStax Cassandra Driver )
```sh
pip install Flask flask-cors cassandra-driver
```

Last one, clone this repo
```sh
git clone https://github.com/DataStax-Examples
/getting-started-with-astra-python.git
```

If everything above went smoothly, fingers crossed, then we are ready to rock.
Go to the directory that you just cloned this repo into
```sh
cd getting-started-with-astra-python
```

Fire up the engines
```sh
FLASK_ENV=development FLASK_APP=getting_started_with_astra.py flask run
```

You should be met with the following output, note that it's running on `localhost` and port `5000`
```sh
 * Serving Flask app "getting_started_with_astra.py" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 204-527-831
```

Once the backend is running, you can start the [Getting Started with Astra UI](https://github.com/DataStax-Examples/getting-started-with-astra-ui) in order to use a web page that leverages this backend.
