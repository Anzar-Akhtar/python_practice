required_skills = {
    "python",
    "git",
    "linux",
    "html",
    "css"
}

student_skills = set(
    input("Enter your skills: ").lower().split()
)

available = student_skills & required_skills

missing = required_skills - student_skills

extra = student_skills - required_skills

print("\n===== CLUB ELIGIBILITY =====")

print("Available skills:", available)

print("Missing skills:", missing)

print("Extra skills:", extra)

print("Required skills:", len(required_skills))
print("Your required skills:", len(available))

if len(available) >= 3:
    print("Status: Eligible ✅")
else:
    print("Status: Not Eligible ❌")