# Getting Started with Apollo - Python backend

## Setup

If you are familiar with Python, then you've likely gotten your hands on Python virtual environments.
We'll be leveraging pyenv while setting up this backend, which will serve our
Spacecraft frontend that will have you flying through the stars.

If you aren't familiar with Python, hop over to our [official documentation](https://helpdocs.datastax.com/aws/dscloud/apollo/dscloudPythonDriver.html#Installingpyenv,Python,andvirtualenv)
for setting that up on your machine, and come back here after you have it installed ( specifically after Step 5 of the Procedure ).

Now that we have that out of the way, we'll use pyenv to install Python 3.6.9
```
pyenv install 3.6.9
```

Next create a new virtualenv using that Python version we just installed.

```
pyenv virtualenv 3.6.9 apollo-venv
```

Almost off to the races, go ahead and activate that virtualenv

```
pyenv activate apollo-venv
```

Woot, now 2 quick dependencies ( Flask and the DataStax Cassandra Driver )

```
pip install Flask https://datastax.artifactoryonline.com/datastax/datastax-public-releases-local/python-driver/cassandra-driver-3.19.0.20190927+dbaas.zip
```

Last one, clone this repo
```
git clone https://github.com/csplinter/getting-started-with-apollo-python.git
```

## Running

If everything above went smoothly, fingers crossed, then we are ready to rock.
Go to the directory that you just cloned this repo into
```
cd getting-started-with-apollo-python
```

Fire up the engines
```
FLASK_APP=getting_started_with_apollo.py flask run
```

You should be met with the following output
```
 * Serving Flask app "getting_started_with_apollo.py"
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
