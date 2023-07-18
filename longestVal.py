def longest_value(dict):
    new_dict = {}
    for key,value in dict.items():
        new_dict[value] = len(value)
    val = 0
    for key,value in new_dict.items():
        if value > val:
            val = value
    return val


print(longest_value({"fruit":"appldtadhe","color":"yellow"}))