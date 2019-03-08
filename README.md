#The easiest way to customize the project

## Python should be at least 3.6

1. Install last version of pipenv: ```pip install pipenv```

2. Create new env: ```pipenv --three```

3. If you use Pycharm, set path to the Project Interpreter on Settings -> Project -> Project Interpreter -> ..Add -> existing environment/..way for your Python.exe (C:/Users/{User}/.virtualenvs/{created_virtualenv}/Scripts/Python.exe) 

4. Next command will install all packages from Pipfile file (should be executed only once) ```pipenv install```

5. Add permission for sh file (for only Linux system): ```chmod +x run-e2e.sh```

6. Run tests ```./run-e2e.sh```