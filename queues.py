import sys
from collections import deque


def total_turns(times, q):
    turns = 0
    for t in times:
        turns += (t + q - 1) // q
    return turns


def completion_order(times, q):
    queue = deque()

    for i, t in enumerate(times, start=1):
        queue.append((i, t))

    order = []

    while queue:
        task_num, remaining = queue.popleft()

        remaining -= q

        if remaining <= 0:
            order.append(task_num)
        else:
            queue.append((task_num, remaining))

    return order


def main():
    n, q = map(int, input().split())
    times = list(map(int, input().split()))

    order = completion_order(times, q)

    print("Completion Order: " + " ".join(map(str, order)))
    print("Total Turns: " + str(total_turns(times, q)))


main()