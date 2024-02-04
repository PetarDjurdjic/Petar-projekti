class Youtube:
    def __init__(self, username, subscribers=0, subscriptions=0):
        self.username = username
        self.subscribers = subscribers
        self.subscriptions = subscriptions    

    def subscribe(self,user):
        user.subscribers +=1
        self.subscriptions +=1


user1 = Youtube("Elshad")
user2 = Youtube("Renad")
user1.subscribe(user2)
user2.subscribe(user1)
print(f"User 1 subscribers: {user1.subscribers}")
print(f"User 1 subscriptions: {user1.subscriptions}")
print(f"User 2 subscribers: {user2.subscribers}")
print(f"User 2 subscriptions: {user2.subscriptions}")
print(user1.subscribers)
print(user1.subscriptions)
print(user2.subscribers)
print(user2.subscriptions)
