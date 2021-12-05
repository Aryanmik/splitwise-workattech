class UsersDb:

    users = {}

    def get(self,user_id):
        user = self.users.get(user_id)
        if not user:
            print(f"User with user_id : {user_id} doesn't exist in db!")
        return user

    def save(self, user):
        self.users[user.id] = user
        return user