# Finally

Test automation framework for the Finally applications.

**Requirements**
Install the following dependencies in your local machine

Python 3 (https://www.python.org/)

Pipenv (https://pypi.org/project/pipenv/)

Chromedriver (https://chromedriver.chromium.org/)


**How to setup the project locally?**

git clone  https://github.com/Omarosking/Finally.git


**Go to the project directory**
  cd my-project



**Install dependencies**
  
  pipenv install
  
  

**Running Tests**

In order to run tests, you need to setup chromedriver in your PATH for your local machine.

All tests are run using pytest, to run tests, run the following command.

In order to run the tests in parallel locally, add the -n flag to the command below. For more info into the xdist library click here.

Tests are organized using Pytest custom markers, hence, an specific set of tests can be run based on the mark they have attached.

**pipenv run python -m pytest "path/to/file"**



