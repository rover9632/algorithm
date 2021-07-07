import random


def quick_sort(a, l=0, r=None):
    if r is None:
        r = len(a) - 1
    if l >= r:
        return

    ori_l, ori_r = l, r
    p = l
    flag = True
    while l < r:
        if flag:
            while a[r] >= a[p] and r > p:
                r -= 1
            a[p], a[r] = a[r], a[p]
            p = r
            flag = not flag
        else:
            while a[l] <= a[p] and l < p:
                l += 1
            a[p], a[l] = a[l], a[p]
            p = l
            flag = not flag

    quick_sort(a, ori_l, p - 1)
    quick_sort(a, p + 1, ori_r)


def main(args):
    a = list(range(50))
    a = random.choices(a, k=20)
    print(a)
    quick_sort(a)
    print(a)
