for _ in range(int(input())):

    cube=[  ['w','w','w','w','w','w','w','w','w'], # 윗 쪽
            ['g','g','g','g','g','g','g','g','g'], # 왼 쪽  
            ['r','r','r','r','r','r','r','r','r'], # 앞 쪽
            ['b','b','b','b','b','b','b','b','b'], # 오른쪽
            ['o','o','o','o','o','o','o','o','o'], # 뒷 쪽
            ['y','y','y','y','y','y','y','y','y'] ]# 아랫쪽
    n=input()
    for a in list(map(str,input().split())):
        if a=='L-':
            cube[1][0],cube[1][1],cube[1][2],cube[1][3],cube[1][5],cube[1][6],cube[1][7],cube[1][8]=cube[1][2],cube[1][5],cube[1][8],cube[1][1],cube[1][7],cube[1][0],cube[1][3],cube[1][6]
            cube[0][0],cube[0][3],cube[0][6],cube[2][0],cube[2][3],cube[2][6],cube[5][6],cube[5][3],cube[5][0],cube[4][6],cube[4][3],cube[4][0]=cube[2][0],cube[2][3],cube[2][6],cube[5][6],cube[5][3],cube[5][0],cube[4][6],cube[4][3],cube[4][0],cube[0][0],cube[0][3],cube[0][6]
        if a=='L+':     
            cube[1][0],cube[1][1],cube[1][2],cube[1][3],cube[1][5],cube[1][6],cube[1][7],cube[1][8]=cube[1][6],cube[1][3],cube[1][0],cube[1][7],cube[1][1],cube[1][8],cube[1][5],cube[1][2]
            cube[0][0],cube[0][3],cube[0][6],cube[2][0],cube[2][3],cube[2][6],cube[5][6],cube[5][3],cube[5][0],cube[4][6],cube[4][3],cube[4][0]=cube[4][6],cube[4][3],cube[4][0],cube[0][0],cube[0][3],cube[0][6],cube[2][0],cube[2][3],cube[2][6],cube[5][6],cube[5][3],cube[5][0]
        if a=='U-':
            cube[0][0],cube[0][1],cube[0][2],cube[0][3],cube[0][5],cube[0][6],cube[0][7],cube[0][8]=cube[0][2],cube[0][5],cube[0][8],cube[0][1],cube[0][7],cube[0][0],cube[0][3],cube[0][6]
            cube[1][0],cube[1][1],cube[1][2],cube[4][2],cube[4][1],cube[4][0],cube[3][2],cube[3][1],cube[3][0],cube[2][0],cube[2][1],cube[2][2]=cube[4][2],cube[4][1],cube[4][0],cube[3][2],cube[3][1],cube[3][0],cube[2][0],cube[2][1],cube[2][2],cube[1][0],cube[1][1],cube[1][2]
        if a=='U+':
            cube[0][0],cube[0][1],cube[0][2],cube[0][3],cube[0][5],cube[0][6],cube[0][7],cube[0][8]=cube[0][6],cube[0][3],cube[0][0],cube[0][7],cube[0][1],cube[0][8],cube[0][5],cube[0][2]
            cube[1][0],cube[1][1],cube[1][2],cube[4][2],cube[4][1],cube[4][0],cube[3][2],cube[3][1],cube[3][0],cube[2][0],cube[2][1],cube[2][2]=cube[2][0],cube[2][1],cube[2][2],cube[1][0],cube[1][1],cube[1][2],cube[4][2],cube[4][1],cube[4][0],cube[3][2],cube[3][1],cube[3][0]
        if a=='R-':
            cube[3][0],cube[3][1],cube[3][2],cube[3][3],cube[3][5],cube[3][6],cube[3][7],cube[3][8]=cube[3][6],cube[3][3],cube[3][0],cube[3][7],cube[3][1],cube[3][8],cube[3][5],cube[3][2]
            cube[0][2],cube[0][5],cube[0][8],cube[2][2],cube[2][5],cube[2][8],cube[5][8],cube[5][5],cube[5][2],cube[4][8],cube[4][5],cube[4][2]=cube[4][8],cube[4][5],cube[4][2],cube[0][2],cube[0][5],cube[0][8],cube[2][2],cube[2][5],cube[2][8],cube[5][8],cube[5][5],cube[5][2]
        if a=='R+':
            cube[3][0],cube[3][1],cube[3][2],cube[3][3],cube[3][5],cube[3][6],cube[3][7],cube[3][8]=cube[3][2],cube[3][5],cube[3][8],cube[3][1],cube[3][7],cube[3][0],cube[3][3],cube[3][6]
            cube[0][2],cube[0][5],cube[0][8],cube[2][2],cube[2][5],cube[2][8],cube[5][8],cube[5][5],cube[5][2],cube[4][8],cube[4][5],cube[4][2]=cube[2][2],cube[2][5],cube[2][8],cube[5][8],cube[5][5],cube[5][2],cube[4][8],cube[4][5],cube[4][2],cube[0][2],cube[0][5],cube[0][8]
        if a=='D-':
            cube[5][0],cube[5][1],cube[5][2],cube[5][3],cube[5][5],cube[5][6],cube[5][7],cube[5][8]=cube[5][6],cube[5][3],cube[5][0],cube[5][7],cube[5][1],cube[5][8],cube[5][5],cube[5][2]
            cube[2][6],cube[2][7],cube[2][8],cube[1][6],cube[1][7],cube[1][8],cube[4][8],cube[4][7],cube[4][6],cube[3][8],cube[3][7],cube[3][6]=cube[3][8],cube[3][7],cube[3][6],cube[2][6],cube[2][7],cube[2][8],cube[1][6],cube[1][7],cube[1][8],cube[4][8],cube[4][7],cube[4][6]
        if a=='D+':
            cube[5][0],cube[5][1],cube[5][2],cube[5][3],cube[5][5],cube[5][6],cube[5][7],cube[5][8]=cube[5][2],cube[5][5],cube[5][8],cube[5][1],cube[5][7],cube[5][0],cube[5][3],cube[5][6]
            cube[2][6],cube[2][7],cube[2][8],cube[1][6],cube[1][7],cube[1][8],cube[4][8],cube[4][7],cube[4][6],cube[3][8],cube[3][7],cube[3][6]=cube[1][6],cube[1][7],cube[1][8],cube[4][8],cube[4][7],cube[4][6],cube[3][8],cube[3][7],cube[3][6],cube[2][6],cube[2][7],cube[2][8]

        if a=='F-':
            cube[2][0],cube[2][1],cube[2][2],cube[2][3],cube[2][5],cube[2][6],cube[2][7],cube[2][8]=cube[2][2],cube[2][5],cube[2][8],cube[2][1],cube[2][7],cube[2][0],cube[2][3],cube[2][6]
            cube[0][6],cube[0][7],cube[0][8],cube[3][2],cube[3][5],cube[3][8],cube[5][8],cube[5][7],cube[5][6],cube[1][8],cube[1][5],cube[1][2]=cube[3][2],cube[3][5],cube[3][8],cube[5][8],cube[5][7],cube[5][6],cube[1][8],cube[1][5],cube[1][2],cube[0][6],cube[0][7],cube[0][8]
        if a=='F+':
            cube[2][0],cube[2][1],cube[2][2],cube[2][3],cube[2][5],cube[2][6],cube[2][7],cube[2][8]=cube[2][6],cube[2][3],cube[2][0],cube[2][7],cube[2][1],cube[2][8],cube[2][5],cube[2][2]
            cube[0][6],cube[0][7],cube[0][8],cube[3][2],cube[3][5],cube[3][8],cube[5][8],cube[5][7],cube[5][6],cube[1][8],cube[1][5],cube[1][2]=cube[1][8],cube[1][5],cube[1][2],cube[0][6],cube[0][7],cube[0][8],cube[3][2],cube[3][5],cube[3][8],cube[5][8],cube[5][7],cube[5][6]
        if a=='B-':
            cube[4][0],cube[4][1],cube[4][2],cube[4][3],cube[4][5],cube[4][6],cube[4][7],cube[4][8]=cube[4][6],cube[4][3],cube[4][0],cube[4][7],cube[4][1],cube[4][8],cube[4][5],cube[4][2]
            cube[0][0],cube[0][1],cube[0][2],cube[3][0],cube[3][3],cube[3][6],cube[5][2],cube[5][1],cube[5][0],cube[1][6],cube[1][3],cube[1][0]=cube[1][6],cube[1][3],cube[1][0],cube[0][0],cube[0][1],cube[0][2],cube[3][0],cube[3][3],cube[3][6],cube[5][2],cube[5][1],cube[5][0]
        
        if a=='B+':
            cube[4][0],cube[4][1],cube[4][2],cube[4][3],cube[4][5],cube[4][6],cube[4][7],cube[4][8]=cube[4][2],cube[4][5],cube[4][8],cube[4][1],cube[4][7],cube[4][0],cube[4][3],cube[4][6]
            cube[0][0],cube[0][1],cube[0][2],cube[3][0],cube[3][3],cube[3][6],cube[5][2],cube[5][1],cube[5][0],cube[1][6],cube[1][3],cube[1][0]=cube[3][0],cube[3][3],cube[3][6],cube[5][2],cube[5][1],cube[5][0],cube[1][6],cube[1][3],cube[1][0],cube[0][0],cube[0][1],cube[0][2]
            
        #print(' '*3+cube[0][0]+cube[0][1]+cube[0][2])
        #print(' '*3+cube[0][3]+cube[0][4]+cube[0][5])
        #print(' '*3+cube[0][6]+cube[0][7]+cube[0][8])
        #print(cube[1][0]+cube[1][1]+cube[1][2]+cube[2][0]+cube[2][1]+cube[2][2]+cube[3][2]+cube[3][1]+cube[3][0]+cube[4][2]+cube[4][1]+cube[4][0])
        #print(cube[1][3]+cube[1][4]+cube[1][5]+cube[2][3]+cube[2][4]+cube[2][5]+cube[3][5]+cube[3][4]+cube[3][3]+cube[4][5]+cube[4][4]+cube[4][3])
        #print(cube[1][6]+cube[1][7]+cube[1][8]+cube[2][6]+cube[2][7]+cube[2][8]+cube[3][8]+cube[3][7]+cube[3][6]+cube[4][8]+cube[4][7]+cube[4][6])
        
        #print(' '*3+cube[5][6]+cube[5][7]+cube[5][8])
        #print(' '*3+cube[5][3]+cube[5][4]+cube[5][5])
        #print(' '*3+cube[5][0]+cube[5][1]+cube[5][2])
        #print()
    print(cube[0][0]+cube[0][1]+cube[0][2])
    print(cube[0][3]+cube[0][4]+cube[0][5])
    print(cube[0][6]+cube[0][7]+cube[0][8])
