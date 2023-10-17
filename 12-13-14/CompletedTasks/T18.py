counter = 0

def increment_counter():
    global counter
    counter +=1

def get_counter():
    global counter
    print(counter)


increment_counter()
increment_counter()
increment_counter()

get_counter()