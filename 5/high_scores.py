high_scores = input("Input scores: ").split()
highest = 0

for n in range(0, len(high_scores)):
    high_scores[n] = int(high_scores[n])

for score in high_scores:
    if score > highest:
        highest = score

print(f"The highest score is: {highest}")