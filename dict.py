# std ={
#     "name":'ashish',
#     "surname":"asgnihotri",
#     "sub":['eng','hindi']
# }
# print(std['sub'][1])
#
# d = dict(a=1,b=1)
# print(type(d))
import copy

# pairs =[("a",1),("b",2)]
# print(dict(pairs))

# keys=["a","b","c"]
# print(dict.fromkeys(keys,0))
#
# d =dict.fromkeys(["a","b"],[])
# d["a"].append(11)
# print(d)
# #accessin elements
# print(d.get("a"))
# print(d.get("x",0))

#adding and updating values

# d ={}
# d["a"]=10
# d["a"]=10
#
# d.update({"b":20,"v":4,"a":-1})
# # print(d)
#
# d.pop("a")
# # print(d)
# d.pop("x",None)
# del d["b"]
# d.clear()
# # print(d)

d = {"a": 1, "b": 2}
# for k,v in d.items():
#     print(k,v)
#
#
# for val in d.values():
#     print(val)

# for key in d():
#     print(key)

# sq ={i*i for i in range(5) if i%2==0}
# print(sq)


# std ={
#         1:{"name":"a","marks":90},
#         2:{"surname":"b","marks":80}
# }
# # print(std[2]["marks"])
# for id,info in std.items():
#     print(id,info)


# s= "banana"
freq ={}
#
# for ch in s:
#     freq[ch]=  freq.get(ch,0)+1
#
# print(freq)
# from collections import Counter
# Counter("banana")


# d1 = {"a": 1}
# d2 = {"b": 2}
#
# d =d1|d2
# print(d)
#
# d1 ={"a":[1,2]}
# d2 =d1.copy()
# print(d2,d1)
#
# d3= copy.deepcopy(d1)
# print(d3)

# for x in s:
#     freq[x]=freq.get(x,0)+1
# print(freq)

# for ch in s:
#     if freq[ch] == 1:
#         print(ch)
#         break

# d = "aabbcdde"
# freq={}
#
# for x in d:
#     freq[x]= freq.get(x,0)+1
#     print(freq)
#     if freq[x]==1:
#         print(x)
# d = [1, 2, 3, 2, 1, 4]
# for ch in d:
#     freq[ch] = freq.get(ch,0)+1
#     if freq[ch]>1:
#         print(ch,end=" ")

# d= {"a":1, "b":2}
# key="z"
# if key in d.keys():
#     print('True',key)
# else:
#     print('False',key)
# d1={"a":10,"b":20}
# d2={"b":30,"c":40}
#
# D3 =d1|d2
# print(D3)


# keys=["a","b","c"]
# values=[1,2,3]
# d={}
# for k,v in zip(keys,values):
#    d[k]=v
# print(d)

d = {'a': 1,'b': {'a': 2, 'c': 3},'d': [{'a': 4}, {'a': 5}]}
# def find_key(data, target):
#     if isinstance(data, dict):
#         for k, v in data.items():
#             if k == target:
#                 print(v)
#             find_key(v, target)
#
#     elif isinstance(data, list):
#         for item in data:
#             find_key(item, target)


# test_dict = {'gfg' : {'Manjeet' : 5, 'Himani' : 10},
#              'is' : {'Manjeet' : 8, 'Himani' : 9},
#              'best' : {'Manjeet' : 10, 'Himani' : 15 }}
# key = 'Himani'
# sum=0
# for k,v in test_dict.items():
#     if key in v:
#         sum+=v[key]
# print(sum,k)

# d = ['go', 'bat', 'me', 'eat', 'goal', 'boy', 'run']
# ch = ['e', 'o', 'b', 'a', 'm', 'g', 'l']
#
# for word in d:
#     valid =True
#     for c in set(word):
#         if word.count(c)>ch.count(c):
#             valid =False
#             break
#     if valid:
#         print(word)


# Input: "education"
# Output: {'a':1,'e':1,'i':1,'o':1,'u':1}


# ip  = "xyyz"
# freq ={}
#
# for ch in ip:
#     freq[ch] = freq.get(ch,0)+1
#     if freq[ch]>2:
#         print('NO')
#         break
# else:
#     print('yes')

# s1 = 'BOBthebuilder'
# s2 = 'fBoOkBIHnfndBthesibuishlider'
#
# for ch in s1:
#     if ch not in s2:
#         print('not')
#         break
# else:
#     print('pos')

test_dict = {"Gfg" : 4, "is" : 7, "Best" : 8, "for" : 6, "Geeks" : 10}