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

#### Applying Dynamic Programming to the problem
By using dynamic programming, we can make solving the knapsack problem magnitudes easier and
define a clear plan to how to do so.

#### Step 1 - Identifying sub problems
Lets say we have a bag with 5 items. We want to find the best combination of all the items but
we have no idea how to start. What if instead of trying to look at all items at the same
time, how about we look at just 1?

We can then look at the problem as 4 + 1 items. What we have now done is isolate one item
from the rest of the items in the list, and are evaluating the cost of that *single* item plus
the cost of all the other items remaining. We can then even further this sub problem to:
```
what is the value of the 3 + 1 items and then the value of the 3 items
what is the value of the 2 + 1 items and then the value of the 2 items
what is the value of the 1 + 1 items and just the value of the 1 items
what is the value of the 0 + 1 items and just the value of the 0 items
```

And now what we have effectively done is reduce the problem to, "What is the cost of nothing and 
the current item we're looking at and the cost of nothing??"

#### Step 2 - Guess the first choice
Luckily, we don't really need to guess the first problem we need to solve since we've already stated in inside
of the identifying the sub problem that we can no longer reduce the problem beyond `0 + 1` items.
This is essentially just calculating the value of a single item plus nothing, which is just the
cost of the single item!

#### Step 3 - Recursively define the value of an optimal solution

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

#### Step 4 - Compute the optimal solution
We can change the previously defined function header to include:
`Knap(c, items, n, memo)`

Where memo is a dictionary. Upon every call, we optimize our algorithm by checking if the value of the current
index has been computed before (indicating that we've already done the work of that sub problem)
and if so we use the computed value. If not, we caculate the value and then store the result in the `memo`,
dictionary for future recursive calls that may depend on that solution.


#### Step 5 - Solve the original problem.

Step 3 solves the problem for us and the solution is in the last line:

```
return max(value + Knap(c - weight, items, n - 1), Knap(c, items, n - 1)))
```

For every recursive call, this returns the maximum value of one simple decision:
Did taking the current item yield a better value than not taking the current item?
If so, let's take it and it's value. If not, let's ignore this item and take the value without it.

#### Resources used for Knapsack problem
* [MIT opencourseware: Optimization problems](https://www.youtube.com/watch?v=uK5yvoXnkSk)
* [CS Dojo: 0/1 Fractional knapsack problem](https://www.youtube.com/watch?v=xOlhR_2QCXY)
* [Geeks for Geeks 0-1 knapsack problem](https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/)



### Part 2 - The coin change problem

In my own words, the coin change problem can be explained as follows:

Given an integer `N = 10` and a infinite amount of coins from
a set of coin values `coins = {1,2,3}`, how many different combinations 
of coins can you make?

#### Step 1 - Identify the sub problems.

Let's create a very simple case where `N = 4` and we only have coins `coins = {1,2}`.
Given these coins, we can make these arrangements:

```
{1,1,1,1}
{1,1,2}
{2,2}
```

If you look at the arrangement of the solution, you should notice the arrangement of the coins and
that their order seems pretty peticular. This is because it is. The first combination is just 4 `1 value`
coins that could fit into the value `N`. This is actually the one of the smallest sub problems.
We can restate this specific sub problem as, how many `1 valued` coins can we fit into the value `N` or simply,
how many of the smallest coins can we fit into the value `N`? After we've determined that amount, we
can then ask, "How many of the smallest coins plus the next smallest coins can we fit into `N`"?

#### Step 2 - Guess the first choice
Using the knowledge we previously stated, the first choice i'd go with is how many times can we fit the smallest
valued coin into N if we can fit it at all? After solving this sub problem, we can then work our way back up towards
finding out the different combinations of all of the other coins.

#### Step 3 - Recursively define the solution
Let's define a function, `count_coins(value, coins, index)`. With this header, we can compute
the recursive solution with:

```python
count_coins(4, [1,2], 2) = count_coins(4, [1, 2], 1) + count_coins(2, [1, 2], 2)
```

In the solution above, we're counting the amount of different combinations we can have if 
we don't take the highest value coin and the value of if we do take the highest value coin and then
adding the solutions to those sub problems together.


#### Step 4 - compute the optimal solution
The optimal solution in this case would require the modification of the function header,
`count_coins` to look like this:

```python
count_coins(value, coins, index, memo)
```

With memo being a dictionary. The dictionary would store the index that it computes the value
to and then other sections of the tree would get access to it, allowing them to not have to recompute
the solutions to the subproblems over again.

#### Step 5 - Solve the original problem
Step 3 solves the problem 
