import sys

def print_all_names():
    for name in cookbook:
        print(name)
    print("\n")


def print_details(namee):
    if namee in cookbook:
        recp = (cookbook[namee])
        for name in recp:
            print(name.ljust(13,' '),":",recp[name])
    else:
        print("this %s not found in cookbook" % namee)
    print("\n")


def delete_recipe(namee):
    if namee in cookbook:
        del cookbook[namee]
    else:
        print("this %s not found in cookbook" % namee)
    print("\n")

def add_recipe():
    recipe = {}
    print(">>> Enter a name:")
    name = input()
    print(">>> Enter ingredients:")
    ingredients = []
    while(True):
        inpt = input()
        if inpt == "":
            break
        ingredients.append(inpt)
        
    recipe["ingredients"] = ingredients;
    print(">>> Enter a meal type:")
    recipe["type"] = input()

    print(">>> Enter a preparation time:")
    recipe["prep_time"] = int(input())
    cookbook[name] = recipe
def info():
    print("Welcome to the Python Cookbook !")
    print("List of available option:")
    print("   1: Print all recipe names.")
    print("   2: Print a details of the recipe name")
    print("   3: Delete a recipe from menu")
    print("   4: Add a recipe to the menu")
    print("   5: Quit")


cookbook = {}
recipe = {"ingredients": ["ham", "bread", "cheese", "tomatoes"],
          "meal": "lunch",
          "prep_time": 10}
cookbook["Sandwich"] = recipe

recipe = {"ingredients": ["flour", "sugar", "eggs"],
          "meal": "dessert",
          "prep_time": 60}
cookbook["Cake"] = recipe

recipe = {"ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
          "meal": "lunch",
          "prep_time": 15}
cookbook["Salad"] = recipe

info()
while (True):
    print("Please select an option:")
    index = input()
    if (index == '1'):
        print_all_names()
    if index == '2':
        print("Enter a name to search for")
        name = input()
        print_details(name)
    if index == '3':
        print("Enter a name to deleted")
        name = input()
        delete_recipe(name)
    if index == '4':
        add_recipe()
    if index == '5':
        exit(1)
    