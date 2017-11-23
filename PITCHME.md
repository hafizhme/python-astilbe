# Python

## Astilbe

0-preliminary

Satria H R Harsono

---

## Why Python?

+++

> The day-to-day work of programming consists not of writing new programs, but mostly **reading and modifying** existing ones. [Eric S. Raymond](https://www.python.org/success-stories/esr/)

+++

> Many of these projects would not have been possible without the **rapid prototyping** that is characteristic for Python. [Konrad Hinsen](https://www.python.org/success-stories/mmtk/)

+++

> Python has dramatically improved development processes for the CORE project, and it has led to the **faster development times** and more rapid releases . . . [Nick Borko](https://www.python.org/success-stories/test-success-story/)

+++

> Python's unique mix of **simplicity** and power continues to be the best available choice for controlling ILM's complex and changing computing environment.[Tim Fortenberry](https://www.python.org/success-stories/industrial-light-magic-runs-python/)

+++

> A language that doesn’t afect **the way you think** about programming, is not worth knowing. [Alan Jay Perlis](http://www.cs.yale.edu/homes/perlis-alan/quotes.html)

---

## Brief History

+++

It is started to develop by Desember 1989 by [Guido van Rossum](https://gvanrossum.github.io/)

+++

Python grew throughout the early nineties, acquiring awesome tools.

+++

> What if Guido was hit by a bus? or if he dropped dead of exhaustion or if he is rubbed out by a member of a rival language following? [Python User at the moment](https://www.packtpub.com/books/content/brief-history-python)

+++

Open since `python 2.0` until present

+++

Top 5 Most Popular Programming Language in 2017. [Stack Overflow Developer Survey 2017](https://insights.stackoverflow.com/survey/2017#most-popular-technologies)

---

Enough b\*\*llsh\*\*!! Go to [Wikipedia](https://en.wikipedia.org/wiki/Python_(programming_language)) for more *chit-chat*

---

## The Language

+++

Python is a **dynamic**, **interpreted** (bytecode-compiled) language.

+++

There are **no type declarations** of variables, parameters, functions, or methods **in source code**.

+++

This makes the code short and flexible, and you lose the compile-time type checking of the source code.

+++

Python **tracks the types** of all values **at runtime** and flags code that does not make sense as it runs. 

+++

```
$ python
Python 2.7.9 (default, Dec 30 2014, 03:41:42) 
[GCC 4.1.2 20080704 (Red Hat 4.1.2-55)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> a = 6
>>> a
6
>>> a + 2
8
>>> a = 'hi'
>>> a
'hi'
>>> a + 2
Traceback (most recent call last):
  File "", line 1, in 
TypeError: cannot concatenate 'str' and 'int' objects
>>> ^D
```

@[1-4](Run the Python interpreter)
@[5](Set a variable in this interpreter session)
@[6-7](Entering an expression prints its value)
@[8-9](Another expression)
@[10]('a' can hold a string just as well)
@[11-12](It prints the assigned string)
@[13](Can you do that?)
@[14-16](Oops)
@[17](Close the interpreter)

Don't code, just look :)

---

## Make sure you have installed `python 3` on your machine

+++

### Installing Python 3 on [Mac OS X](http://docs.python-guide.org/en/latest/starting/install3/osx/#install3-osx)

+++

### Installing Python 3 on [Windows](http://docs.python-guide.org/en/latest/starting/install3/win/#install3-windows)

+++

### Installing Python 3 on [Linux](http://docs.python-guide.org/en/latest/starting/install3/linux/#install3-linux)

+++

Don't feel good with any tutorial? Go to official documentation then, [Official Documention](https://wiki.python.org/moin/BeginnersGuide/Download)

---

## There are many ways to run your python code

+++

### Interpret your code
Code in any of your favorite *text editor*, save as `<file_name>.py`, open in terminal/command prompt : `$ python3 path/to/your/file/<file_name>.py`

+++

### Using high rank Integrated Development Environment (IDE)
... for full set and easy development, like [PyCharm](https://www.jetbrains.com/Python_IDE)(?)

+++

### Code in interpreter
Open in terminal/command prompt : `$ python3`. Then type your code after you got similar to the following output
```
Python 3.5.2 (default, Sep 14 2017, 22:51:06) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

+++

### Or using Python IDLE
The one I never used before (and never will, maybe) [Python IDLE](https://docs.python.org/3/library/idle.html)

---

### What's next?

+++

If you think it is enough beeing here, you can go around and do your own exploration to some of these.

+++

These are my reference in building this slide.
- http://docs.python-guide.org/en/latest/ *
- https://developers.google.com/edu/python/ *
- https://docs.python.org/3/ *

+++

I did these a long time ago, these are my begining of my journey in python tho.
- https://www.codecademy.com/learn/learn-python **
- https://learnpythonthehardway.org/ **

+++

Yes it is rude, but going arround and peeking to some code is a good source of motivation.
- https://github.com/topics/python

---

Please help me to improve this slide [on github issues](https://github.com/hafizhme/python-astilbe/issues)

`github.com/hafizhme/python-astilbe`
