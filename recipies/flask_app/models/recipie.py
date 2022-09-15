from flask_app.config.mysqlconnection import connectToMySQL

class Recipies:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.instructions = data["instructions"]
        self.nutrients = data["nutrients"]
        self.cook = data["cook"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = 0

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL("recipesUsers").query_db(query)

        recipies = []
        for result in results:
            one_instance = cls(result)
            recipies.append(one_instance)
        return recipies

    @classmethod
    def save(cls,data):
        query = "INSERT INTO recipes (name, instructions,nutrients,cook ,created_at, updated_at) VALUE (%(name)s, %(instructions)s,%(nutrients)s,%(cook)s, NOW(), NOW())" 

        recipe_id = connectToMySQL("recipesUsers").query_db(query,data)

        return recipe_id
    
    @classmethod
    def edit(cls, data):
        query = "UPDATE recipes SET name = %(name)s, instructions = %(instructions)s, nutrients = %(nutrients)s, cook = %(cook)s  WHERE id = %(id)s;"
        recipe_id = connectToMySQL("recipesUsers").query_db(query,data)
        return recipe_id
