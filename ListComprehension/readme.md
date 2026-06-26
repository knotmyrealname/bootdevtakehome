# List Comprehension

What if you want to create a new list based on the values in an existing list (for example, having the new list be double the value of the original)?

Your first thought may have been to create a new list and iterate over the existing list, like this:
 
```
list = [1, 2, 3]

new_list = []
for x in list:
    new_list.append(x * 2)
# new_list should have [2, 4, 6]
```

Although this is valid, Python has a more *concise* and *efficient* expression to implement this: [<u>List Comprehensions</u>](https://docs.python.org/3.10/tutorial/datastructures.html#list-comprehensions). 

With List Comprehension, you can do the perform the initialization and `for` loop in the same step, as follows:

```
list = [1, 2, 3]

new_list = [x * 2 for x in list]
# new_list should have [2, 4, 6]
```

You may be able to notice how the syntax is very similar, with list comprehension basically rearranging the `for` loop, using
- `[]` from `new_list = []`
- `x * 2` from `new_list.append(x * 2)`
- and `for x in list` from `for x in list:`

## Assignment

An intern has added a new function to create a minion for a summoner in Fantasy Quest using a `for` loop. **Update their code** to use the more concise **List Comprehension** expression.

```
def create_minion(summoner_stats):
    minion_stats = []
    for stat in summoner_stats:
        minion_stats.append(stat * 0.5)
    return minion_stats
```

## Tip

You can try rearranging the for loop as shown above:
- start with `minion_stats = []`
- add the `          ` expression from `minion_stats.append(stat * 0.5)` inside the brackets
- add the `                          `expression from `for stat in summoner_stats:` inside the brackets