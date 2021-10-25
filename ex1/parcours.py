#!/usr/bin/env python3

def district_value(list, pos):
    if (abs(list[0] - pos) > abs(list[-1] - pos)):
        return abs(list[0] - pos) / len(list)
    return abs(list[-1] - pos) / len(list)

def go_up(lists, i, pos):
    if i == 0:
        return True
    elif i == len(lists):
        return False
    elif district_value(lists[i-1], pos) > district_value(lists[i], pos):
        return True
    return False

def get_neighborhood(list_house, max_size):
    sub_list = []
    current = []
    old = list_house[0]
    for house in list_house:
        if (old + max_size) < house or (old < 0 and house > 0):
            sub_list.append(current)
            current = []
        current.append(house)
        old = house
    sub_list.append(current)
    return sub_list

def print_lists(lists):
    for list in lists:
        print("===")
        print(list)
        print("\n")

def parcours(list_house):
    result = []
    list_house.sort()
    #print((list_house[-1] - list_house[0]) * 0.0025)
    sub_list = get_neighborhood(list_house, (list_house[-1] - list_house[0]) * 0.0025)
    #print_lists(sub_list)
    i = 0
    pos = 0
    while sub_list[i][0] < 0:
        i+=1
    while len(sub_list) != 1:
        if go_up(sub_list,i,pos):
            for house in sub_list[i]:
                result.append(house)
            pos = sub_list[i][-1]
            sub_list.pop(i)
        else:
            j = len(sub_list[i-1])
            while j > 0:
                result.append(sub_list[i-1][j-1])
                j -= 1
            pos = sub_list[i-1][0]
            sub_list.pop(i-1)
            i -= 1
    if sub_list[0][0] >= pos:
        for house in sub_list[0]:
            result.append(house)
    else:
        j = len(sub_list[0])
        while j > 0:
            result.append(sub_list[0][j-1])
            j -= 1
    return result
