from one_d_settings import length,rule, first


matrix=[0 for i in range(length)]
matrix[length//2]=1


with open('E:\\coding\\game_of_life\\one_d\\result.txt','w+') as f:
    for i in range(first):
        
        new_mat=[]
        to_pr=''
        for j in matrix:
            to_pr+='  ' if j==0 else '[]'
        print(to_pr)
        f.write(f'{to_pr}\n')
        for x,i in enumerate(matrix):
            cur_rules=[]
            cur_rules.append(matrix[x-1 if x!=0 else x])
            cur_rules.append(matrix[x])
            cur_rules.append(matrix[x+1 if x+1<length else x])
            new_mat.append(rule[tuple(cur_rules)])
        matrix=new_mat

