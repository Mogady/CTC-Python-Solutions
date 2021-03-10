# This is what i learned about Python while trying to approach the optimal solution

- how does python "in" operator works and what its BigO
    - [complexity of in operator in python](https://stackoverflow.com/questions/13884177/complexity-of-in-operator-in-python)
    - [how is the in operator implemented](https://stackoverflow.com/questions/53542860/in-python-how-is-the-in-operator-implemented-to-work-does-it-use-the-next-me)
- Python sorted() uses Timsort algorthim which is O(N*LogN)
    - [sorted time complexity](https://stackoverflow.com/a/14434514)
    - [TimeSort Algorthim](https://en.wikipedia.org/wiki/Timsort)
- String slicing is O(N^2) since it is simply copying
    - [Time complexity of string slice](https://stackoverflow.com/a/35181399)
- .join() O(N) is faster than += O(N^2) for strings
    - [Why is ''.join() faster than += in Python?](https://stackoverflow.com/questions/39312099/why-is-join-faster-than-in-python)
    - [Time complexity of += and .join()](https://stackoverflow.com/questions/34008010/is-the-time-complexity-of-iterative-string-append-actually-on2-or-on)
- set.difference() is O(N) and i guess set(A)^set(B) is O(N^2)
    - [run time of the set difference](https://stackoverflow.com/questions/48044353/what-is-the-run-time-of-the-set-difference-function-in-python)
- collections.deque() is better for stacks if we don't care about the internal indexing as it is a double linked lists, but list might be better if the stack size will be small and we intend to access other elemetns inside the stack
    - [how to implment stacks in python](https://realpython.com/how-to-implement-python-stack/#using-collectionsdeque-to-create-a-python-stack)