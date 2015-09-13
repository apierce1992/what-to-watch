from movie_lib import *
from user_relations import *


def top_50():
    popularity = {}
    for key, value in all_ratings.items():
        if len(value) >= 20:
            avg = sum(value)/len(value)
            popularity[key] = round(avg, 2)
            sorted_list = sorted(popularity.items(), key = lambda c: c[1], reverse = True)
            top_50 = sorted_list[:50]
            counter = 0
    for x in top_50:
        print(str(counter+1) + ': ' +str(all_movies[top_50[counter][0]]) + ' ' + str(top_50[counter][1]))
        counter += 1

def top_50_for_user(user_id):
    pop_unseen = {}
    user_seen = all_reviewed(user_id)
    for key, value in all_ratings.items():
        if key not in user_seen:
            if len(value) >= 20:
                avg = sum(value)/len(value)
                pop_unseen[key] = round(avg, 2)
                sorted_list = sorted(pop_unseen.items(), key = lambda c: c[1], reverse = True)
                top_50 = sorted_list[:50]
                counter = 0
    for x in top_50:
        print(str(counter+1) + ': ' +str(all_movies[top_50[counter][0]]) + ' ' + str(top_50[counter][1]))
        counter += 1


def main():
    print("Okay let's see the top 50 movies! At least according to Movie Lens...")
    user = input("What is your user id? Remember we have a total of 943 users.\n")
    user = int(user)
    top_50_for_user(user)
main()
