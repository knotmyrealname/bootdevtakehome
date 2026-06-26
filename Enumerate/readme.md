# Enumerate

What if you also need the index of the items in a list?

Python has a built-in function to allow you to do this called `enumerate`. `enumerate` takes in a list and returns the current `index` and the cooresponding `value`, using the following syntax:

```
list = ["a", "b", "c"]
for i, v in enumerate(list):
    print(f"{i}, {v}")

# prints:
# 0, a
# 1, b
# 2, c
```

Here, `i` and `v` refer to the `index` of the `value` and the `value` itself.

## Benefits

Now, you may be wondering: Can't I just do this with a traditional `for` loop?

```
list = ["a", "b", "c"]
for i in range(0, len(list)):
    print(f"{i}, {list[i]}")
```

You're absolutely correct! As in every programming language, there's often more than one way to do things. However, with each of these methods, there are key advantages and disadvantages that may lead you to choose one over the other.

The main reason you'll want to use `enumerate` over this method is because it's cleaner, more readable, and handles indexing for you. However, `enumerate` is not the be-all and end-all of for loops as it can get messy if you need to perform array indexing or access multiple list values at the same time. In these cases, the traditional `for` loop still reigns supreme.

A general rule of thumb is to use
- `for v in list:` when you only need the value
- `for i, v in enumerate(list):` when you need both the index and value
- `for i in range(0, len(list)):` when you need to index values in the list, when editing the list or accessing multiple values at the same time.

## Assignment

Fantasy Quest is adding a new party system to allow friends to play together. As part of this, we need to allow the player to see their current party. 

Complete the `show_party` function using enumerate. It takes a the current party (a list of strings) and prints all the member names.

Example:

```
party = ["a", "b", "c"]
show_party(party)
```

should print

```
Member 0: a
Member 1: b
Member 2: c
```