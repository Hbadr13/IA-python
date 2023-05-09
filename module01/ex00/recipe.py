class Recipe:
    def __init__(self, name="", lvl=-1, cook_t=-1, ings=list, dscp="", r_type=""):
        self.name = name
        self.cooking_lvl = lvl if lvl in range(1, 6) else -1
        self.cooking_time = cook_t if cook_t > 0 else -1
        self.ingredients = ings if type(ings) == list else ""
        self.description = dscp
        self.recipe_type = r_type if r_type in [
            "starter", "lunch", "dessert"] else ""
        self.recipeValed = True
        if self.name == "" or self.cooking_lvl == -1 or self.cooking_time == -1 or self.ingredients == "" or self.recipe_type == "":
            self.recipeValed = False
            print("I Cannot create this recipe")

    def __str__(self):
        txt = "%s is name of this recipe\n"     % self.name
        txt += "    Some details about %s,\n"     % self.name
        txt += "    • Cooking_lvl   : %d,\n"     % self.cooking_lvl
        txt += "    • Cooking_time  : %d m,\n"   % self.cooking_time
        txt+= f"    • Ingredients   : {self.ingredients},\n"
        txt += "    • description   : %s,\n"     % self.description
        txt += "    • recipe_type   : %s,\n"     %self.recipe_type
        return txt
