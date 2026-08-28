req_skills = {
    "python",
    "linux",
    "docker",
    "aws",
    "git"
}

stu_skills = set(
    input("Enter yours skills: ").split()
)

available = stu_skills & req_skills
missing = req_skills - stu_skills

print("\n--- Skill Analysis ---")

print("Your Skills:", available)
print("Missing Skills:", missing)