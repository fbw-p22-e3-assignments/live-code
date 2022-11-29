# exercise 1 - task 5

users = [
    {
        "name": "Holly",
        "type": "Student",
        "password": "hunter"
    },
    {
        "name": "Peter",
        "type": "Student",
        "password": "pan"
    },
    {
        "name": "Janis",
        "type": "Teacher",
        "password": "joplin"
    }
]

user_name = input("Please enter your name: ")
user_password = input("Please enter your password: ")

def get_user(user_name, user_password):
    for user in users:
        if user['name'] == user_name and user['password'] == user_password:
            return user

def show_offer(user_name, user_password):
    user = get_user(user_name, user_password)
    role = user and user['type']
    if role != 'Teacher':
        return "We have great courses to offer you!"
    return ''

print(show_offer(user_name, user_password))
# print(show_offer('Holly', 'hunter'))
# print(show_offer('Janis', 'joplin'))
# print(show_offer('Anonymous123', 'password'))
