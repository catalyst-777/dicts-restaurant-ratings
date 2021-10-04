"""Restaurant rating lister."""


# put your code here
import random
import os
def restaurant_ratings(file_name):
    file = open(file_name)
    rating_dict = {}
    for line in file:
        keys_values = line.strip().split(':')
        rating_dict[keys_values[0]] = keys_values[1]
   
    while True: 
        answer = input("Do you want to continue? ")
        if answer == "No":
          break

        resturant_name = input("Give a resturant name: ")
        resturant_score = int(input("Give a resturant score: "))
        if resturant_score < 1 or resturant_score > 5:
            resturant_score = int(input("Sorry, please enter score between 1 and 5: "))
        
        rating_dict[resturant_name] = resturant_score
     

    return sorted(rating_dict.items())
    

def change_random(file_name):
    file = open(file_name)
    rating_dict = {}
    for line in file:
        keys_values = line.strip().split(':')
        rating_dict[keys_values[0]] = keys_values[1]
        
    picked = random.choice(list(rating_dict.items()))
    print(picked)
    choice = input(f"Do you want to change the rating of {picked}? ")
    if choice == "Yes":
        new_pick = input("What is your new rating? ")
        
        
    rating_dict[picked[0]] = new_pick
    return rating_dict

def change_rating(file_name):
    file = open(file_name)
    rating_dict = {}
    for line in file:
        keys_values = line.strip().split(':')
        rating_dict[keys_values[0]] = keys_values[1]
    
    
    resturant_name = input("What resturant rating do you want to change? ")
    if resturant_name in rating_dict:
        new_score = input("What do you want to rate this resturant? ")
        rating_dict[resturant_name] = new_score
    else:
        to_add = input("Resturant does not exist. Would you like to continue? ")
        if to_add == "Yes":
            resturant_name = input("What resturant rating do you want to change? ")
            new_score = input("What do you want to rate this resturant? ")
            rating_dict[resturant_name] = new_score
            
    return rating_dict

def view_upload_files():
    dir_list = os.listdir()
    print(dir_list)


view_upload_files()
# print(change_rating("scores.txt"))
# print(restaurant_ratings("scores.txt"))
