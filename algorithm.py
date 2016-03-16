#/usr/bin/env python
#-*- coding:utf-8 -*-

def bubble_sort(list):
    len_list = len(list)
    if len_list<2:
        return list
    for i in range(0,len_list):
        for j in range(0,len_list-i-1):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
    return list



if __name__=="__main__":
    list=[2,4,90,40,35,84,82,76,92,101]
    print(bubble_sort(list))
