nums = [3, 6, 8, 4]
sorted(nums)

names = ["ala", "anna", "karol", "jan"]
# sortujemy po długości słowa
sorted(names, key=len)


def get_user_age(user):
    _, age = user
    return age


# własna funckja do sortowania
users = [("bob, 25"), ("ann", 20)]
sorted(users, key=get_user_age)

# uzycie lambdy - taka mini funkcja
users = [("bob, 25"), ("ann", 20)]
sorted(users, key=lambda x: x[1])
