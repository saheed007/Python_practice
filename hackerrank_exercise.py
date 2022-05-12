name_score_pair=[]
for i in range(int(input())):
    name = input("name: ")
    score = float(input("score: "))
    name_score_pair.append([name, score])
##print(name_score_pair)

score_list =[]
for i in range(len(name_score_pair)):
    score_list.append(name_score_pair[i][1])
score_list.sort()
print('score_list:',score_list,'\n')


mosts= score_list.count(min(score_list))
print(mosts)
score_list = score_list[mosts:]
print(score_list)
lowests=[]
for y,z in name_score_pair:
    if z == score_list[0]:
        lowests.append(y)
        lowests.sort()
for w in lowests:
    print(w)
    

# test cases
#  ['Harsh', 20],['Beria',20],['Varun', 19],['Kakunami',19],['Vikas',21]
#  ['a',2],['b',5],['c',5],['mary',3],['Harry',3],['Barry',3],['f',1]

