def quick_sort(list_to_sort) -> list:
    """Algorytm szybkiego sortowania"""

    if len(list_to_sort) <= 1:
        return list_to_sort
    else:
        mid_point = (len(list_to_sort) - 1) // 2
        mid_value = list_to_sort[mid_point]
        left_list = [x for i, x in enumerate(list_to_sort) if (i != mid_point and x <= mid_value)]
        right_list = [x for i, x in enumerate(list_to_sort) if (i != mid_point and x > mid_value)]
        return quick_sort(left_list) + [mid_value] + quick_sort(right_list)


# -----------------------------------------------------
import random


def quick_sort_test(n) -> bool:
    l = [random.randint(1, n) for i in range(n)]
    return quick_sort(l) == sorted(l)
# -----------------------------------------------------


# test
def main():
    l = [12, 3, 87, -9, 2, 988, 76, 3.8, 0, 3, 77, 27]
    print('Przed sortowaniem:\r\n%s' % str(l))
    print('Po sortowaniu:\r\n%s' % str(quick_sort(l)))

    print('Test na liczbach losowych:', quick_sort_test(1000))


if __name__ == '__main__':
    main()