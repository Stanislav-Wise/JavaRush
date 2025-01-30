def password_protected(password):
    secret = "Это секретное сообщение."

    def inner(input_password):
        if input_password == password:
            return secret
        else:
            return "Доступ запрещён."

    return inner


access_control = password_protected("mypassword")
print(type(access_control))
print(access_control("wrongpassword"))
print(access_control("mypassword"))