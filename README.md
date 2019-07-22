root@stretchdev-test:~/Scratchbook/test# python print_pairs.py
[[0 0]
 [0 0]]
root@stretchdev-test:~/Scratchbook/test# python print_pairs.py -v
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
root@stretchdev-test:~/Scratchbook/test# python test_printpairs.py
..
----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
root@stretchdev-test:~/Scratchbook/test# tox
py27 installed: DEPRECATION: Python 2.7 will reach the end of its life on January 1st, 2020. Please upgrade your Python as Python 2.7 won't be maintained after that date. A future version of pip will drop support for Python 2.7.,numpy==1.16.4
py27 run-test-pre: PYTHONHASHSEED='4141867649'
py27 run-test: commands[0] | python /root/Scratchbook/test/print_pairs.py
[[0 0]
 [0 0]]
py27 run-test: commands[1] | python /root/Scratchbook/test/test_printpairs.py
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
py35 installed: numpy==1.16.4
py35 run-test-pre: PYTHONHASHSEED='4141867649'
py35 run-test: commands[0] | python /root/Scratchbook/test/print_pairs.py
[[0 0]
 [0 0]]
py35 run-test: commands[1] | python /root/Scratchbook/test/test_printpairs.py
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

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

