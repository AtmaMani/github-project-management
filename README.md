# GitHub Project Management
This repo is a set of Python script tools to manage your GitHub repositories
and projects. Here you will find tools such as one to get the list of all
issues closed, generate a table and export that into a csv. You can later
use this to build your 'issues addressed' list to go with your projects releases.

I will add more scripts over time as the need arises.

## Dependencies
  - Python 3x
  - [github3.py](https://github.com/sigmavirus24/github3.py)
  - pip

## Installation
I highly recommend using this in either virtualenv or a conda env. Below
are the steps if you have set up ana`conda` or mini`conda` on your machine:

```PYTHON
# Create a new environment
conda create --name python-github-mgt ipython
activate python-github-mgt
pip install github3.py

# cd to your code dir
cd /lib/user/code/
git clone https://github.com/AtmaMani/github-project-management.git
```

## Usage
```PYTHON
# Activate your conda env or virtual env
activate python-github-mgt

# cd to your code dir
cd /lib/user/code/github-project-management

# call the python script from command line and follow the instructions
python list_closed_issues.py
```
