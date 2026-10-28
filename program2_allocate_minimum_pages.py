"""
Experiment 3: Matrix and Binary Search
Program 2: Allocate Minimum Pages
Aim: Minimize the maximum pages assigned to any student.
"""

def allocate_pages(pages, students):
    if students > len(pages):
        return -1
    low, high = max(pages), sum(pages)
    answer = high
    while low <= high:
        mid = (low + high) // 2
        used, total = 1, 0
        for p in pages:
            if total + p > mid:
                used += 1
                total = p
            else:
                total += p
        if used <= students:
            answer = mid
            high = mid - 1
        else:
            low = mid + 1
    return answer

print(allocate_pages([12, 34, 67, 90], 2))
