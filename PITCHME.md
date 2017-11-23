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
@[20-21](Ahah! Try to figure this one :p)
@[22-23](And this XD)
@[24](Please introduce, **dictionary**.)
@[25-29](Are you tired coding in a line? Try this one.)
@[30-31](Investigate!)
@[32-33](Access `'aliases'` index)
@[34-35](ooh, dive more)
@[36](Create new index and assign new value on to it)
@[37-38](Investigate!)
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

## Type of ~~data type~~ object

+++

### Mutable 
@[](A mutable object is that you **can assign a new value** in a variable **without creating a new one**.)
@[](**List** and **dictionary** are mutable data type.)

+++?code=src/mutable

@[1](Recall our mutable object, `my_list`.)
@[2-3](Recall our mutable object, `my_list`.)
@[4-5](Print its address in hexadecimal.)
@[6](Make some changes on an element.)
@[7-8](Make some changes on an element.)
@[9-10](Tadaaa)
@[3-5,8-10](See the different?)
@[3-5,8-10](The element is changed.)
@[3-5,8-10](The address remain the same.)

+++

### Imutable 
@[](An imutable object is that you can assign a new value by **creating a new one**.)
@[](**Tupple**, **integer**, **float**, **boolean** and **string** are imutable data type.)

+++?code=src/imutable

@[1](Recall our imutable object, `my_var`.)
@[1](Here we will give the proof.)
@[2-3](Print its address in hexadecimal.)
@[4](Make some 'changes'.)
@[5-6](Tadaaa)
@[1-3,4-6](See the different?)
@[1,4](The element is changed.)
@[3,6](The address is changed too.)
@[3,6](This is an elementary proof that python creating a new object every **assignment**.)
@[7](How about our tupple?)
@[8-9](Print its address in hexadecimal.)
@[10-13](Make some 'changes' that goes wrong.)
@[7,14](Let's do a cheap trick.)
@[15-16](And yes, you got what you want.)
@[7-9,16-18](See the different?)
@[9,18](The address is changed.)
@[19,22](Assignment on a list element.)
@[19,22](It will show you that every assignment is creating a new object.)
@[19](Recall our mutable object, `my_list`)
@[20-21](Print its address in hexadecimal.)
@[22](Make some 'changes'.)
@[22](that is now, we know that is **assignment**)
@[23-24](Tadaaa)
@[21,24](The address is changed.)

---

Operator

+++

## Arithmetics

+++

Because this slide is not meant to be your reference,
please go to the [official documentation](https://docs.python.org/3/library/operator.html#mapping-operators-to-functions)

---

## Standard input
in Python 3

+++?code=src/input-python3

@[1](Save input to a variable.)
@[1](Take a look that we put a welcoming on it.)
@[2](This is our welcoming message.)
@[3](So, what's your name.)
@[3](In my case it is 'Gollum')
@[3](In my case it is 'Gollum')
@[3](Press `Enter` when you are done.)
@[4](Nothing?)
@[5-6](Print `my_var`.)
@[7](In case you are to shy to put a welcoming message,)
@[7](just let it be.)
@[8](Okay, we need to type something on it.)
@[8](Since the programmer is to shy to type a welcoming message.)
@[9](We will go with 'Gollum'.)
@[10-11](Print `my_var`.)
@[1-6](This is input that takes string.)
@[6](How to take input as an integer one?)
@[12-13](Create new one that probably will input as an integer.)
@[14](I am 17 yo.)
@[15-16](Print `my_var`)
@[15-16](It is string gentlemen.)
@[15-16](But this is not rigid!)
@[17](Use `type()` instead,)
@[17](a method to check varible's type)
@[17-18](Oh my god, I saw `'str'`, is that string!?)

+++

Enough for now :D

---

Please help me to improve this slide [on github issues](https://github.com/hafizhme/python-astilbe/issues)

`github.com/hafizhme/python-astilbe`
