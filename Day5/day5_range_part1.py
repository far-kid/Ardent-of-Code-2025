# def performbs(item):
#     f

fresh_items = 0

ranges= []
values = []
with open(r"Day5/input.txt") as f:
    before, after = f.read().strip().split("\n\n")

ranges = [list(map(int, line.split("-"))) for line in before.splitlines()]
values = [int(line) for line in after.splitlines()]



values = sorted(values)
ranges = sorted(ranges, key=lambda ranges: ranges[0])
print(values)

for value in values:
    if value<ranges[0][0]:
        continue
    if value>ranges[len(ranges)-1][1]:
        break
    for r in ranges:
        if value>r[0] and value<r[1]:
            fresh_items+=1
            break
    
    
    

print(fresh_items)