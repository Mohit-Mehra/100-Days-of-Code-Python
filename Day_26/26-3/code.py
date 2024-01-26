with open("Day_26/26-3/file1.txt", "r") as file1:
    f1_data = file1.readlines()

with open("Day_26/26-3/file2.txt", "r") as file2:
    f2_data = file2.readlines()


result = [int(num) for num in f1_data if num in f2_data]

# Write your code above 👆


print(result)
