def sort_the_apples(apples, bucket_1, bucket_2):
    bucket_1 = []
    bucket_2 = []
    for apple in apples:
        if apple == 'red':
            bucket_1.append(apple)
        else:
            bucket_2.append(apple)
    return bucket_1, bucket_2


here_are_apples = ['red', 'green', 'red', 'yellow', 'green', 'red']
sorted_bucket_1, sorted_bucket_2 = sort_the_apples(
    here_are_apples, bucket_1=[], bucket_2=[])

print(len(sorted_bucket_1))
print(len(sorted_bucket_2))
