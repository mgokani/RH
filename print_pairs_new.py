# pairs([4, 1, 3, 5, 2, 6, 8, 7], 8)

d = {}

p = [4, 1, 3, 5, 2, 6, 8, 7]
n = 8
r = []

for index, value in enumerate(p):
  if value in d:
    r.append(value)
    r.append(p[d[value]])
  else:
    d[n - value] = index

print(d)

print(r)
