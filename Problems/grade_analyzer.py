num_subjects = int(input("How many scores you want to collect: "))
grades = []
total = 0
average = 0
i = 1

for grade in range(num_subjects):
    score = int(input("Please enter your score: "))
    grades.append(score)

print("\nRatings:")
for scores in grades:
    total += scores
    if scores < 100 and scores >= 90:
        print(f"{scores}: Excellent")
    elif scores <= 89 and scores >= 75:
        print(f"{scores}: Passed")
    elif scores < 75:
        print(f"{scores}: Needs improvement")
    else:
        print("{scores}: Invalid score")

average = total / num_subjects
print(f"Grade average: {average:.2f}")
