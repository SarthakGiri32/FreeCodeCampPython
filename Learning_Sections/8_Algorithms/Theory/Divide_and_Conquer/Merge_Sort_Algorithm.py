def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    sorted_list = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list

def main():
    unsorted_list = [42, 37, 53, 17, 98, 2, 40, 72, 33, 16, 23, 67, 82]
    print(f"Sorted list:\n{", ".join(map(str, merge_sort(unsorted_list)))}")

if __name__ == "__main__":
    main()
