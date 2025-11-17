#Assignment 5

##Task 1

student = {'Alex':89,
           'Alice':87,
           'Bob':79,
           'Maya':88,
           'Jakob':90,
           "Justin"#Its value is None
           'Mark':75,
           'Lala':87}

user_name = input("Enter the student name:")
try:
    #data = student["user_name"]
    print(f"{user_name}'s mark is: {student[user_name]}")

except :
    print(f"{user_name} is not found. Please try with Correct name.")


##Task 2

list = [1,2,3,4,5,6,7,8,9,10]

first_five = list[0:5]
rev_ff = first_five[::-1]

print(f"Original list: {list}")
print(f"Extracted first five elements: {first_five}")
print(f"Reversed extracted elements: {rev_ff}")
