# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 08:21:03 2022
purpose : Flames calculator
@author: Joshua
"""
def result(num):
    #num=int(input())
    a=['F','L','A','M','E','S']

    if num%6==0:
        a6=a[0:-1]
    #print(a6)
    else:
        b=num%6
        a6=a[b:]
        if a[0:b-1]!=[]:
            for i in a[0:b-1]:
                a6.append(i)
    #print(a6)

    if num%5==0:
        a5=a6[0:-1]
        #print(a5)  
    else:
        b=num%5
        a5=a6[b:]
        if a6[0:b-1]!=[]:
            for i in a6[0:b-1]:
                a5.append(i)
    #print(a5)
    
    if num%4==0:
        a4=a5[0:-1]
        #print(a4)
    else:
        b=num%4
        a4=a5[b:]
        if a5[0:b-1]!=[]:
            for i in a5[0:b-1]:
                a4.append(i)
    #print(a4)

    if num%3==0:
        a3=a4[0:-1]
    #print(a3)
    else:
        b=num%3
        a3=a4[b:]
        if a4[0:b-1]!=[]:
            for i in a4[0:b-1]:
                a3.append(i)
    #print(a3)

    if num%2==0:
        final=a3[0]
        return final
    else:
        final=a3[1]
        return final
#print(result(1))