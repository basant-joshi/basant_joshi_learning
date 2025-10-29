##########################################################################
'''
Two Sum Problem
coding 1- # x = [7, 2, 3, 8, 9] 
# target = 12, 
# o/p =[3,9] 
# find 2 elements which add equal to target
'''
# nums = [7, 2, 3, 8, 9,6,15]
# target = 9
# listt = []
# seen = set()
# for n in nums:
#     complement = target - n
#     if complement in seen:
#         listt.append((complement,n))
#     seen.add(n)
# print(listt)

##########################################################################
'''
First palindrom in the given string
coding 2 - 
s="babad" 
o/p = bab means first palindrome
'''

# s = "malyalambabadjahaj"
# s_len = len(s)

# for i in range(s_len):
#     for j in range(i+1,s_len+1):
#         sub = s[i:j]
#         if sub == sub[::-1] and len(sub) > 1:
#             print(sub)
#             exit()  #just in case if you want to print first palinadrom than put exit() instead of break

##########################################################################
'''
Find rank for the given list/array
input =  [10,20,30,40,10,20]
output = [1,2,3,4,1,2]
'''

# nums = [10,20,30,40,10,20]
# sorted_set = sorted(set(nums))
# rank_dict = {num:rank+1 for rank,num in enumerate(sorted_set)}
# rank_list = [rank_dict[i] for i in nums]
# print(rank_list)

##########################################################################
'''Flatten a list
input = [[1,2],[3,4],[5,6]]
output = [1,2,3,4,5,6]
'''
# listt = [[1,2],[3,4],[5,6]]
# new_list = [x for i in listt for x in i]
# print(new_list)
##########################################################################
'''
Flatten a list
input = [1,[2,[3,4],5]]
output = [1,2,3,4,5]
'''

# def flatten(lst):
#     flat = []
#     for item in lst:
#         if isinstance(item,list):
#             flat.extend(flatten(item))
#         else:
#             flat.append(item)
#     return flat
# listt = [1,[2,[3,4],[5,[6,7,8,[9,[10,11,[12,13]]]]]]]   
# print(flatten(listt))
##########################################################################
'''
Multithreading
'''
# import threading,time

# def print_name():
#     for i in ["A","B","C","D","E"]:
#         print(i)
#         time.sleep(1)


# def print_number():
#     for i in range(10):
#         print(i)

# t1 = threading.Thread(target=print_name)
# t2 = threading.Thread(target=print_number)

# t1.start()
# t2.start()

# t1.join()
# t2.join()
##########################################################################
'''
Exception handling
'''
# s = "Basant"
# try:
#     s[0] = "B"
#     print(s)
# except Exception as e:
#     print("Can not make any change in immutable string ", e)
# finally:
#     print("Did exception handling")
##########################################################################
'''
Generators
'''
# def print_name():
#     for i in range(10):        
#         yield i
    
# gen = print_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
##########################################################################
'''
Iterator
'''
listt = [10,20,30]
it = iter(listt)

print(next(it))
print(next(it))
print(next(it))
print(next(it))
##########################################################################
'''
Bubble sort
'''
# listt = [1,3,2,1,0,5,8]

# l_len = len(listt)
# for i in range(l_len):
#     for j in range(0,l_len-i-1):
#         if listt[j] > listt[j+1]:
#             listt[j],listt[j+1] = listt[j+1],listt[j]
# print("Final list= ", listt)
##########################################################################