from user import User
def check_user(user_id,list_of_users):
    for index in range (0,len(list_of_users)):
        if list_of_users[index].id==user_id:
           return list_of_users[index]
    user=User(user_id)
    list_of_users.append(user)
    return user