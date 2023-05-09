import time as time
from recipe import Recipe
from datetime import datetime


class Book:
    def __init__(self, name="", creation_date=datetime.now(), l_update=datetime.now()):
        self.name = name
        self.creation_date = creation_date
        self.last_update = l_update
        self.recipes_list = {"starter": [], "lunch": [], "dessert": []}

    def __str__(self):
        txt = "%s is name of this Book\n" % self.name
        txt += "    Some details about %s,\n" % self.name
        txt += "    • creation_date     :" \
            + self.creation_date.strftime("%d/%m/%Y, %H:%M:%S") + "\n"
        txt += "    • last_update       :" \
            + self.last_update.strftime("%d/%m/%Y, %H:%M:%S") + "\n"
        txt += f"    • recipes_list      :{[ls for ls in self.recipes_list]}\n"
        return txt

    def get_recipe_by_name(self, name):
        """Prints a recipe with the name \texttt{name} and returns the instance"""
        for node in self.recipes_list:
            for recp in self.recipes_list[node]:
                if recp.name == name:
                    print(recp)
                    return recp
        print("this recipe name does not exist in the recipe list")
        return None

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        if recipe_type in self.recipes_list:
            lst = self.recipes_list[recipe_type]
            return lst
        print("this type is not supported")

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if type(recipe) != Recipe:
            pass
        for typee in self.recipes_list:
            if recipe.recipe_type == typee:
                for obj in self.recipes_list[typee]:
                    if id(recipe) == id(obj) or recipe.name == obj.name:
                        return
                self.recipes_list[typee].append(recipe)
                self.last_update = datetime.now()
