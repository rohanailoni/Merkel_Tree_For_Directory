
from hashlib import *

def Hash_string(str):

    str=str.encode()
    

    return sha256(str).hexdigest()

class Tree_Node:

    def __init__(self):
        self.left=None
        self.right=None
        self.value=None
        self.hash=None

dic=["A","B","C","D"]


def draw_tree(dic):
    if len(dic)%2==0:
        arr=dic
        while len(arr)!=1:
            i=0
            temp1=[]
            while i<len(arr):
                temp=arr[i:i+2]
                if len(temp)==1:
                    s1=Tree_Node()
                    s1.left=temp[0]
                    s1.right=None
                    s1.hash=Hash_string(temp[0].hash)
                    s1.value=temp[0].value
                    i+=2
                    print(s1.value,s1.hash)
                    temp1.append(s1)
                if len(temp)==2:     

                    s1=Tree_Node()
                    s1.left=temp[0]
                    s1.right=temp[1]
                    print(temp[0].hash,temp[1].hash)
                    s1.hash=Hash_string(temp[0].hash+temp[1].hash)
                    s1.value=temp[0].value+temp[1].value
                    print(s1.value,s1.hash," At second pos")
                    i+=2
                    temp1.append(s1)
                else:
                    pass

            arr=temp1

        return arr[0]
        
    else:
        arr=dic
        while len(arr)!=1:
            i=0
            temp1=[]
            while i<len(arr):
                temp=arr[i:i+2]
                if len(temp)==1:
                    s1=Tree_Node()
                    s1.left=temp[0]
                    s1.right=None
                    s1.hash=Hash_string(temp[0].hash)
                    s1.value=temp[0].value
                    i+=2
                    print(s1.value,s1.hash)
                    temp1.append(s1)
                if len(temp)==2:     

                    s1=Tree_Node()
                    s1.left=temp[0]
                    s1.right=temp[1]
                    print(temp[0].hash,temp[1].hash)
                    s1.hash=Hash_string(temp[0].hash+temp[1].hash)
                    s1.value=temp[0].value+temp[1].value
                    print(s1.value,s1.hash," At second pos")
                    i+=2
                    temp1.append(s1)
                else:
                    pass

            arr=temp1

        return arr[0]


temp=[]
for i in dic:
    s=Tree_Node()
    s.left=None
    s.right=None
    s.hash=Hash_string(i)
    s.value=i
    temp.append(s)
dic=temp
tree=draw_tree(dic)

if tree.hash==tree1.hash:
    print("No change")

print(tree.hash)


# a1=Hash_string("A")

# a2=Hash_string("B")

# a3=Hash_string("C")

# a4=Hash_string("D")

# a5=Hash_string("E")

# a6=Hash_string(a1+a2)
# print("AB",a6)
# a7=Hash_string(a3+a4)
# print("CD",a7)
# a8=Hash_string(a5)
# print("E",a8)
# a9=Hash_string(a6+a7)
# print("ABCD",a9)
# a10=Hash_string(a8)
# print("E",a10)
# a11=Hash_string(a9+a10)
# print("ABCDE",a11)
# print(a11)
