# CodeWarsKataStuff
Just some CodeWars Solutions in Python.

A nice example:
```python
def solve(a): return sum(isinstance(x, int) and [1, -1][x % 2] for x in a)
```
or of course this is a nice one:
```python
for i in range(1, 101): print("Fizz"[(i%3)*4:] + "Buzz"[(i%5)*4:] or i)
```
