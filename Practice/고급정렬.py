#셸 정렬
def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr


#힙 정렬
def heap_sort(arr):
    #노드의 수
    n = len(arr)

    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    return arr


#병합 정렬
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


#퀵 정렬
def quick_sort(arr, pivot_index=None):
    if len(arr) <= 1:
        return arr
    
    if pivot_index is None:
        pivot = arr[len(arr) // 2]
    else:
        pivot = arr[pivot_index]

    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)

#이중피벗 퀵정렬
def double_quick_sort(arr, pivot_index1=None, pivot_index2=None):
    if len(arr) <=1:
        return arr
    
    pivot1 = arr[0] if pivot_index1 is None else arr[pivot_index1]
    pivot2 = arr[-1] if pivot_index2 is None else arr[pivot_index2]

    if pivot1 > pivot2:
        pivot1, pivot2 = pivot2, pivot1

    left = [x for x in arr if x < pivot1]
    p1 = [x for x in arr if x == pivot1]
    mid = [x for x in arr if (x > pivot1 and x < pivot2)]
    # 두 피벗이 같으면 p1에 이미 담겨 있으므로 p2는 비움
    p2 = [x for x in arr if x == pivot2] if pivot2 != pivot1 else []
    right = [x for x in arr if x > pivot2]

    return double_quick_sort(left) + p1 + double_quick_sort(mid) + p2 + double_quick_sort(right) 

#Radix 정렬
def radix_sort(arr):
    if len(arr) <= 1:
        return arr

    def counting_sort_by_digit(arr, exp):
        buckets = [[] for _ in range(10)]
        for num in arr:
            digit = (num // exp) % 10
            buckets[digit].append(num)
        result = []
        for bucket in buckets:
            result.extend(bucket)
        return result

    def sort_non_negative(arr):
        if not arr:
            return arr
        max_val = max(arr)
        exp = 1
        while max_val // exp > 0:
            arr = counting_sort_by_digit(arr, exp)
            exp *= 10
        return arr

    # 음수는 절댓값으로 정렬한 뒤 순서를 뒤집어 양수 앞에 붙임
    negatives = sort_non_negative([-x for x in arr if x < 0])
    positives = sort_non_negative([x for x in arr if x >= 0])
    return [-x for x in reversed(negatives)] + positives


# 테스트
arr = [27, 10, 12, 20, 25, 13, 15, 22, 30]

print("Shell Sort: ", shell_sort(arr.copy()))
print("Heap Sort:  ", heap_sort(arr.copy()))
print("Merge Sort: ", merge_sort(arr.copy()))
print("Quick Sort: ", quick_sort(arr.copy()))
print("Double Quick Sort: ", double_quick_sort(arr.copy()))
print("Radix Sort: ", radix_sort(arr.copy()))