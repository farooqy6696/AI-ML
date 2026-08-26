#13. Secure Login System (Decorators)

logged_in = True


def login_required(func):

    def wrapper():
        if logged_in:
            func()
        else:
            print("Access Denied! Please Login.")

    return wrapper


@login_required
def view_balance():
    print("Balance = ₹50,000")


view_balance()