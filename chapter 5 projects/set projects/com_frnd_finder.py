user1 = set(
    input("Enter user 1 friends: ").split()
)

user2 = set(
    input("Enter user 2 friends: ").split()
)

com_frnd = user1 & user2
uni_frnd1 = user1 - user2
uni_frnd2 = user2 - user1

print("\nCommon Friends:")
for friend in com_frnd:
    print(friend)

print("\nuser 1 unique frnds:", uni_frnd1)
print("\nuser 2 unique frnds:", uni_frnd2)