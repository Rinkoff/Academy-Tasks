data = [("Ivan",23),("George",19),("Kate",43)]

sorted_list = sorted(data, key=lambda x : x[1], reverse=True)

print(sorted_list)