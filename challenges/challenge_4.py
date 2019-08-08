"""
    Solving the knapsack and another dynamic programming problem
    of my choice.
"""
import timeit
import types


class Item:
    """
        Item to store meta information for items that
        are to be stored within the knapsack.
    """

    def __init__(self, name, weight, value):
        self.name = name
        self.value = value
        self.weight = weight

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other_item):
        return self.value == other_item.value

    def __lt__(self, other_item):
        return self.value < other_item.value

    def __gt__(self, other_item):
        return self.value < other_item.value

    def __str__(self):
        return f"< Item: {self.name:10}\tValue: {self.value:<3}\tWeight: {self.weight:>2} >"

    def __repr__(self):
        return str(self)


def simple_knapsack(
    capacity: int, items: [Item], cost_func: types.FunctionType, curr_index: int = None
):
    """
        Simple knapsack solution that naively approaches solving the knapsack problem. The algorithm
        solves the problem by breaking the problem into the smallest possible state where we have
        either no items or no more capacity left. It then builds up from that stat
        adding one or no items at a time, evaluating which decision has lead
        to a more optimal solution to the sub problem. It then builds up these subproblems
        to get an overall solution that has looked at every item in the bag.


        Args:
        * capacity - The capacity of the knapsack as an int.
        * items - A list of item objects for choosing from
        * cost_func - The cost function to determine the value of each items
        * curr_index [None] - The current index of the item we're looking at inside
        of the items.

        Returns:
        * A tuple that contains the total value of all the items based on the cost function
        and then the list of all items taken.
    """
    if curr_index is None:
        curr_index = len(items) - 1

    # If there is no more space left or we've traversed all the items, return
    # 0, as we can't go further
    if capacity == 0 or curr_index < 0:
        return 0, []

    curr_item: Item = items[curr_index]

    if curr_item.weight > capacity:
        return simple_knapsack(capacity, items, cost_func, curr_index - 1)

    # Get the item value and calculate the new capacity of our knapsack
    # after an item is added.
    item_value = cost_func(curr_item)
    new_capacity = capacity - curr_item.weight

    # Simulate taking the item
    value_with_item, items_with_curr = simple_knapsack(
        new_capacity, items, cost_func, curr_index - 1
    )

    total_value_with_item = value_with_item + item_value

    # Don't take the item, but take the value
    value_without_item, items_without_curr = simple_knapsack(
        capacity, items, cost_func, curr_index - 1
    )

    # If the value with the item is greater than the value without the
    # item, return the current total value and all the items
    if total_value_with_item > value_without_item:
        all_items = [curr_item]
        all_items.extend(items_with_curr)
        return total_value_with_item, all_items

    return value_without_item, items_without_curr


def memoized_knapsack(capacity, items, cost_func, curr_index=None, memo=None):
    """
        Memoized knapsack solution that will calculate the value of all combinations of items and
        then memorize the value of those combinations. The algorithm calculates the solution to
        the problem by breaking the problem into the smallest possible state where we have either no
        items or no more capacity left. It then builds up from that state adding one item or no
        items at a time, evaluating which decision has lead to a more optimal solution to the
        sub problem, and then storing the answers to those sub problems so they
        don't have to be calculated again.

        Args:
        * capacity - The capacity of the knapsack as an int.
        * items - A list of item objects for choosing from
        * cost_func - The cost function to determine the value of each items
        * curr_index [None] - The current index of the item we're looking at inside
        of the items.

        Returns:
        * A tuple that contains the total value of all the items based on the cost function
        and then the list of all items taken.
    """
    # If there is no more space left or we've traversed all the items, return
    # 0, as we can't go further

    if curr_index is None:
        curr_index = len(items) - 1
        memo = {}

    # If the capacity is 0 or the current index has gone past all of the items.
    if capacity == 0 or curr_index < 0:
        return 0, []

    curr_item: Item = items[curr_index]

    # If the item has a weight greater than the current capacity,
    # skip to the next item.
    if curr_item.weight > capacity:
        return memoized_knapsack(capacity, items, cost_func, curr_index - 1, memo)

    # Get the item value and calculate the new capacity of our knapsack
    # if the item were to be added to it.
    item_value = cost_func(curr_item)
    new_capacity = capacity - curr_item.weight

    # If the weight of the items from the current weight onwards
    # hasnt' been computed, compute it!
    if curr_index not in memo:
        value_with_item, items_with_curr = memoized_knapsack(
            new_capacity, items, cost_func, curr_index - 1, memo
        )

        total_value_with_item = value_with_item + item_value
        # Store the result of the current items
        memo[curr_index] = total_value_with_item, items_with_curr
    else:
        value_with_item, items_with_curr = memo[curr_index]

    total_value_with_item = value_with_item + item_value

    # If the weight of the next set of items not
    # including the current one hasn't been computed,
    # compute it!
    if curr_index - 1 not in memo:
        # Don't take the item, but take the value
        value_without_item, items_without_curr = memoized_knapsack(
            capacity, items, cost_func, curr_index - 1, memo
        )

        memo[curr_index - 1] = value_without_item, items_without_curr
    else:
        value_without_item, items_without_curr = memo[curr_index - 1]

    # If the value with the item is greater than the value without the
    # item, return the current total value and all the items
    if total_value_with_item > value_without_item:
        all_items = [curr_item]
        all_items.extend(items_with_curr)
        return total_value_with_item, all_items

    # The value without the item was greater, take it instead
    return value_without_item, items_without_curr


def count_coins(value, coins, index):
    """
        Count the amount of different ways you can make change with coins of value
        
    """
    if value == 0:
        print(index)
        return 1

    if value < 0:
        return 0

    if index < 0 and value >= 1:
        return 0

    value_with_coin = value - coins[index]
    return count_coins(value, coins, index - 1) + count_coins(
        value_with_coin, coins, index
    )


def memoized_count_coins(value, coins, index, memo):
    """
        A memoized coin counting algorithm. This algorithm relies on the memoizing the values
        of the coins 
    """
    # If the value is 0, we have found one way to fit the coins into the value
    if value == 0:
        return 1

    # If the index is less than or equal to the amount of coins,
    # there are no ways to fit this set of coins into the value.
    if index == len(coins):
        return 0

    key = f"{value}-{index}"

    # Check if the answer has already been computed
    if key in memo:
        return memo[key]

    current_sum = 0
    total_ways = 0

    # While the current sum is less than the value
    while current_sum <= value:
        # Math for keeping track of combos
        current_coin = coins[index]
        new_value = value - current_sum
        current_sum += current_coin

        # No need to recurse if the value is less than 0
        if new_value >= 0:
            num_ways = memoized_count_coins(new_value, coins, index + 1, memo)
            total_ways += num_ways

    # Memoize the answer
    memo[key] = total_ways

    return total_ways


def main():
    """
        Solve the knapsack problem and another DP programming challenge.
    """
    capacity = 20
    sorted_knapsack_items = sorted(knapsack_items)

    print("#### CHALLENGE 4 PART 1 ####")
    print(
        f"Solving the knapsack problem with a knapsack that has a capacity of {capacity}"
    )
    print("and these are the items we can choose from:")
    for item in sorted_knapsack_items:
        print(f"\t{item}")

    print("\nThe optimal solution to the problem is $2550 worth of goods")

    memo_score, memo_items = memoized_knapsack(
        capacity, sorted_knapsack_items, lambda item: item.value
    )

    print(
        f"\nThe memoized_knapsack function computed a bag with the score: ${memo_score}"
    )
    print("and took these items: ")
    for item in memo_items:
        print(f"\t{item}")

    coins = [1, 2, 3, 4]
    value = 4

    print("\n#### CHALLENGE 4 PART 2 ####")
    print(
        f"Solving the coin count problem where we have a value {value} and coins {coins}"
    )

    print(
        "\nThe optimal solution to the problem is 5, because there's 5 ways to fit those coins into 4"
    )

    num_of_ways = memoized_count_coins(value, coins, 0, {})

    print(
        f"\nThe memoized_count_coins computed {num_of_ways} ways to fit {coins} into {value}"
    )


knapsack_items = [
    Item("Macbook", 10, 1500),
    Item("TV", 20, 800),
    Item("IPhone", 5, 900),
    Item("Minecraft", 1, 25),
    Item("Diamond", 50, 1200),
    Item("Toothbrush", 1, 5),
    Item("Monitor", 10, 250),
    Item("Shoes", 2, 120),
]
if __name__ == "__main__":
    main()
