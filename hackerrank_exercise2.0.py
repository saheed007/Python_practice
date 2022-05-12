###############################################################################
#           SOLUTION 1

name_score_pair=[]
for _ in range(int(input())):
    while True:
        try:
            name_score_pair.append([input("name: "), float(input("score: "))])
            break
        except:
            print('score must be a number! enter name-value pair again')

lowests = sorted(list(set([y for x,y in name_score_pair])))[1]
result=[a for a,b in sorted(name_score_pair) if b == lowests]
for w in result:
    print(f"the person with the second lowest score is {w}")
    
###############################################################################
#          SOLUTION 2

marksheet = []
for _ in range(0,int(input())):
    marksheet.append([input(), float(input())])
    
second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))

###############################################################################

# test cases (name-score pairs)
# (1) ---    ['Harsh', 20],['Beria',20],['Varun', 19],['Kakunami',19],['Vikas',21]
# (2) ---    ['a',2],['b',5],['c',5],['mary',3],['Harry',3],['Barry',3],['f',1]
