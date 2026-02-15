# defining a program to manage and analyze user data

def average(scores):
        return sum(scores)/len(scores)
    
def check_admin(roles):
    if "admin" in roles:
        return "Yes"
    else:
        return "No"
    
def main():  
    user_info = [
    {
        "Name": "Ana",
        "Scores": [78, 85, 91],
        "Roles": {"editor", "admin"}
    },
    {
        "Name": "Arihant",
        "Scores": [93, 84, 77],
        "Roles": {"viewer", "admin"},
    },
    {
        "Name": "Aysha",
        "Scores": [81, 69, 97],
        "Roles": {"viewer"}
    }
]
    for user in user_info:
        name = user["Name"]
        score_list = user["Scores"]
        user_roles = user["Roles"]

        avg = average(score_list)
        is_admin = check_admin(user_roles)
        details = (name, avg, is_admin)

        print(f"Name: {details[0]}")
        print(f"Average: {details[1]}")
        print(f"Admin Access: {details[2]}")

main()