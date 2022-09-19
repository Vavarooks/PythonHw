from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import Users
class Recipies:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.instructions = data["instructions"]
        self.nutrients = data["nutrients"]
        self.cook = data["cook"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = None
        self.users_id = data["users_id"]

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes JOIN users ON recipes.users_id = users.id;"
        results = connectToMySQL("recipesUsers").query_db(query)

        recipies = []
        for result in results:
            one_instance = cls(result)

            user_data = {
                "id" : result["users.id"],
                "first_name" : result["first_name"],
                "last_name" : result["last_name"],
                "email" : result["email"],
                "password" : result["password"],
                "created_at" : result["users.created_at"],
                "updated_at" : result["users.updated_at"],
            }
            one_instance.user_id = Users(user_data)
            recipies.append(one_instance)
        print(one_instance)
        return recipies

    @classmethod
    def save(cls,data):
        query = "INSERT INTO recipes (name, instructions,nutrients,cook ,created_at, updated_at, users_id) VALUE (%(name)s, %(instructions)s,%(nutrients)s,%(cook)s, NOW(), NOW(),%(users_id)s)" 

        recipe_id = connectToMySQL("recipesUsers").query_db(query,data)

        return recipe_id

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM recipes WHERE id = %(id)s"
        exsponge = connectToMySQL("recipesUsers").query_db(query,data)

        return exsponge

    @classmethod
    def edit(cls, data):
        query = "UPDATE recipes SET name = %(name)s, instructions = %(instructions)s, nutrients = %(nutrients)s, cook = %(cook)s  WHERE id = %(id)s;"
        recipe_id = connectToMySQL("recipesUsers").query_db(query,data)
        return recipe_id

    @classmethod
    def veiw_one(cls,data):
        query = "SELECT * FROM recipes WHERE recipes.id = %(id)s;"
        single_recipe_id = connectToMySQL("recipesUsers").query_db(query,data)
        one_instance = cls(single_recipe_id[0])
        return one_instance
