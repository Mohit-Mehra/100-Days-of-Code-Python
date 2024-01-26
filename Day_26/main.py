# List Comprehension

# numbers = [1, 2, 3, 4]
# new_numbers = [n + 1 for n in numbers]
# print(new_numbers)


# range_list = [n * 2 for n in range(1, 6)]
# print(range_list)


# name = "Mohit"
# new_list = [letter for letter in name]
# print(new_list)


# names = ["Mohit", "Blazorus", "Goku", "Naruto"]

# short_names = [name for name in names if len(name) <= 5]
# print(short_names)

# long_names = [name.upper() for name in names if len(name) > 5]
# print(long_names)


# Dictionary Comprehension
import random

names = ["Mohit", "Blazorus", "Goku", "Naruto"]
students_score = {student: random.randint(1, 100) for student in names}
print(students_score)

passed_student = {
    student: score for (student, score) in students_score.items() if score >= 60
}
print(passed_student)
