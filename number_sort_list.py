# Create a sorting function which sorts numbers not by numerical order, but by number length!
# This means sorting numbers with the least digits first, up to
# the numbers with the most digits.
# Notes
# If two numbers have the same number of digits,
# return them in the order they first appeared (this makes it
# different to just sorting the numbers normally).
def number_len_sort(lst):
    sorted_list = []
    for length in range(1, 11):
        for i in lst:
            if len(str(i)) == length:
                sorted_list.append(i)
    return sorted_list


print(number_len_sort([1, 54, 1, 2, 463, 2]))

print(number_len_sort([999, 421, 22, 990, 32]))

print(number_len_sort([9, 8, 7, 6, 5, 4, 31, 2, 1, 3]))
