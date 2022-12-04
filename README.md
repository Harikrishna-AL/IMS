
# IMS

An Inventory Management System(IMS) is the tool that provides user the ability to track Inventory of different infrastructures of an organisation.


## Installation

- Fork and clone the project,  and add a upstream remote to track main repo changes
 ```
        $ git clone git@github.com:{username}/IMS.git
        $ cd IMS
        $ git remote add upstream git@github.com:Harikrishna-AL/IMS.git
```

Create a python 3 virtualenv, and activate the environment.
```bash
        $ virtualenv venv
        $ source bin/activate
        
```

⛔️After installing new packages, update the requirements.txt file⛔️
```bash
        $ pip freeze > requirements.txt
```

Install the project dependencies from `requirements.txt`
```
        $ pip install -r requirements.txt
```

## Setup

* `python manage.py makemigrations` to commit the database version
* `python manage.py migrate --run-syncdb` - set up database
* `python manage.py createsuperuser` - create admin user
* `python manage.py runserver`  - run the project locally

## Development

- For creating new features, create new branch locally and work on it.
- After testing the feature, create a PR.
- To fetch new changes

```bash
    $ git fetch upstream
    $ git rebase upstream/master
```

## Formatting

- Use `black` for formatting the code.
- `black` is already installed in the project dependencies.
- To format the code, run `black .` in the project root directory.



