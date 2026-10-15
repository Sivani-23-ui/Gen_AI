marks_list = [78, 35, 92, 40, 61]
marks_tuple = tuple(marks_list)

print("List:", marks_list)
print("List data type:", type(marks_list))

print("Tuple:", marks_tuple)
print("Tuple data type:", type(marks_tuple))

print("Highest marks:", max(marks_list))
print("Lowest marks:", min(marks_list))

pass_count = (
    (marks_list[0] >= 40)
    + (marks_list[1] >= 40)
    + (marks_list[2] >= 40)
    + (marks_list[3] >= 40)
    + (marks_list[4] >= 40)
)

print("Students scoring at least 40:", pass_count)

valid_range = min(marks_list) >= 0 and max(marks_list) <= 100
print("All marks are within 0 to 100:", valid_range)

marks_list[0] = 80
print("Modified list:", marks_list)

# A tuple is immutable, so changing an element causes a TypeError.
# Uncomment the next line to observe the error.
# marks_tuple[0] = 80

print("Original tuple remains:", marks_tuple)
