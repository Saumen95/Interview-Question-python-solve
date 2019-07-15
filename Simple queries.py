def b_search(arr, target):
    l , r = 0, len(arr) - 1
    while l < len(arr) and r >= 0 and l <= r:
        mid = (l + r) // 2

        if arr[mid] == target:
            return mid + 1

        elif arr[mid]>target:
            r = mid - 1

        else:
            l = mid + 1

    return l


def count(nums, maxs):
    nums = sorted(nums)
    result = []
    for maxi in maxs:
        count = b_search(nums, maxi)
        result.append(count) 

    return result


arr = [1, 2, 4, 4, 7]
maxes = [3, 5]
res = count(arr, maxes)
print("numbers =", arr, "maxes =", maxes, "answer =", res)