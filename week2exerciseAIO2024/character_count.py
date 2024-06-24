string = input()
def count(string):
    list_string = list(string)
    dict_string = {}
    for index in list_string:
        if index not in dict_string:#check if index not in , then we creat the new one
            dict_string[index] = 1
        else:
            dict_string[index] +=1
    return dict_string
print(count(string))