# Additional basic list exercises

# D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.
def remove_adjacent(nums):
    # +++your code here+++
    return ' '


# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.
def linear_merge(list1, list2):
     # +++your code here+++
    return ' '
    

# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def results_compare(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print(f'{prefix} got: {got}  expected: {expected}')


# Calls the above functions with interesting inputs.
def main():
    print('remove_adjacent')
    results_compare(remove_adjacent([1, 2, 2, 3, 3, 5, 5, 5]), [1, 2, 3, 5])
    results_compare(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
    results_compare(remove_adjacent([]), [])

    print()
    print('linear_merge')
    results_compare(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']), ['aa', 'bb', 'cc', 'xx', 'zz'])
    results_compare(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']), ['aa', 'bb', 'cc', 'xx', 'zz'])
    results_compare(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']), ['aa', 'aa', 'aa', 'bb', 'bb'])


if __name__ == '__main__':
    main()
    input()
