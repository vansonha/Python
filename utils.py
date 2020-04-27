def add(x,y):
    return x+y

def remove_spaces(data):
    return data.replace(" ","")

def validation_email(email):
    return True if '@' in email else False