n = int(input())

prev = input()
groups = 1   # first magnet always forms one group

for _ in range(1, n):
    cur = input()
    if cur != prev:
        groups += 1
    prev = cur

print(groups)
