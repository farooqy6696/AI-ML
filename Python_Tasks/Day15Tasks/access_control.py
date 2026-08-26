#8. Decorator-based Access Control
#Scenario: Restrict access to certain functions.
#Task:
# ● Create a decorator to check user role
# ● Use condition inside decorator
# ● Apply decorator to multiple functions
# ● Store roles in a dictionary

# Store user roles in a dictionary

user_roles = {
    "Rahul": "admin",
    "Priya": "user",
    "Arun": "manager"
}


# Create decorator
def check_role(required_role):

    def decorator(function):

        def wrapper(username):

            if user_roles.get(username) == required_role:
                return function(username)

            else:
                print("Access denied for", username)

        return wrapper

    return decorator


# Admin function
@check_role("admin")
def delete_user(username):
    print("User deleted by", username)


# Manager function
@check_role("manager")
def view_reports(username):
    print("Reports opened by", username)


# Test the functions

delete_user("Rahul")
delete_user("Priya")

view_reports("Arun")
view_reports("Rahul")