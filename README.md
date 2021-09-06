<!--- STARTEXCLUDE --->
# Getting Started with Apache Cassandra™ and Python using DataStax Astra DB
*50 minutes, Intermediate, [Start Building](https://github.com/DataStax-Examples/getting-started-with-astra-python#prerequisites)*

This sample Python backend provides a REST API service that is used with the [Getting Started with Astra UI](https://github.com/DataStax-Examples/getting-started-with-astra-ui) to show a
simple example of how to connect to and query DataStax Astra DBs.
<!--- ENDEXCLUDE --->


![image](https://raw.githubusercontent.com/DataStax-Examples/sample-app-template/master/screenshots/astra-sample-app-default.png)


## Objectives
- How to connect to DataStax Astra DB using the secure connect bundle
- How to share a DataStax Driver Session throughout a Python application
- How to expose a basic REST API using the DataStax Driver
  
## How this works
This project is built in Python and uses Flask to expose a REST API backend for use with the [Getting Started with Astra UI](https://github.com/DataStax-Examples/getting-started-with-astra-ui).

This application is the middle man that receives requests from the UI web page and serves data from the underlying DataStax Astra DB.

## Get Started
To build and play with this app, follow the build instructions that are located here: [https://github.com/DataStax-Examples/getting-started-with-astra-python](https://github.com/DataStax-Examples/getting-started-with-astra-python#prerequisites)

<!--- STARTEXCLUDE --->
## Prerequisites
Let's do some initial setup by creating a serverless(!) database.

### DataStax Astra
1. Create a [DataStax Astra account](https://dtsx.io/38B5JGj) if you don't already have one:
![image](https://raw.githubusercontent.com/DataStax-Examples/sample-app-template/master/screenshots/astra-register-basic-auth.png)

2. On the home page. Locate the button **`Create Database`**
![image](https://raw.githubusercontent.com/DataStax-Examples/sample-app-template/master/screenshots/astra-dashboard.png)

3. Locate the **`Get Started`** button to continue
![image](https://raw.githubusercontent.com/DataStax-Examples/sample-app-template/master/screenshots/astra-select-plan.png)

4. Define a **database name**, **keyspace name** and select a database **region**, then click **create database**.
![image](https://raw.githubusercontent.com/DataStax-Examples/sample-app-template/master/screenshots/astra-create-db.png)

5. Your Astra DB will be ready when the status will change from *`Pending`* to **`Active`** 💥💥💥 
![image](https://raw.githubusercontent.com/DataStax-Examples/sample-app-template/master/screenshots/astra-db-active.png)

6. After your database is provisioned, we need to generate an Application Token for our App. Go to the `Settings` tab in the database home screen.
![image](https://raw.githubusercontent.com/DataStax-Examples/sample-app-template/master/screenshots/astra-db-settings.png)

1. Select `Admin User` for the role for this Sample App and then generate the token. Download the CSV so that we can use the credentials we need later.
![image](https://raw.githubusercontent.com/DataStax-Examples/sample-app-template/master/screenshots/astra-db-settings-token.png)

1. After you have your Application Token, head to the database connect screen and select the driver connection that we need. Go ahead and download the `Secure Bundle` for the driver.
![image](https://raw.githubusercontent.com/DataStax-Examples/sample-app-template/master/screenshots/astra-db-connect-bundle.png)

9. Make note of where to use the `Client Id` and `Client Secret` that is part of the Application Token that we generated earlier.
![image](https://raw.githubusercontent.com/DataStax-Examples/sample-app-template/master/screenshots/astra-db-connect-bundle-driver.png)

### Github
1. Click `Use this template` at the top of the [GitHub Repository](https://github.com/DataStax-Examples/getting-started-with-astra-python):
![image](https://raw.githubusercontent.com/DataStax-Examples/sample-app-template/master/screenshots/github-use-template.png)

2. Enter a repository name and click 'Create repository from template':
![image](https://raw.githubusercontent.com/DataStax-Examples/sample-app-template/master/screenshots/github-create-repository.png)

3. Clone the repository:
![image](https://raw.githubusercontent.com/DataStax-Examples/sample-app-template/master/screenshots/github-clone.png)

## 🚀 Getting Started Paths:
*Make sure you've completed the [prerequisites](#prerequisites) before starting this step*
  - [Running on your local machine](#running-on-your-local-machine)
  - [Running on Gitpod](#running-on-gitpod)
  - [Deploying to Vercel](#deploying-to-vercel)
  - [Deploying to Netlify](#deploying-to-netlify)

### Running on your local machine
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

<!--- ENDEXCLUDE --->
