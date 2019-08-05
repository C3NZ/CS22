"""
    Solving the knapsack and another dynamic programming problem
    of my choice.
"""


class Item:
    """
        Item to store meta information for items that
        are to be stored within the knapsack.
    """

    def __init__(self, name, weight, value):
        self.name = name
        self.value = value
        self.weight = weight

    def __eq__(self, other_item):
        return self.value == other_item.value

    def __lt__(self, other_item):
        return self.value < other_item.value

    def __gt__(self, other_item):
        return self.value < other_item.value

    def __str__(self):
        return f"<Item: {self.name}, Value: {self.value}, Weight: {self.weight}>"

    def __repr__(self):
        return f"<Item: {self.name}, Value: {self.value}, Weight: {self.weight}>"


def simple_knapsack(capacity, items, cost_func, curr_index=None):
    """
        Simple knapsack solution that has a naive approach of finding the best
        items
    """
    # If there is no more space left or we've traversed all the items, return
    # 0, as we can't go further

    if curr_index is None:
        curr_index = len(items) - 1

    if capacity == 0 or curr_index <= 0:
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


def main():
    """
        Solve the knapsack problem and another DP programming challenge.
    """
    capacity = 20
    items = [
        Item("Macbook", 20, 15),
        Item("TV", 15, 30),
        Item("IPhone", 5, 8),
        Item("USB", 3, 1),
        Item("Minecraft", 20, 1),
        Item("Super dense diamond", 50, 30),
        Item("Toothbrush", 1, 1),
        Item("Monitor", 5, 5),
        Item("Shoes", 2, 5),
        Item("Books", 4, 20),
    ]

    items = sorted(items)

    item_values, items = simple_knapsack(capacity, items, lambda item: item.value)

    item_values, items = simple_knapsack(
        capacity, items, lambda item: item.value / item.weight
    )


if __name__ == "__main__":
    main()
