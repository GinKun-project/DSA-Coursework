def longest_hike(trail, k):
    start = 0
    max_length = 0

    for end in range(1, len(trail)):
        while start < end and trail[end] - trail[start] > k:
            start += 1
        max_length = max(max_length, end - start + 1)

    return max_length


trail = [4, 2, 1, 4, 3, 4, 5, 8, 15]
k = 3
print(longest_hike(trail, k))