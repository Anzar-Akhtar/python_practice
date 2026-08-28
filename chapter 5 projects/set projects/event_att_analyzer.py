day1 = set(
    input("Enter Day 1 students: ").split()
)

day2 = set(
    input("Enter Day 2 students: ").split()
)

both_days = day1 & day2
only_day1 = day1 - day2
only_day2 = day2 - day1
all_stu = day1 | day2

print("\n==== EVENT REPORT ====")

print("Student on both days:", both_days)
print("Only day 1:", only_day1)
print("Only day 2:", only_day2)
print("Total unique students:", len(all_stu))

if both_days:
    print("Yes, some students attended both days")
else:
    print("No student attended both days")