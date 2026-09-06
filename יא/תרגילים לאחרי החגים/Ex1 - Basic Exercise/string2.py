# Additional basic string exercises

# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
def verbing(s):
     # +++your code here+++
    return ' '


# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(s):
     # +++your code here+++
    return ' '


# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
def front_back(a, b):
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


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
    print('verbing')
    results_compare(verbing('hail'), 'hailing')
    results_compare(verbing('swiming'), 'swimingly')
    results_compare(verbing('do'), 'do')

    print
    print('not_bad')
    results_compare(not_bad('This movie is not so bad'), 'This movie is good')
    results_compare(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    results_compare(not_bad('This tea is not hot'), 'This tea is not hot')
    results_compare(not_bad("It's bad yet not"), "It's bad yet not")
    results_compare(not_bad("my name is yoram"), "my name is yoram")

    print
    print('front_back')
    results_compare(front_back('abcd', 'xy'), 'abxcdy')
    results_compare(front_back('abcde', 'xyz'), 'abcxydez')
    results_compare(front_back('Kitten', 'Donut'), 'KitDontenut')


if __name__ == '__main__':
    main()
    input()
