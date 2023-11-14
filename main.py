# Recursion

"""
Summing a List of numbers
"""


def sum_list(x):
    # base case is if the list doesn't exist => return 0
    if not x:
        return 0
    # use first + rest
    else:
        return x[0] + sum_list(x[1:])


"""
Summing a nested list of numbers
"""


def sum_nested_list(x):
    # base case is if the list doesn't exist => return 0
    if not x:
        return 0
    # if the first item is a nested list, perform recursion on the first as well as the rest
    elif isinstance(x[0], list):
        return sum_nested_list(x[0]) + sum_nested_list(x[1:])
    # otherwise perform recursion only on the rest of the list
    else:
        return x[0] + sum_nested_list(x[1:])


"""
Cleaning zeroes from ends of a list without loops
"""


def cleaned(l):
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


"""
Generator all elements from tree
"""


def elts(tree):
    yield tree[0]
    for child in tree[1:]:
        yield from elts(child)


if __name__ == "__main__":
    list_nums = [1, 2, 3, 4, 5]
    nested_list_nums = [[1, 2], [3, [4, 5]], [[[[[6]]]]]]
    dirty_list = [0, 0, 0, 1, 2, 3, 4, 5, 0, 0, 0, 0]
    tree = [13, [7], [8, [99], [16, [77]], [42]]]
    # print(sum_list(list_nums))
    # print(sum_nested_list(nested_list_nums))
    # print(cleaned(dirty_list))
    # for elem in elts(tree):
    #     print(elem)
    # agenda = 13
    

