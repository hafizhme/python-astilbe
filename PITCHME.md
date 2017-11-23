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

[1](We just put a few updated on our `if.py` from previous.)
[5](Put `else:` on it without indentation.)
[6](Indent this line with a single tab.)
[3-4](Line 4 belongs to any `True` condition.)
[5-6](Line 6 belongs to any `False` condition.)

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

Please help me to improve this slide [on github issues](https://github.com/hafizhme/python-astilbe/issues)

`github.com/hafizhme/python-astilbe`
