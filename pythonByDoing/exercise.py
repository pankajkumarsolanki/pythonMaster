import random

# #lottery_numbers = set(random.sample(range(22), 6))
# lottery_numbers = {8, 0, 4, 6, 20}
#
# # Here are your players; find out who has the most numbers matching lottery_numbers!
# players = [
#     {'name': 'Rolf', 'numbers': {1, 3, 5, 7, 9, 11}},
#     {'name': 'Charlie', 'numbers': {2, 7, 8, 22, 10, 5}},
#     {'name': 'Anna', 'numbers': {13, 14, 15, 16, 17, 18}},
#     {'name': 'Jen', 'numbers': {19, 2, 12, 7, 3, 5}}
# ]
# # l = []
# for player in players:
#     s = set(player["numbers"]).intersection(lottery_numbers)
#     l.append(len(s))
# print(l)
#
# for j in l:
#     if j == max(l):
#         print("{} won {}.".format(players[j]["name"], (max(l)*100)))
#

# -----------------------------------

#Udemy Solution>>#
#
# top_player = players[0]  # start by saying "the top matching player is the first one"
#
# for player in players:  # Go over each player
#     matched_numbers = len(player["numbers"].intersection(lottery_numbers))  # Calculate how many numbers they matched
#     if matched_numbers > len(top_player["numbers"].intersection(lottery_numbers)):  # If they matched more than the current top player...
#         top_player = player  # Say this player is the new top player
#
# # Calculate their winnings using the formula!
# winnings = 100 ** len(top_player["numbers"].intersection(lottery_numbers))
#
# # Then print out—here in Udemy we have to use .format, but normally you'd want to use f-strings.
# print(f"{top_player['name']} won {winnings}.")

#----------------------------------------------------

# We have a class called Club, and it is initialized like this (no need to change):
class Club:
    def __init__(self, name):
        self.name = name
        self.players = []
        
    def __len__(self):
        return  len(self.players)

    def __getitem__(self, i):
        return self.players[i]

    def __str__(self):
        return f"Club {self.name} with {len(self)} players"

    def __repr__(self):
        return f"Club {self.name}: {self.players}"

# define a method that allows us to access the i-th player in the club directly via indexing.
# for example, if some_club is an object of Club class,
# we can access the i-th player in some_club like this (you may assume i is always valid):
# some_club[i]

some_club = Club('Arsenal')
some_club.players.append('Rolf')
some_club.players.append('Anne')
print(some_club[1])

# define a method that returns a string representation of this object,
# which can be used to recreate this object.
# The return value should be in such format (beware of the spacing):
# Club {club_name}: {list_of_players}
# the club_name and list_of_players should be replaced by the according value of current object


# define a method that returns a readable string representation of this object for the user.
# The return value should be in such format (beware of the spacing):
# Club {club_name} with {count_of_players} players
# the club_name and count_of_players should be replaced by the according value of current object


# You only need to finish the methods, we will take care of the object creation and call those methods for you!