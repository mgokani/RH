# RH - practice doctest, unittest, tox and pep8

## Requirements
* python2.7
* python3.5
* python3.6
* python3.7
* python3.8
* pycodestyle
* tox
* numpy

## Execution
```
$ python print_pairs.py
[[0 0]
[0 0]]
```

## Run doctest
```
$ python print_pairs.py -v
Trying:
pairs([4, 1, 3, 5, 2, 6, 8, 7], 8)
Expecting:
array([[1, 7],
[2, 6],
[3, 5]])
ok
1 items had no tests:
__main__.pairs
1 items passed all tests:
1 tests in __main__
1 tests in 2 items.
1 passed and 0 failed.
Test passed.
[[0 0]
[0 0]]
```

## Run Unit tests
```
$ python test_printpairs.py -v
test_exception (__main__.TestPairs)
Test if exception is raised when no pairs are found ... ok
test_negativenumbers (__main__.TestPairs)
Test a combination of positive and negative numbers ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
```

## Run doctest, unittest, pycodestyle on different python env using tox
```
$ tox
py27 installed: DEPRECATION: Python 2.7 will reach the end of its life on January 1st, 2020. Please upgrade your Python as Python 2.7 won't be maintained after that date. A future version of pip will drop support for Python 2.7.,numpy==1.16.4,pycodestyle==2.5.0
py27 run-test-pre: PYTHONHASHSEED='2446546459'
py27 run-test: commands[0] | pycodestyle --verbose --statistics /root/Scratchbook/test/print_pairs.py
local configuration: in /root/Scratchbook/test
checking print_pairs.py
py27 run-test: commands[1] | pycodestyle --verbose --statistics /root/Scratchbook/test/test_printpairs.py
local configuration: in /root/Scratchbook/test
checking test_printpairs.py
py27 run-test: commands[2] | /root/Scratchbook/test/.tox/py27/bin/python /root/Scratchbook/test/print_pairs.py -v
Trying:
    pairs([4, 1, 3, 5, 2, 6, 8, 7], 8)
Expecting:
    array([[1, 7],
           [2, 6],
           [3, 5]])
ok
1 items had no tests:
    __main__.pairs
1 items passed all tests:
   1 tests in __main__
1 tests in 2 items.
1 passed and 0 failed.
Test passed.
[[0 0]
 [0 0]]
py27 run-test: commands[3] | /root/Scratchbook/test/.tox/py27/bin/python /root/Scratchbook/test/test_printpairs.py -v
test_exception (__main__.TestPairs)
Test if exception is raised when no pairs are found ... ok
test_negativenumbers (__main__.TestPairs)
Test a combination of positive and negative numbers ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
py35 installed: numpy==1.16.4,pycodestyle==2.5.0
py35 run-test-pre: PYTHONHASHSEED='2446546459'
py35 run-test: commands[0] | pycodestyle --verbose --statistics /root/Scratchbook/test/print_pairs.py
local configuration: in /root/Scratchbook/test
checking print_pairs.py
py35 run-test: commands[1] | pycodestyle --verbose --statistics /root/Scratchbook/test/test_printpairs.py
local configuration: in /root/Scratchbook/test
checking test_printpairs.py
py35 run-test: commands[2] | /root/Scratchbook/test/.tox/py35/bin/python /root/Scratchbook/test/print_pairs.py -v
Trying:
    pairs([4, 1, 3, 5, 2, 6, 8, 7], 8)
Expecting:
    array([[1, 7],
           [2, 6],
           [3, 5]])
ok
1 items had no tests:
    __main__.pairs
1 items passed all tests:
   1 tests in __main__
1 tests in 2 items.
1 passed and 0 failed.
Test passed.
[[0 0]
 [0 0]]
py35 run-test: commands[3] | /root/Scratchbook/test/.tox/py35/bin/python /root/Scratchbook/test/test_printpairs.py -v
test_exception (__main__.TestPairs)
Test if exception is raised when no pairs are found ... ok
test_negativenumbers (__main__.TestPairs)
Test a combination of positive and negative numbers ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
py36 create: /root/Scratchbook/test/.tox/py36
ERROR: InterpreterNotFound: python3.6
py37 create: /root/Scratchbook/test/.tox/py37
ERROR: InterpreterNotFound: python3.7
py38 create: /root/Scratchbook/test/.tox/py38
ERROR: InterpreterNotFound: python3.8
__________________________________________________________________________________________ summary __________________________________________________________________________________________
  py27: commands succeeded
  py35: commands succeeded
ERROR:  py36: InterpreterNotFound: python3.6
ERROR:  py37: InterpreterNotFound: python3.7
ERROR:  py38: InterpreterNotFound: python3.8
```
Note: My system does not have python 3.6, python3.7 and python3.8 installed and hence there are InterpreterNotFound errors in tox output
