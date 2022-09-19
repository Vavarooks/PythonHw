from flask_app.config.mysqlconnection import connectToMySQL
import re	# the regex module
from flask import Flask, render_template, redirect, request, session, flash
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Users:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data['password']
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def save(cls,data):
        query = "INSERT INTO user (first_name, last_name, email, password, created_at, updated_at) VALUE (%(first_name)s,%(last_name)s,%(email)s,%(password)s, NOW(), NOW())" 

        user_id = connectToMySQL("users_rg").query_db(query,data)

        return user_id

    @classmethod
    def find_one_by_email(cls,data):
        query = "SELECT * FROM user WHERE email=%(email)s;"

        results = connectToMySQL("users_rg").query_db(query,data)

        if len(results) == 0:
            return False
        one_instance = cls(results[0])

        return one_instance

    @staticmethod
    def validate(data):
        is_valid = True
        has_special_char =  False

        if data["password"] != data["password_confirm"]:
            flash("passwords must match!")
            is_valid = False

        for letter in data["password"]:
            if letter in ["!","@","#","$","%","^","&","*"]:
                has_special_char = True
            if not has_special_char:
                flash("Needs a special character!")
                is_valid = False

        if len(data['first_name']) < 1:
            flash("More than one letter please!")
            is_valid = False
        if len(data['last_name']) < 1:
            flash("More than one letter please!")
            is_valid = False
        if len(data['email']) < 1:
            flash("More than one letter please!")
            is_valid = False
        if len(data['password']) < 1:
            flash("More than one charater please!")
            is_valid = False

        return is_valid

    @staticmethod
    def validate_user( users ):
        is_valid = True
        if not EMAIL_REGEX.match(users['email']): 
            flash("Invalid email address!")
            is_valid = False
        if not (users['email']):
            flash("Email cannot be blank!", 'email')
        return is_valid
