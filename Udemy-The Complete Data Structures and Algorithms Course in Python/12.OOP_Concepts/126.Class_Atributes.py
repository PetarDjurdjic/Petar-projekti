# class StarCookie:
#     def __init__(self,color,weight):
#         self.color = color
#         self.weight = weight

# # star_cookie1 = StarCookie()
# # star_cookie1.weight = 15
# # star_cookie1.color = "Red"
# # print(star_cookie1.weight)
# # print(star_cookie1.color)

# star_cookie1 = StarCookie("Red", 16)
# print(star_cookie1.color)
# print(star_cookie1.weight)


# class YouTube:
#     def __init__(self, username,subscribers = 0):
#         self.username = username
#         self.subscribers = subscribers

# user1 = YouTube("Elshad")
# print(user1.username)
# print(user1.subscribers)

# user2 = YouTube("Renad")
# user2.subscriber = 5
# print(user2.username)
# print(user2.subscribers)



class StarCookie:
    milk = 0.1
    def __init__(self, color, weight):
        self.color = color
        self.weight = weight

star_cookie1 = StarCookie("Red", 16)
star_cookie2 = StarCookie("Blue", 15)
star_cookie1.milk = 0.2

print(star_cookie1.__dict__)
print(star_cookie2.__dict__)
print(StarCookie.__dict__)

print(star_cookie1.milk)
print(star_cookie2.milk)
print(StarCookie.milk)
