# automation-python
**Installing Pytest With APT**
```
$ sudo apt-get update
$ sudo apt search python3-pytest
```

**Run tests**
```
pytest
```

**Run tests in a directory**
```
pytest directory_name/
```

**Run tests by marker expressions**
```
pytest -m rozetka
```
Will run all tests which are decorated with the @pytest.mark.rozetka decorator.
See the pytest.ini file for information on all available marks.
