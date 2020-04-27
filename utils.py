#add funtion
def add(x,y):
    return x+y+1

def remove_spaces(data):
    return data.replace(" ","")

def validation_email(email):
    return True if '@' in email else False