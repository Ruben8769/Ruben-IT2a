nearby_people = {'Rolf', 'Jen', 'Anna'}
user_friends = set()
username = input("What's your name? ")
user_friends.add(username)
print(nearby_people.intersection(user_friends))