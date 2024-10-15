import string

def Remove_matching_letter(l1,l2):
    l=[]
    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i] == l2[j]:
                c = l1[i]
                l1.remove(c)
                l2.remove(c)
                l = l1+["*"]+l2
                return [l,True]
    l = l1+ ["*"] +l2                
    return [l,False]                
    

s1 = input("Enter First name:")
s1 = s1.lower()
s1 = s1.replace(" ", "")

s2 = input("Enter Second name:")
s2 = s2.lower()
s2 = s2.replace(" ", "")

l1 = list(s1)
l2 = list(s2)

flag =True

while flag:
    return_list = Remove_matching_letter(l1,l2)
    con_list = return_list[0]
    flag = return_list[1]
    star_index = con_list.index("*")
    l1 = con_list[:star_index]
    l2 = con_list[(star_index+1):]

# print(l1)
# print(l2)
# l = l1 + l2
# print(l)

count = len(l1) + len(l2)
print(count)
result = ["Friendship","Love","Affection","Marriage","Enemy","Sister"]


while len(result) > 1:
    split_index = (count%len(result)) - 1
    if split_index>=0:
        right = result[split_index+1:]
        left = result[:split_index]
        result = right + left
    else:
        result = result[:len(result) - 1]

print("RelationShip Status:",result[0])
