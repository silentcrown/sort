# -*- coding:utf-8 -*-.
# 选择排序 O(n**2), O(1),
import copy

arr = [-7, 23, 1, -10, 3, 4, -2, 3, 0, 9, 45, -4]


def select_sort(aaa):
    a = copy.deepcopy(aaa)
    for i in range(len(a) - 1):
        min_ind = None
        for j in range(i, len(a)):
            if min_ind == None:
                min_ind = j
            if a[j] < a[min_ind]:
                min_ind = j
        a[i], a[min_ind] = a[min_ind], a[i]
    return a


# 插入排序
def insert_sort(aaa):
    a = copy.deepcopy(aaa)
    for i in range(len(a) - 1):
        for j in range(i + 1, 0, -1):
            if a[j] < a[j - 1]:
                a[j], a[j - 1] = a[j - 1], a[j]
    return a


# 改进冒泡排序
def bubble_sort(aaa):
    a = copy.deepcopy(aaa)
    for i in range(len(a)):
        flag = 0
        for j in range(1, len(a) - i):
            if a[j - 1] > a[j]:
                a[j], a[j - 1] = a[j - 1], a[j]
                flag = 1
        if flag == 0: break
    return a



def quick_sort(aaa):
    a = copy.deepcopy(aaa)
    if len(a) < 1: return a
    left, right = 0, len(a) - 1
    quick_sort_dfs(a, left, right)
    return a


def quick_sort_dfs(data, l, r):
    i, j = l, r
    if len(data) < 1 or l > r:
        return
    x = data[i]
    while i < j:
        while i < j and data[j] >= x:
            j -= 1
        if i < j:
            data[i] = data[j]
            i += 1
        while i < j and data[i] <= x:
            i += 1
        if i < j:
            data[j] = data[i]
            j -= 1
    data[i] = x
    quick_sort_dfs(data, l, i - 1)
    quick_sort_dfs(data, i + 1, r)
    return


def adjust_to_large_heap(a, i, end):
    # 调整成大根堆，根结点最大
    cur_ind = i
    while cur_ind < end:
        left_ind = 2 * cur_ind + 1
        right_ind = 2 * cur_ind + 2
        max_ind = cur_ind
        if left_ind < end and a[left_ind] > a[max_ind]:
            max_ind = left_ind
        if right_ind < end and a[right_ind] > a[max_ind]:
            max_ind = right_ind
        if max_ind != cur_ind:
            a[cur_ind], a[max_ind] = a[max_ind], a[cur_ind]
            cur_ind = max_ind
        else:
            break


def heap_sort(aaa):
    a = copy.deepcopy(aaa)
    first = int((len(a) - 1) / 2)
    while first >= 0:
        adjust_to_large_heap(a, first, len(a))
        first -= 1

    end = len(a) - 1
    while end > 0:
        a[0], a[end] = a[end], a[0]
        adjust_to_large_heap(a, 0, end)
        end -= 1
    return a


def shell_sort(aaa):
    a = copy.deepcopy(aaa)
    gap = int(len(a) / 2)
    while gap > 0:
        for i in range(len(a) - gap):
            if a[i] > a[i + gap]:
                a[i], a[i + gap] = a[i + gap], a[i]
        gap -= 1
    return a


def merge_split(a, l, r):
    if l >= r:
        return
    mid = int((l + r) / 2)
    merge_split(a, l, mid)
    merge_split(a, mid + 1, r)
    merge_two(a, l, r, mid)


def merge_two(a, l, r, mid):
    cl, cr = l, mid + 1
    temp = []
    while cl <= mid and cr <= r:
        if a[cl] <= a[cr]:
            temp.append(a[cl])
            cl += 1
        else:
            temp.append(a[cr])
            cr += 1
    while cl <= mid:
        temp.append(a[cl])
        cl += 1
    while cr <= r:
        temp.append(a[cr])
        cr += 1
    for i in range(l, r + 1):
        a[i] = temp[i - l]
    return


def merge_sort(aaa):
    a = copy.deepcopy(aaa)
    merge_split(a, 0, len(a) - 1)
    return a


print(arr)
aa = copy.deepcopy(arr)
aa.sort()
print(aa)
print('简单选择排序：' + '正确' if aa == select_sort(arr) else '简单选择排序：' + '错误')
print('简单插入排序：' + '正确' if aa == insert_sort(arr) else '简单选择排序：' + '错误')
print('改进冒泡排序：' + '正确' if aa == bubble_sort(arr) else '改进冒泡排序：' + '错误')
print('快速排序：' + '正确' if aa == quick_sort(arr) else '快速排序：' + '错误')
print('堆排序：' + '正确' if aa == heap_sort(arr) else '堆排序：' + '错误')
print('希尔排序：' + '正确' if aa == shell_sort(arr) else '希尔排序：' + '错误')
print('归并排序：' + '正确' if aa == merge_sort(arr) else '归并排序：' + '错误')