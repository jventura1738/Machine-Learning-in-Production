# zxpy

Shell scripts made simple 🐚

Inspired by Google's [zx](https://github.com/google/zx), but made much simpler and more accessible using Python.

## Rationale

Bash is cool, and it's extremely powerful when paired with linux coreutils and pipes. But apart from that, it's a whole another language to learn, and has a (comparatively) unintuitive syntax for things like conditionals and loops.

`zxpy` aims to supercharge bash by allowing you to write scripts in Python, but with native support for bash commands and pipes.

Let's use it to find all `TODO`s in one of my other projects, and format them into a table:

```python
#! /usr/bin/env zxpy
todo_comments = ~"git grep -n TODO"
for todo in todo_comments.splitlines():
    filename, lineno, code = todo.split(':', 2)
    *_, comment = code.partition('TODO')
    print(f"{filename:40} on line {lineno:4}: {comment.lstrip(': ')}")
```

Running this, we get:

```console
$ ./todo_check.py
README.md                                on line 154 : move this content somewhere more sensible.
instachat/lib/models/message.dart        on line 7   : rename to uuid
instachat/lib/models/update.dart         on line 13  : make int
instachat/lib/services/chat_service.dart on line 211 : error handling
server/api/api.go                        on line 94  : move these to /chat/@:address
server/api/user.go                       on line 80  : check for errors instead of relying on zero value
```

### A larger, practical example

You can find a comparison between a practical-ish script written in bash and
zxpy in [EXAMPLE.md](./EXAMPLE.md)

## Installation <a href="https://pypi.org/project/zxpy"><img src="https://img.shields.io/badge/pypi-zxpy-blue?style=flat"></a>

```console
pip install zxpy
```

## Basic Examples

Make a file `script.py` (The name and extension can be anything):

```python
#! /usr/bin/env zxpy
~'echo Hello world!'

file_count = ~'ls -1 | wc -l'
print("file count is:", file_count)
```

And then run it:

```bash
$ chmod +x ./script.py

$ ./script.py
Hello world!
file count is: 3
```

> Run `>>> help('zx')` in Python REPL to find out more ways to use zxpy.

A slightly more involved example: [run_all_tests.py](./examples/run_all_tests.py)

```python
#! /usr/bin/env zxpy
test_files = (~"find -name '*_test\.py'").splitlines()

for filename in test_files:
    try:
        print(f'Running {filename:.<50}', end='')
        output = ~f'python {filename}'  # variables in your shell commands :D
        assert output == ''
        print('Test passed!')
    except:
        print(f'Test failed.')
```

Output:

```bash
$ ./run_all_tests.py
Running ./tests/python_version_test.py....................Test failed.
Running ./tests/platform_test.py..........................Test passed!
Running ./tests/imports_test.py...........................Test passed!
```

More examples are in [EXAMPLE.md](./EXAMPLE.md), and in the [examples folder](./examples).

## `stderr` and return codes

To get `stderr` and return code information out of the shell command, there is an
alternative way of invoking the shell.

To use it, just use **3 variables** on the
left side of your `~'...'` shell string:

```python
stdout, stderr, return_code = ~'echo hi'
print(stdout)       # hi
print(return_code)  # 0
```

More examples are in the [examples folder](./examples).

## Interactive mode

```pycon
$ zxpy
zxpy shell
Python 3.8.5 (default, Jan 27 2021, 15:41:15)
[GCC 9.3.0]

>>> ~"ls | grep '\.py'"
__main__.py
setup.py
zx.py
>>>
```

> Also works with `path/to/python -m zx`

It can also be used to start a zxpy session in an already running REPL.
Simply do:

```pycon
>>> import zx; zx.install()
```

and zxpy should be enabled in the existing session.

## Development/Testing

To install from source, clone the repo, and do the following:

```bash
$ source ./venv/bin/activate  # Always use a virtualenv!
$ pip install -r requirements-dev.txt
Processing ./zxpy
[...]
Successfully installed zxpy-1.X.X
$ pytest ./tests  # runs tests
```
