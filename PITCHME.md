# Python

## Astilbe

1-very-basic

Satria H R Harsono

---

## Get your hand dirty

+++

Type following code on your favorite text editor and save as `hello.py`.

```python
import sys

def main():
    print('Hello there', sys.argv[1])

if __name__ == '__main__':
    main()
```

+++

```
hafizhme@machine:~$ cd Code/python-astilbe/
hafizhme@machine:~/Code/python-astilbe$ python hello.py Jay
Hello there Jay
hafizhme@machine:~/Code/python-astilbe$ 
```
@[1](Open terminal/command prompt and navigate to your project directory, where you save `hello.py` is)
@[2](Run your program and add your name behind)
@[3-4](What you get there huh?)

+++

Do you think that was too messy? Try this one . . .

```python
import sys

print('Hello there', sys.argv[1])
```

+++

. . . absolutely perform just the same I promise. Afterward, we will prefer this way for now.

+++

Maybe you will be using the previous type when you met modular programming. As I said, we will prefer this way for now.

---

## Variable
### &
## Data Type

+++

We will move on to Python Shell, Python Interactive Interpreter, Python Interpreter Console, or whatever you named it is.
```
hafizhme@machine:~/Code/python-astilbe$ python
Python 3.5.2 (default, Sep 14 2017, 22:51:06) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

@[1](Type `python` on your console, or `python3` if you install multiple python version on your machine. Because we will be using python3.\* now)
@[2](Make sure you got python 3.\* here)
@[3-4](Ok you can ignore this for now)
@[5](Here you are, ready to code)

+++

```
>>> my_var = 200
>>> print(my_var)
200
>>> my_var
200
>>> my_var = 'I forgot something'
>>> print(my_var)
I forgot something
>>> my_var
'I forgot something'
```
@[1](What you are doing now is assigning an integer value `200` to a variable named `my_var`)
@[2-3](Then I can print the value of `my_var` using `print()` method)
@[4-5](As long as you are in Python Shell, printing variable by calling the variable is just fine)
@[6](You can reuse your previous variable even these are having different data type)
@[7-8](And this is just fine)
@[9](Try this too?)
@[9-10](Oops. Now you know. `print()` will convert any value to string representation)

+++

Congratulations, you just experienced using **dynamically-typed** language.

+++

Dynamically-typed language is (for short) a language you **don't need to define type** of variable you are using.

+++

So, I can assign numerous different value to my variable?

---

## Still Data type

+++?code=src/still-data-type

@[1](This is number, but got comma on it, \(read: float type\).)
@[2-3](Investigate!)
@[4](Boolean data type)
@[5-6](Investigate!)
@[7](False)
@[8-9](Investigate!)
@[10](Here it is, a list with multiple value in multiple data type.)
@[11-12](Investigate!)
@[13-14](Remember you can do the same using `print`, in case you are not in Python Shell.)
@[15-16](Accessing first index of `my_list` that is **zero-based** index.)
@[17](You can change a value of your list.)
@[18-19](Try to investigate!)
@[20-21](Ahah! Try to figuring this one :p)
@[22-23](And this XD)
@[24](Please introduce, **dictionary**.)
@[25-29](Are tired coding in a line, try this one.)
@[30-31](Try to investigate!)
@[32-33](Access `'aliases'` index)
@[34-35](ooh, dive more)
@[36](Create new index and assign new value on to it)
@[37-38](Try to investigate!)
@[39-44](You can assign empty list or dictionary.)
@[39-44](But why??)
@[45](Please introduce, **tupple**.)
@[46-47](Just like list.)
@[48-49](Just like list.)
@[50-51](Just like list.)
@[52-53](Just like list.)
@[54-57](Opps)
@[54-57](Just like list huh?)
@[57](Hope you can figured something.)

---

Please help me to improve this slide [on github issues](https://github.com/hafizhme/python-astilbe/issues)

`github.com/hafizhme/python-astilbe`
