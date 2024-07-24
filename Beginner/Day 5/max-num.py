# Find max score
# Input scores separated by comma
scores = input().split(',')
for n in range(0, len(scores)):
    scores[n] = int(scores[n])
max_score = 0
for score in scores:
    if score > max_score:
        max_score = score
print(max_score)