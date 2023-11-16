# Recursion


def sum_list(x):
    """
    Summing a List of numbers"""
    # base case is if the list doesn't exist => return 0
    if not x:
        return 0
    # use first + rest
    else:
        return x[0] + sum_list(x[1:])


def sum_nested_list(x):
    """
    Summing a nested list of numbers"""
    # base case is if the list doesn't exist => return 0
    if not x:
        return 0
    # if the first item is a nested list, perform recursion on the first as well as the rest
    elif isinstance(x[0], list):
        return sum_nested_list(x[0]) + sum_nested_list(x[1:])
    # otherwise perform recursion only on the rest of the list
    else:
        return x[0] + sum_nested_list(x[1:])


def cleaned(l):
    """
    Cleaning zeroes from ends of a list without loops
    """
    # if the list is empty
    if not l:
        return []
    # if the front is 0, keep executing on the rest of the list
    elif l[0] == 0:
        return cleaned(l[1:])
    # if the end is 0, keep executing on the list excluding the last element
    elif l[-1] == 0:
        return cleaned(l[:-1])
    # otherwise, return the list
    return l[:]


def elements(tree):
    """
    Generator for all elements from tree"""
    yield tree[0]
    for child in tree[1:]:
        yield from elements(child)


def swap_pairs(inp):
    """
    Swap adjacent pairs"""
    # base case => return the unmodified list if it's length 0 or 1
    if len(inp) < 2:
        return inp[:]
    else:
        # returns the first pair reversed, perform recursion on rest
        return [inp[1], inp[0]] + swap_pairs(inp[2:])


if __name__ == "__main__":
    # list_nums = [1, 2, 3, 4, 5]
    # print(sum_list(list_nums))
    # nested_list_nums = [[1, 2], [3, [4, 5]], [[[[[6]]]]]]
    # print(sum_nested_list(nested_list_nums))
    # dirty_list = [0, 0, 0, 1, 2, 3, 4, 5, 0, 0, 0, 0]
    # print(cleaned(dirty_list))
    # tree = [13, [7], [8, [99], [16, [77]], [42]]]
    # for elem in elements(tree):
    #     print(elem)
    # pairs = [1, 2, 3, 4]
    # print(swap_pairs(pairs))
    test = [1, 2]
    print(test[0:1] + [3])
