def quick_sort(int_list: list[int]) -> list[int]:
    if len(set(int_list)) <= 1:
        return int_list

    pivot_index: int = len(int_list) // 2
    less_than_pivot_list: list[int] = [n for n in int_list if n < int_list[pivot_index]]
    equal_to_pivot_list: list[int] = [n for n in int_list if n == int_list[pivot_index]]
    greater_than_pivot_list: list[int] = [n for n in int_list if n > int_list[pivot_index]]

    less_than_pivot_list = quick_sort(less_than_pivot_list)
    equal_to_pivot_list = quick_sort(equal_to_pivot_list)
    greater_than_pivot_list = quick_sort(greater_than_pivot_list)

    sorted_list: list[int] = []

    sorted_list.extend(less_than_pivot_list)
    sorted_list.extend(equal_to_pivot_list)
    sorted_list.extend(greater_than_pivot_list)

    return sorted_list


def main() -> None:
    print(quick_sort([20, 3, 14, 1, 5]))
    print(quick_sort([83, 4, 24, 2]))
    print(quick_sort([4, 42, 16, 23, 15, 8]))
    print(quick_sort([87, 11, 23, 18, 18, 23, 11, 56, 87, 56]))
    print(quick_sort([87, 15, 23, 18, 27, 23, 11, 56, 73, 56]))


if __name__ == "__main__":
    main()
