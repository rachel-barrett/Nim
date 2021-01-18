To run this application, assuming you have python3 installed, type the following commands into your bash terminal:

``` bash
$ git clone https://github.com/rachel-barrett/nim-py
$ cd nim-py
$ python3 -m venv sandbox # create sandbox
$ source sandbox/bin/activate # activate sandbox
(sanbdox) $ python -m pip install -r requirements.txt # install dependencies into sandbox
(sandbox) $ python Nim.py # run program (in sandbox environment)
```
Once you have finished and want to remove the program from your system, you can simply remove the directory nim-py.