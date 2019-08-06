# CS 2.2 Graph challenges

## Table of contents for documentation
* [ALL DOCUMENTATION](docs.md)

## Challenge 4
### Part 1 - The knapsack problem

In my own words, you can state the knapsack problem as such:

Given a knapsack with a finite capacity and a list of items that have both weights and values,
find the best combination of items that maximize an objective (value, value / weight, etc).

To simplify, we're looking for the maximum value we can obtain from list of items while still
obeying the capacity of our bag.

### Applying Dynamic Programming to the problem
By using dynamic programming, we can make solving the knapsack problem magnitudes easier and
define a clear plan to how to do so.

### Step 1 - Identifying sub problems
Lets say we have a bag with 5 items. We want to find the best combination of all the items but
we have no idea how to start. What if instead of trying to look at all items at the same
time, how about we look at just 1?

We can then look at the problem as 4 + 1 items. What we have now done is isolate one item
from the rest of the items in the list, and are evaluating the cost of that *single* item plus
the cost of all the other items remaining. We can then even further this sub problem to:
```
what is the value of the 3 + 1 items and just the 3
what is the value of the 2 + 1 items and just the 2
what is the value of the 1 + 1 items and just the 1
what is the value of the 0 + 1 items and just the 0
```

And now what we have effectively done is reduce the problem to, "What is the cost of nothing and 
the current item we're looking at and the cost of nothing??"

### Step 2 - Guess the first choice
Luckily, we don't really need to guess the first problem since we've already stated in inside
of the identifying the sub problem that we can no longer reduce the problem beyond `0 + 1` items.
This is essentially just calculating the value of a single item plus nothing, which is just the
cost of the single item!

### Step 3 - Recursively define the value of an optimal solution

Let say that our knapsack function header is `Knap(c, items, n)` Where c is the capacity of our
bag, items is the list of items that we can choose from, and n is the current index we're on in
the list of items (The currently evaluated item).

The value of a single item can also be stated as `value = items[n].value` and the weight of a single
item is also state ad `weight = items[n].weight`

With this insight, we can define the recurisve value of the optimal solution as:

```python
value = items[n].value
weight = items[n].weight

return max(value + Knap(c - weight, items, n - 1), Knap(c, items, n - 1)))
```

### Step 4 - Compute the optimal solution
We can change the previously defined function header to include:
`Knap(c, items, n, memo)`

Where memo is a dictionary. Upon every call, we optimize our algorithm by checking if the value of the current
index has been computed before (indicating that we've already done the work of that sub problem)
and if so we use the computed value. If not, we caculate the value and then store the result in the `memo`,
dictionary for future recursive calls that may depend on that solution.


### Step 4 - Solve the original problem.

Step 3 solves the problem for us and the solution is in the last line:

```
return max(value + Knap(c - weight, items, n - 1), Knap(c, items, n - 1)))
```

For every recursive call, this returns the maximum value of one simple decision:
Did taking the current item yield a better value than not taking the current item?
If so, let's take it and it's value. If not, let's ignore this item and take the value without it.


