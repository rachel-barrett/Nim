To run this application, assuming you have python, pip and virtualenv installed, type the following commands into your bash terminal:

``` bash
$ git clone https://github.com/rachel-barrett/Nim
$ cd Nim
$ virtualenv sandbox # create sandbox
$ source sandbox/bin/activate # activate sandbox
$ pip install -r requirements.txt # install dependencies into sandbox
$ python Nim.py # run program (in sandbox environment)
$ deactivate; rm -r sandbox # cleanup
```
Once you have finished and want to remove the program from your system, you can simply remove the directory Nim.