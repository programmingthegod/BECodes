import threading
import time
import random
 
MAX = 20
 
THREAD_MAX = 4
 
a = [0] * MAX
part = 0
 
def merge(low, mid, high):
    left = a[low:mid+1]
    right = a[mid+1:high+1]
 
    n1 = len(left)
    n2 = len(right)
    i = j = 0
    k = low
 
    while i < n1 and j < n2:
        if left[i] <= right[j]:
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1
        k += 1
 
    while i < n1:
        a[k] = left[i]
        i += 1
        k += 1
 
    while j < n2:
        a[k] = right[j]
        j += 1
        k += 1
 
def merge_sort(low, high):
    if low < high:
        mid = low + (high - low) // 2
 
        merge_sort(low, mid)
        merge_sort(mid + 1, high)
 
        merge(low, mid, high)
 
def merge_sort_threaded():
    global part
     
    for i in range(THREAD_MAX):
        t = threading.Thread(target=merge_sort, args=(part*(MAX//4), (part+1)*(MAX//4)-1))
        part += 1
        t.start()
         
    for i in range(THREAD_MAX):
        t.join()
 
    merge(0, (MAX // 2 - 1) // 2, MAX // 2 - 1)
    merge(MAX // 2, MAX // 2 + (MAX - 1 - MAX // 2) // 2, MAX - 1)
    merge(0, (MAX - 1) // 2, MAX - 1)
 
if __name__ == '__main__':
    for i in range(MAX):
        a[i] = random.randint(0, 100)
 
    t1 = time.perf_counter()
 
    merge_sort_threaded()
 
    t2 = time.perf_counter()
 
    print("Sorted array:", a)
    print(f"Time taken: {t2 - t1:.6f} seconds")