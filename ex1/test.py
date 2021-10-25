#!/usr/bin/env python3

def ref_parcours(list):
    print("list length :", len(list))
    list.sort()
    result = []
    pos = 0
    i = 0
    while list[i] < pos :
        i +=1
    while len(list) != 1:
        if i == 0 :
            pos = list[i]
            list.pop(i)
        elif i == len(list):
            pos = list[i-1]
            list.pop(i-1)
            i -= 1
        elif (pos - list[i-1]) < (list[i] - pos):
            pos = list[i-1]
            list.pop(i-1)
            i -= 1
        else:
            pos = list[i]
            list.pop(i)
        result.append(pos)
    result.append(list[0])
    return result

def average_wait(list):
    time = 0
    dist = 0
    pos = 0

    for house in list:
        dist += abs(house - pos)
        time += dist
        pos = house
    print("list length :", len(list))
    print("total time :", time)
    time = time / len(list)
    
    ref_list = ref_parcours(list)
    ref_time = 0
    dist = 0
    pos = 0

    for house in ref_list:
        dist += abs(house - pos)
        ref_time += dist
        pos = house
    print("ref list length :", len(ref_list))
    print("ref total time :", ref_time)
    ref_time = ref_time / len(ref_list)
    
    print("the average time wait for your solution is :", time)
    print("the average time wait for the reference solution is :", ref_time)
    if (time < 0.9 * ref_time):
        print("\033[32mvous faites {:.2f} %  du temps d'attente de l'algo de reference\033[0m".format((time/ref_time)*100).rstrip("0"))
        print("\033[32mYour solution is ok for the project.\033[0m")
    else:
        print("\033[31mvous faites {:.2f} %  du temps d'attente de l'algo de reference\033[0m".format((time/ref_time)*100).rstrip("0"))
        print("\033[31mYour solution isn't enough efficient.\033[0m")
    