# Python

## Astilbe

2-decision-making

Satria H R Harsono

---

## There are 4 type of decision making in python

---

### If

+++

Type these following code on your favorite text editor and save as `if.py`.

+++?code=src/if.py&lang=python

@[3,4](You have to make sure to indent correctly.)
@[3,4](You have to watch your indent here!!)
@[4](This belongs to `if`.)
@[6](We don't give an indentation on this line.)
@[6](Therefore, this line don't belongs to `if`.)
@[1](Save the prompted value to `your_name`.)
@[2]
@[3](Check wheather it is `True` or not.)
@[3](You can use any `boolean` data type return value instead.)
@[4](Execute this if given condition is True.)
@[5]
@[6](This line will be executed no matter what.)

+++

```
hafizhme@machine:~/Code/python-astilbe$ python3 if.py 
What is your name? Gollum
MY PRECIOUS!!!
We wants it, we needs it. Must have the precious. . . .
hafizhme@machine:~/Code/python-astilbe$ python3 if.py 
What is your name? Smeagol
We wants it, we needs it. Must have the precious. . . .
```

@[1-2](Try to type 'Gollum')
@[3-4](Make sure the output is similar to mine.)
@[3](Thise line printed because the condition is `True`.)
@[4](Thise line printed because whatever the condition is.)
@[5-6](Try to type 'Smeagol')
@[7](Make sure the output is similar to mine.)
@[6-7]('MY PRECIOUS!!!' is not printed because the condition is `False`.)

---

### If Else

+++

Type these following code on your favorite text editor and save as `ifelse.py`.

+++?code=src/ifelse.py&lang=python

@[1-6](We just put a few updated on our `if.py` from previous.)
@[5](Put `else:` on it without indentation.)
@[6](Indent this line with a single tab.)
@[3-4](Line 4 belongs to any `True` condition.)
@[5-6](Line 6 belongs to any `False` condition.)

+++

```
hafizhme@machine:~/Code/python-astilbe$ python3 ifelse.py
What is your name? Gollum
MY PRECIOUS!!!
hafizhme@machine:~/Code/python-astilbe$ 
hafizhme@machine:~/Code/python-astilbe$ python3 ifelse.py
What is your name? Smeagol
We wants it, we needs it. Must have the precious. They stole it from us. Sneaky little hobbitses. Wicked, tricksy, false!
hafizhme@machine:~/Code/python-astilbe$ 
```

@[1-2](Try to type 'Gollum')
@[3](Make sure the output is similar to mine.)
@[3](This line printed because the condition is `True`.)
@[1-4](And we won't see 'We wants it, we ne . . .' anywhere, since we use `if else`.)
@[5-6](Try to type 'Smeagol')
@[7](Make sure the output is similar to mine.)
@[7](This line printed because the condition is `False`.)
@[5-8](Likewise,we  won'tsee 'MY PRECIOUS!!!' anywhere, since we use 'if else.)

---

### Elif

+++

Type these following code on your favorite text editor and save as `elif.py`.

+++?code=src/elif.py&lang=python

@[1-6](Again we just put a few updated on our `ifelse.py` from previous.)
@[5](Replaced by `elif your_name == 'Smeagol':`.)
@[3-4](Line 4 belongs to any `True` condition for **first condtion**.)
@[5-6](Line 6 belongs to any `True` condition for **second condition**.)

+++?code=src/elif-run

@[1-2](Try to type 'Gollum')
@[3](Make sure the output is similar to mine.)
@[3](This line printed because the first condition is `True`.)
@[4-5](Try to type 'Smeagol')
@[6](Make sure the output is similar to mine.)
@[6](This line printed because the second condition is `True`.)
@[7-8](Try to type 'Frodo')
@[7-9](This case seems do not print any.)
@[7-9](No condition is `True`.)
@[7-9](You could give `else:` in the last line to make the remain condition catched.)

---

### Nested If

+++

You don't seem to be newbie, why don't give you a simple task? hmmm.

+++

Remember this old days when you are asked to create a **grading program** using `pascal`?

@[](You can finish this problem using `elif`, try to use `nested if` instead.)

+++

Range | Grade
---|---
`[90,100]` | A
`[80,90)` | AB
`[70,80)` | B
`[60,70)` | BC
`[50,60)` | C
`[40,50)` | CD
`[30,40)` | D
`[20,30)` | DE
`[0,20)` | E

---

@[](There are much more magic you don't know about decision making in Python.)
@[](This slide is not a slide instead intend to make you expert.)
@[](Expert learn by doing, by experiencing.)

---

Please help me to improve this slide [on github issues](https://github.com/hafizhme/python-astilbe/issues)

`github.com/hafizhme/python-astilbe`
