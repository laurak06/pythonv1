# 1

names = ['Nikita', 'Katana', 'Toma']
ages = [25, 30, 35]
names_ages = dict(zip(names, ages))
print(names_ages)

# 2

text = "python"

for i, s in enumerate(text, 1):
    print(i, s)

# 3

numbers = ["10", "20", "30", "40"]
numbers = list(map(int, numbers))

print(numbers)

# 4

words = ["apple", "banana", "cherry", "dog", "elephant"]
words_d = list(filter(lambda x: x[0].lower() == 'd', words))
print(words_d)

# 5

students = ["Alice", "Bob", "Charlie", "David"]
scores = [85, 92, 78, 90]

students_scores = list(zip(students, scores))
students_more80 = list(filter(lambda x: x[1] > 80, students_scores))

enumerated = []

for i, student in enumerate(students_more80, 1):
    print(i, student[0])
    enumerated.append((i,) + student)

print(enumerated)


