# Python

## Astilbe

4-list-tupple-dictionary

Satria H R Harsono

---

Make sure you understand  thefollowing preliminary materials before continuing this session

+++

```
>>> my_list = list(range(5))
>>> my_list = [str(x) for x in range(20)]
>>> another_list = [2,5,1,3,9,6]
>>> my_list = [x for x in another_list if x % 2 == 0]
>>> str_list, int_list = [str(x) for x in range(20)], [x for x in range(20)]
>>> my_list = list(range(10))
>>> a, *b, c = my_list
>>> my_matrix = [
...     [0,1,2,3],
...     [0,1,2,3],
...     [4,1,2,4],
... ]
>>> my_matrix = [[x for x in range(5)] for x in range(5)]
>>> 
>>> matrix = [
...     [i*10+j for j in range(2,11,2)]
...     for i in range(0,10)
... ]
>>> [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
```

@[1](An easy way to create list consisting 0,1,2,3,4)
@[2](Using a for to make a list)
@[2](and make a casting before storing in to the list)
@[3-4](Using a condition before storing in to the new list)
@[5](Awesome huh?)
@[6-7](Hey, you have to try this XD. Find out what is inside `a`, `b`, `c`!)
@[8-12](What is this?)
@[8-12](You can do this too.)
@[14](Create a `10 x 5` matrix consisting all positive even number less or equal then 100 in a single assignment. And without direct assignment.)
@[15-18]()
@[19]
@[20]

---

## Method in String

+++

There are so much methods.
`https://docs.python.org/3/library/string.html`

+++

```
>>> sentence = "sneaky little hobbitses wicked tricksy false"
>>> sentence.capitalize()
'Sneaky little hobbitses wicked tricksy false'
>>> sentence.split(' ')
['sneaky', 'little', 'hobbitses', 'wicked', 'tricksy', 'false']
>>> words = sentence.split(' ')
>>> '-'.join(words)
'sneaky, little, hobbitses, wicked, tricksy, false'
>>> '-'.join(words) + '.'
'sneaky, little, hobbitses, wicked, tricksy, false.'
>>> ('-'.join(words) + '.').capitalize()
'Sneaky, little, hobbitses, wicked, tricksy, false.'
```

@[1]
@[2]
@[3]
@[4]
@[5]
@[6]
@[7]
@[8]
@[9]
@[10]
@[11]
@[12]

+++

----

## Method in List

+++

`https://docs.python.org/3/tutorial/datastructures.html`

+++

```
>>> fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
>>> fruits.count('apple')
2
>>> fruits.count('tangerine')
0
>>> fruits.index('banana')
3
>>> fruits.index('banana', 4)  # Find next banana starting a position 4
6
>>> fruits.reverse()
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
>>> fruits.append('grape')
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
>>> fruits.sort()
>>> fruits
['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
>>> fruits.pop()
'pear'
>>> foods = ['rice', 'tomato', 'meat']
>>> foods.extends(fruits)
>>> foods[len(foods):] = fruits
>>> foods
['rice', 'tomato', 'meat', 'apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange']
>>> del fruits
>> fruits
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'fruits' is not defined
>>> stocks = foods
>>> stocks[0] = "potato"
>>> stocks
['potato', 'tomato', 'meat', 'apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange']
>>> foods
['potato', 'tomato', 'meat', 'apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange']
>>> stocks = foods.copy()
>>> foods[0] = 'rice'
>>> foods
['rice', 'tomato', 'meat', 'apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange']
>>> stocks
['potato', 'tomato', 'meat', 'apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange']
>>> foods.sort()
>>> foods
['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'meat', 'orange', 'rice', 'tomato']
>>> set(foods)
{'banana', 'rice', 'kiwi', 'apple', 'tomato', 'grape', 'orange', 'meat'}
```

@[1]
@[2]
@[3]
@[4]
@[5]
@[6]
@[7]
@[8]
@[9]
@[10]
@[11]
@[12]
@[13]
@[14]
@[15]
@[16]
@[17]
@[18]
@[19]
@[20]
@[21]
@[22]
@[23]
@[24]
@[25]
@[26]
@[27]
@[28]
@[29]
@[30]
@[31]
@[32]
@[33]
@[34]
@[35]
@[36]
@[37]
@[38]
@[39]
@[40]
@[41]
@[42]
@[43]
@[44]
@[45]
@[46]
@[47]

---

## Sets

The forgotten one

+++

```
>>> basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
>>> print(basket)                      # show that duplicates have been removed
{'orange', 'banana', 'pear', 'apple'}
>>> 'orange' in basket                 # fast membership testing
True
>>> 'crabgrass' in basket
False
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a                                  # unique letters in a
{'a', 'r', 'b', 'c', 'd'}
>>> a - b                              # letters in a but not in b
{'r', 'd', 'b'}
>>> a | b                              # letters in a or b or both
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
>>> a & b                              # letters in both a and b
{'a', 'c'}
>>> a ^ b                              # letters in a or b but not both
{'r', 'd', 'b', 'm', 'z', 'l'}
```

@[1]
@[2]
@[3]
@[4]
@[5]
@[6]
@[7]
@[8]
@[9]
@[10]
@[11]
@[12]
@[13]
@[14]
@[15]
@[16]
@[17]
@[18]
@[19]

---

## Zip

+++

```
>>> a = [x for x in range(0,5)]
>>> b = [x for x in range(5,10)]
>>> c = [x for x in range(10,15)]
>>> d = zip(a,b,c)
>>> d
<zip object at 0x7fed15e1a8c8>
```

@[1]
@[2]
@[3]
@[4]
@[5]
@[6]

---

## Tupple

+++

```
>>> t = 12345, 54321, 'hello!'
>>> t[0]
12345
>>> t
(12345, 54321, 'hello!')
>>> # Tuples may be nested:
... u = t, (1, 2, 3, 4, 5)
>>> u
((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
>>> # Tuples are immutable:
... t[0] = 88888
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> # but they can contain mutable objects:
... v = ([1, 2, 3], [3, 2, 1])
>>> v
([1, 2, 3], [3, 2, 1])
```

@[1]
@[2]
@[3]
@[4]
@[5]
@[6]
@[7]
@[8]
@[9]
@[10]
@[11]
@[12]
@[13]
@[14]
@[15]
@[16]
@[17]
@[18]

---

## Dictionary

+++

```
>>> tel = {'jack': 4098, 'sape': 4139}
>>> tel['guido'] = 4127
>>> tel
{'sape': 4139, 'guido': 4127, 'jack': 4098}
>>> tel['jack']
4098
>>> del tel['sape']
>>> tel['irv'] = 4127
>>> tel
{'guido': 4127, 'irv': 4127, 'jack': 4098}
>>> list(tel.keys())
['irv', 'guido', 'jack']
>>> sorted(tel.keys())
['guido', 'irv', 'jack']
>>> 'guido' in tel
True
>>> 'jack' not in tel
False
>>> dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{'sape': 4139, 'jack': 4098, 'guido': 4127}
>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}
>>> dict(sape=4139, guido=4127, jack=4098)
{'sape': 4139, 'jack': 4098, 'guido': 4127}
>>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
>>> for k, v in knights.items():
...     print(k, v)
...
gallahad the pure
robin the brave
```

@[1]
@[2]
@[3]
@[4]
@[5]
@[6]
@[7]
@[8]
@[9]
@[10]
@[11]
@[12]
@[13]
@[14]
@[15]
@[16]
@[17]
@[18]
@[19]
@[20]
@[21]
@[22]
@[23]
@[24]
@[25]
@[26]
@[27]
@[28]
@[29]
@[30]

---

Obligatory : `https://docs.python.org/3/tutorial/datastructures.html`
Additional : `http://book.pythontips.com/en/latest/map_filter.html`

---

Please help me to improve this slide [on github issues](https://github.com/hafizhme/python-astilbe/issues)

`github.com/hafizhme/python-astilbe`
