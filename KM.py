# FDC KM 0.1.1
#

'''
1.ustal ilość zmiennych
2.pobierz iloczyny pełne równe 1
3.zbuduj tablicę
4.wypełnij tablicę
5.POGRUPUJ
6.uporządkuj&usuń duplikaty
7.odczytaj & wypisz'''

ST = [0,1,3,2]
TK = []
TT = []; rTT=[]

def Siatka(n):      #KK
    if(n==8):   return (4,4,4,4);
    elif(n==7): return (4,4,4,2);
    elif(n==6): return (4,4,4,1);
    elif(n==5): return (4,4,2,1);
    elif(n==4): return (4,4,1,1);
    elif(n==3): return (4,2,1,1);
    elif(n==2): return (2,2,1,1);
    elif(n==1): return (2,1,1,1);
    elif(n==0): return (1,1,1,1);

def Wypisz(TT):
    for l in range(len(TT)):
        for k in range(len(TT[l])):
            for j in range(len(TT[l][k])):
                for i in range(len(TT[l][k][j])):
                    print(TT[l][k][j][i][0],end=' ')
                print()
            print()
        print()

def Trans(TK):
    global W,X,Y,Z
    TT=[]; n=0
    for l in range(W):
        xyz = []
        for k in range(Z):
            xy = []
            for j in range(Y):
                xx = []
                for i in range(X):
                    xx.append([TK[n][0],TK[n][5],TK[n][6]])
                    n+=1
                    if(i==3): xx[3],xx[2]=xx[2],xx[3];
                xy.append(xx)
                if(j==3): xy[3],xy[2]=xy[2],xy[3];
            xyz.append(xy)
            if(k==3): xyz[3],xyz[2]=xyz[2],xyz[3];
        TT.append(xyz)
        if(l==3): TT[3],TT[2]=TT[2],TT[3];
    return TT;

def Trans_Rev(TK):
    global W,X,Y,Z
    TT=[]; n=0
    for i in range(X):
        wyz = []
        for j in range(Y):
            wz = []
            for k in range(Z):
                ww = []
                for l in range(W):
                    e = []
                    ww.append(e)
                wz.append(ww)
            wyz.append(wz)
        TT.append(wyz)
        
    '''for i in range(X):
        xyz = []
        for j in range(Y):
            xy = []
            for k in range(Z):
                xx = []
                for l in range(W):
                    xx.append([TK[n][0],TK[n][5],TK[n][6]])
                    n+=1
                    if(l==3): xx[3],xx[2]=xx[2],xx[3];
                xy.append(xx)
                if(k==3): xy[3],xy[2]=xy[2],xy[3];
            xyz.append(xy)
            if(j==3): xyz[3],xyz[2]=xyz[2],xyz[3];
        TT.append(xyz)
        if(i==3): TT[3],TT[2]=TT[2],TT[3];
    return TT;'''

    for i in range(X):
        for j in range(Y):
            for k in range(Z):
                for l in range(W):
                    TT[i][j][k][l] = TK[l][k][j][i]
    return TT;
                    

def Near(kom,TK=TK,TT=TT):
    global W,X,Y,Z
    print(TK[kom])

    tx = TK[kom][1]; ty = TK[kom][2]
    tz = TK[kom][3]; tw = TK[kom][4]

    print(TT[tw][tz][ty][tx-1]); print(TT[tw][tz][ty][(tx+1)%X])
    print(TT[tw][tz][ty-1][tx]); print(TT[tw][tz][(ty+1)%Y][tx])
    print(TT[tw][tz-1][ty][tx]); print(TT[tw][(tz+1)%Z][ty][tx])
    print(TT[tw-1][tz][ty][tx]); print(TT[(tw+1)%W][tz][ty][tx])

def Lista(TK,TT):
    global X,Y,Z,W;
    lista = []
    for i in range(len(TK)):
        x=TK[i][1]
        y=TK[i][2]
        z=TK[i][3]
        w=TK[i][4]
        if(TT[x][y][z][w][0]!=0):
            #1D
            pillz_x = 0; pillz_y = 0;
            pillz_z = 0; pillz_w = 0;
            kij_x = 0; kij_y = 0;
            kij_z = 0; kij_w = 0;
            #2D
            kafel_xy= 0; kafel_xz= 0; kafel_xw= 0;
            kafel_yz= 0; kafel_yw= 0;
            kafel_zw= 0;
            lufa_xy = 0; lufa_xw = 0; lufa_xz = 0;
            lufa_yx = 0; lufa_yz = 0; lufa_yw = 0;
            lufa_zx = 0; lufa_zy = 0; lufa_zw = 0;
            lufa_wy = 0; lufa_wx = 0; lufa_wz = 0;
            pol_xy = 0; pol_xw = 0; pol_xz = 0;
            pol_yw = 0; pol_yz = 0;
            pol_zw = 0;
            #3D
            kost_xyz = 0; kost_xzw = 0; 
            kost_yzw = 0; kost_xyw = 0;
            dział_xyz= 0; dział_xzw= 0; dział_xyw= 0;
            dział_yxz= 0; dział_yxw= 0; dział_yzw= 0;
            dział_zxy= 0; dział_zyw= 0; dział_zxw= 0;
            dział_wxy= 0; dział_wyz= 0; dział_wxz= 0;
            kana_xyz = 0; kana_xyw = 0;
            kana_xzy = 0; kana_xzw = 0;
            kana_xwz = 0; kana_xwy = 0;
            kana_yzx = 0; kana_yzw = 0;
            kana_ywx = 0; kana_ywz = 0;
            kana_zwx = 0; kana_zwy = 0;
            szsc_xyz = 0; szsc_xzw = 0;
            szsc_xyw = 0; szsc_yzw = 0;
            #4D
            plazm_x = 0; plazm_y = 0;
            plazm_z = 0; plazm_w = 0;
            burg_xy = 0; burg_xw = 0; burg_xz = 0;
            burg_yw = 0; burg_yz = 0;
            burg_zw = 0;
            taxi_xyz= 0; taxi_yzw= 0;
            taxi_xzw= 0; taxi_xyw= 0;
            m_tese = 0; tesserakt= 0;
            
            #sprawdzanie pastylek i kijków x4
            if(TT[(x+1)%X][y][z][w][0]!=0):
                pillz_x = 1
                if(TT[(x+2)%X][y][z][w][0]!=0 and
                   TT[(x+3)%X][y][z][w][0]!=0): kij_x=1
            if(TT[x][(y+1)%Y][z][w][0]!=0):
                pillz_y = 1
                if(TT[x][(y+2)%Y][z][w][0]!=0 and
                   TT[x][(y+3)%Y][z][w][0]!=0): kij_y=1   
            if(TT[x][y][(z+1)%Z][w][0]!=0):
                pillz_z = 1
                if(TT[x][y][(z+2)%Z][w][0]!=0 and
                   TT[x][y][(z+3)%Z][w][0]!=0): kij_z=1
            if(TT[x][y][z][(w+1)%W][0]!=0):
                pillz_w = 1
                if(TT[x][y][z][(w+2)%W][0]!=0 and
                   TT[x][y][z][(w+3)%W][0]!=0): kij_w=1

            #sprawdzanie kafelek x6
            if(pillz_x and pillz_y):
                if(TT[(x+1)%X][(y+1)%Y][z][w][0]!=0):
                    kafel_xy = 1
            if(pillz_x and pillz_z):
                if(TT[(x+1)%X][y][(z+1)%Z][w][0]!=0):
                    kafel_xz = 1
            if(pillz_x and pillz_w):
                if(TT[(x+1)%X][y][z][(w+1)%W][0]!=0):
                    kafel_xw = 1

            if(pillz_y and pillz_z):
                if(TT[x][(y+1)%Y][(z+1)%Z][w][0]!=0):
                    kafel_yz = 1
            if(pillz_y and pillz_w):
                if(TT[x][(y+1)%Y][z][(w+1)%W][0]!=0):
                    kafel_yw = 1

            if(pillz_z and pillz_w):
                if(TT[x][y][(z+1)%Z][(w+1)%W][0]!=0):
                    kafel_zw = 1
                    
            #sprawdzanie kostek x4
            if(kafel_xy and kafel_yz and kafel_xz):
                if(TT[(x+1)%X][(y+1)%Y][(z+1)%Z][w][0]!=0):
                    kost_xyz = 1
                    
            if(kafel_xy and kafel_yw and kafel_xw):
                if(TT[(x+1)%X][(y+1)%Y][z][(w+1)%W][0]!=0):
                    kost_xyw = 1
            if(kafel_xw and kafel_zw and kafel_xz):
                if(TT[(x+1)%X][y][(z+1)%Z][(w+1)%W][0]!=0):
                    kost_xzw = 1
            if(kafel_yw and kafel_yz and kafel_zw):
                if(TT[x][(y+1)%Y][(z+1)%Z][(w+1)%W][0]!=0):
                    kost_yzw = 1

            #sprawdzanie małego teseraktu x1
            if(kost_xyz and kost_xyw and kost_xzw and kost_yzw):
                if(TT[(x+1)%X][(y+1)%Y][(z+1)%Z][(w+1)%W][0]!=0):
                   m_tese=1

            #sprawdzanie luf x3x4
            if(kafel_xy and kij_x):
                   if(TT[(x+2)%X][(y+1)%Y][z][w][0]!=0 and
                      TT[(x+3)%X][(y+1)%Y][z][w][0]!=0): lufa_xy=1
            if(kafel_xz and kij_x):
                   if(TT[(x+2)%X][y][(z+1)%Z][w][0]!=0 and
                      TT[(x+3)%X][y][(z+1)%Z][w][0]!=0): lufa_xz=1
            if(kafel_xw and kij_x):
                   if(TT[(x+2)%X][y][z][(w+1)%W][0]!=0 and
                      TT[(x+3)%X][y][z][(w+1)%W][0]!=0): lufa_xw=1

            if(kafel_xy and kij_y):
                   if(TT[(x+1)%X][(y+2)%Y][z][w][0]!=0 and
                      TT[(x+1)%X][(y+3)%Y][z][w][0]!=0): lufa_yx=1
            if(kafel_yz and kij_y):
                   if(TT[x][(y+2)%Y][(z+1)%Z][(w+0)%W][0]!=0 and
                      TT[x][(y+3)%Y][(z+1)%Z][(w+0)%W][0]!=0): lufa_yz=1
            if(kafel_yw and kij_y):
                   if(TT[x][(y+2)%Y][(z+0)%Z][(w+1)%W][0]!=0 and
                      TT[x][(y+3)%Y][(z+0)%Z][(w+1)%W][0]!=0): lufa_yw=1

            if(kafel_xz and kij_z):
                   if(TT[(x+1)%X][(y+0)%Y][(z+2)%Z][(w+0)%W][0]!=0 and
                      TT[(x+1)%X][(y+0)%Y][(z+3)%Z][(w+0)%W][0]!=0): lufa_zx=1
            if(kafel_yz and kij_z):
                   if(TT[x][(y+1)%Y][(z+2)%Z][(w+0)%W][0]!=0 and
                      TT[x][(y+1)%Y][(z+3)%Z][(w+0)%W][0]!=0): lufa_zy=1
            if(kafel_zw and kij_z):
                   if(TT[x][(y+0)%Y][(z+2)%Z][(w+1)%W][0]!=0 and
                      TT[x][(y+0)%Y][(z+3)%Z][(w+1)%W][0]!=0): lufa_zw=1

            if(kafel_xw and kij_w):
                   if(TT[(x+1)%X][(y+0)%Y][(z+0)%Z][(w+2)%W][0]!=0 and
                      TT[(x+1)%X][(y+0)%Y][(z+0)%Z][(w+3)%W][0]!=0): lufa_wx=1
            if(kafel_yw and kij_w):
                   if(TT[x][(y+1)%Y][(z+0)%Z][(w+2)%W][0]!=0 and
                      TT[x][(y+1)%Y][(z+0)%Z][(w+3)%W][0]!=0): lufa_wy=1
            if(kafel_zw and kij_w):
                   if(TT[x][(y+0)%Y][(z+1)%Z][(w+2)%W][0]!=0 and
                      TT[x][(y+0)%Y][(z+1)%Z][(w+3)%W][0]!=0): lufa_wz=1

            #sprawdzanie dział x3x4
            if(kost_xyz and lufa_xy and lufa_xz and
               TT[(x+2)%X][(y+1)%Y][(z+1)%Z][(w+0)%W][0]!=0 and
               TT[(x+3)%X][(y+1)%Y][(z+1)%Z][(w+0)%W][0]!=0): dział_xyz=1
            if(kost_xyz and lufa_yx and lufa_yz and
               TT[(x+1)%X][(y+2)%Y][(z+1)%Z][(w+0)%W][0]!=0 and
               TT[(x+1)%X][(y+3)%Y][(z+1)%Z][(w+0)%W][0]!=0): dział_yxz=1
            if(kost_xyz and lufa_zx and lufa_zy and
               TT[(x+1)%X][(y+1)%Y][(z+2)%Z][(w+0)%W][0]!=0 and
               TT[(x+1)%X][(y+1)%Y][(z+3)%Z][(w+0)%W][0]!=0): dział_zxy=1

            if(kost_yzw and lufa_wy and lufa_wz and
               TT[(x+0)%X][(y+1)%Y][(z+1)%Z][(w+2)%W][0]!=0 and
               TT[(x+0)%X][(y+1)%Y][(z+1)%Z][(w+3)%W][0]!=0): dział_wyz=1
            if(kost_yzw and lufa_yw and lufa_yz and
               TT[(x+0)%X][(y+2)%Y][(z+1)%Z][(w+1)%W][0]!=0 and
               TT[(x+0)%X][(y+3)%Y][(z+1)%Z][(w+1)%W][0]!=0): dział_yzw=1
            if(kost_yzw and lufa_zw and lufa_zy and
               TT[(x+0)%X][(y+1)%Y][(z+2)%Z][(w+1)%W][0]!=0 and
               TT[(x+0)%X][(y+1)%Y][(z+3)%Z][(w+1)%W][0]!=0): dział_zyw=1

            if(kost_xzw and lufa_xw and lufa_xz and
               TT[(x+2)%X][(y+0)%Y][(z+1)%Z][(w+1)%W][0]!=0 and
               TT[(x+3)%X][(y+0)%Y][(z+1)%Z][(w+1)%W][0]!=0): dział_xzw=1
            if(kost_xzw and lufa_wx and lufa_wz and
               TT[(x+1)%X][(y+0)%Y][(z+1)%Z][(w+2)%W][0]!=0 and
               TT[(x+1)%X][(y+0)%Y][(z+1)%Z][(w+3)%W][0]!=0): dział_wxz=1
            if(kost_xzw and lufa_zx and lufa_zw and
               TT[(x+1)%X][(y+0)%Y][(z+2)%Z][(w+1)%W][0]!=0 and
               TT[(x+1)%X][(y+0)%Y][(z+3)%Z][(w+1)%W][0]!=0): dział_zxw=1

            if(kost_xyw and lufa_xy and lufa_xw and
               TT[(x+2)%X][(y+1)%Y][(z+0)%Z][(w+1)%W][0]!=0 and
               TT[(x+3)%X][(y+1)%Y][(z+0)%Z][(w+1)%W][0]!=0): dział_xyw=1
            if(kost_xyw and lufa_yx and lufa_yw and
               TT[(x+1)%X][(y+2)%Y][(z+0)%Z][(w+1)%W][0]!=0 and
               TT[(x+1)%X][(y+3)%Y][(z+0)%Z][(w+1)%W][0]!=0): dział_yxw=1
            if(kost_xyw and lufa_wx and lufa_wy and
               TT[(x+1)%X][(y+1)%Y][(z+0)%Z][(w+2)%W][0]!=0 and
               TT[(x+1)%X][(y+1)%Y][(z+0)%Z][(w+3)%W][0]!=0): dział_wxy=1

            #sprawdzanie dział plazmowych x4
            if(m_tese):
              if(dział_xyz and dział_xzw and dział_xyw):
                 if(TT[(x+2)%X][(y+1)%Y][(z+1)%Z][(w+1)%W][0]!=0 and
                    TT[(x+3)%X][(y+1)%Y][(z+1)%Z][(w+1)%W][0]!=0): plazm_x=1
              if(dział_yxz and dział_yzw and dział_yxw):
                 if(TT[(x+1)%X][(y+2)%Y][(z+1)%Z][(w+1)%W][0]!=0 and
                    TT[(x+1)%X][(y+3)%Y][(z+1)%Z][(w+1)%W][0]!=0): plazm_y=1
              if(dział_zxy and dział_zxw and dział_zyw):
                 if(TT[(x+1)%X][(y+1)%Y][(z+2)%Z][(w+1)%W][0]!=0 and
                    TT[(x+1)%X][(y+1)%Y][(z+3)%Z][(w+1)%W][0]!=0): plazm_z=1
              if(dział_wyz and dział_wxz and dział_wxy):
                 if(TT[(x+1)%X][(y+1)%Y][(z+1)%Z][(w+2)%W][0]!=0 and
                    TT[(x+1)%X][(y+1)%Y][(z+1)%Z][(w+3)%W][0]!=0): plazm_w=1

            #sprawdzanie płaszczyzn (pól) x6
            if(lufa_xy and lufa_yx):
                if(TT[(x+2)%X][(y+2)%Y][(z+0)%Z][(w+0)%W][0]!=0 and
                   TT[(x+3)%X][(y+2)%Y][(z+0)%Z][(w+0)%W][0]!=0 and
                   TT[(x+2)%X][(y+3)%Y][(z+0)%Z][(w+0)%W][0]!=0 and
                   TT[(x+3)%X][(y+3)%Y][(z+0)%Z][(w+0)%W][0]!=0): pol_xy=1
            if(lufa_xz and lufa_zx):
                if(TT[(x+2)%X][(y+0)%Y][(z+2)%Z][(w+0)%W][0]!=0 and
                   TT[(x+3)%X][(y+0)%Y][(z+2)%Z][(w+0)%W][0]!=0 and
                   TT[(x+2)%X][(y+0)%Y][(z+3)%Z][(w+0)%W][0]!=0 and
                   TT[(x+3)%X][(y+0)%Y][(z+3)%Z][(w+0)%W][0]!=0): pol_xz=1
            if(lufa_xw and lufa_wx):
                if(TT[(x+2)%X][(y+0)%Y][(z+0)%Z][(w+2)%W][0]!=0 and
                   TT[(x+3)%X][(y+0)%Y][(z+0)%Z][(w+2)%W][0]!=0 and
                   TT[(x+2)%X][(y+0)%Y][(z+0)%Z][(w+3)%W][0]!=0 and
                   TT[(x+3)%X][(y+0)%Y][(z+0)%Z][(w+3)%W][0]!=0): pol_xw=1
            if(lufa_zy and lufa_yz):
                if(TT[(x+0)%X][(y+2)%Y][(z+2)%Z][(w+0)%W][0]!=0 and
                   TT[(x+0)%X][(y+2)%Y][(z+3)%Z][(w+0)%W][0]!=0 and
                   TT[(x+0)%X][(y+3)%Y][(z+2)%Z][(w+0)%W][0]!=0 and
                   TT[(x+0)%X][(y+3)%Y][(z+3)%Z][(w+0)%W][0]!=0): pol_yz=1
            if(lufa_wy and lufa_yw):
                if(TT[(x+0)%X][(y+2)%Y][(z+0)%Z][(w+2)%W][0]!=0 and
                   TT[(x+0)%X][(y+2)%Y][(z+0)%Z][(w+3)%W][0]!=0 and
                   TT[(x+0)%X][(y+3)%Y][(z+0)%Z][(w+2)%W][0]!=0 and
                   TT[(x+0)%X][(y+3)%Y][(z+0)%Z][(w+3)%W][0]!=0): pol_yw=1
            if(lufa_wz and lufa_zw):
                if(TT[(x+0)%X][(y+0)%Y][(z+2)%Z][(w+2)%W][0]!=0 and
                   TT[(x+0)%X][(y+0)%Y][(z+3)%Z][(w+2)%W][0]!=0 and
                   TT[(x+0)%X][(y+0)%Y][(z+2)%Z][(w+3)%W][0]!=0 and
                   TT[(x+0)%X][(y+0)%Y][(z+3)%Z][(w+3)%W][0]!=0): pol_zw=1

            #sprawdzanie kanapek x2x6
            if(pol_xy):
               if(dział_xyz and dział_yxz and
                  TT[(x+2)%X][(y+2)%Y][(z+1)%Z][(w+0)%W][0]!=0 and
                  TT[(x+3)%X][(y+2)%Y][(z+1)%Z][(w+0)%W][0]!=0 and
                  TT[(x+2)%X][(y+3)%Y][(z+1)%Z][(w+0)%W][0]!=0 and
                  TT[(x+3)%X][(y+3)%Y][(z+1)%Z][(w+0)%W][0]!=0): kana_xyz=1
               if(dział_xyw and dział_yxw and
                  TT[(x+2)%X][(y+2)%Y][(z+0)%Z][(w+1)%W][0]!=0 and
                  TT[(x+3)%X][(y+2)%Y][(z+0)%Z][(w+1)%W][0]!=0 and
                  TT[(x+2)%X][(y+3)%Y][(z+0)%Z][(w+1)%W][0]!=0 and
                  TT[(x+3)%X][(y+3)%Y][(z+0)%Z][(w+1)%W][0]!=0): kana_xyw=1
            if(pol_xz):
               if(dział_xyz and dział_zxy and
                  TT[(x+2)%X][(y+1)%Y][(z+2)%Z][(w+0)%W][0]!=0 and
                  TT[(x+3)%X][(y+1)%Y][(z+2)%Z][(w+0)%W][0]!=0 and
                  TT[(x+2)%X][(y+1)%Y][(z+3)%Z][(w+0)%W][0]!=0 and
                  TT[(x+3)%X][(y+1)%Y][(z+3)%Z][(w+0)%W][0]!=0): kana_xzy=1
               if(dział_xzw and dział_zxw and
                  TT[(x+2)%X][(y+0)%Y][(z+2)%Z][(w+1)%W][0]!=0 and
                  TT[(x+3)%X][(y+0)%Y][(z+2)%Z][(w+1)%W][0]!=0 and
                  TT[(x+2)%X][(y+0)%Y][(z+3)%Z][(w+1)%W][0]!=0 and
                  TT[(x+3)%X][(y+0)%Y][(z+3)%Z][(w+1)%W][0]!=0): kana_xzw=1
            if(pol_xw):
               if(dział_xyw and dział_wxy and
                  TT[(x+2)%X][(y+1)%Y][(z+0)%Z][(w+2)%W][0]!=0 and
                  TT[(x+3)%X][(y+1)%Y][(z+0)%Z][(w+2)%W][0]!=0 and
                  TT[(x+2)%X][(y+1)%Y][(z+0)%Z][(w+3)%W][0]!=0 and
                  TT[(x+3)%X][(y+1)%Y][(z+0)%Z][(w+3)%W][0]!=0): kana_xwy=1
               if(dział_xzw and dział_wxz and
                  TT[(x+2)%X][(y+0)%Y][(z+1)%Z][(w+2)%W][0]!=0 and
                  TT[(x+3)%X][(y+0)%Y][(z+1)%Z][(w+2)%W][0]!=0 and
                  TT[(x+2)%X][(y+0)%Y][(z+1)%Z][(w+3)%W][0]!=0 and
                  TT[(x+3)%X][(y+0)%Y][(z+1)%Z][(w+3)%W][0]!=0): kana_xwz=1

            if(pol_yz):
               if(dział_yxz and dział_zxy and
                  TT[(x+1)%X][(y+2)%Y][(z+2)%Z][(w+0)%W][0]!=0 and
                  TT[(x+1)%X][(y+3)%Y][(z+2)%Z][(w+0)%W][0]!=0 and
                  TT[(x+1)%X][(y+2)%Y][(z+3)%Z][(w+0)%W][0]!=0 and
                  TT[(x+1)%X][(y+3)%Y][(z+3)%Z][(w+0)%W][0]!=0): kana_yzx=1
               if(dział_yzw and dział_zyw and
                  TT[(x+0)%X][(y+2)%Y][(z+2)%Z][(w+1)%W][0]!=0 and
                  TT[(x+0)%X][(y+3)%Y][(z+2)%Z][(w+1)%W][0]!=0 and
                  TT[(x+0)%X][(y+2)%Y][(z+3)%Z][(w+1)%W][0]!=0 and
                  TT[(x+0)%X][(y+3)%Y][(z+3)%Z][(w+1)%W][0]!=0): kana_yzw=1
            if(pol_yw):
               if(dział_yxw and dział_wxy and
                  TT[(x+1)%X][(y+2)%Y][(z+0)%Z][(w+2)%W][0]!=0 and
                  TT[(x+1)%X][(y+3)%Y][(z+0)%Z][(w+2)%W][0]!=0 and
                  TT[(x+1)%X][(y+2)%Y][(z+0)%Z][(w+3)%W][0]!=0 and
                  TT[(x+1)%X][(y+3)%Y][(z+0)%Z][(w+3)%W][0]!=0): kana_ywx=1
               if(dział_yzw and dział_wyz and
                  TT[(x+0)%X][(y+2)%Y][(z+1)%Z][(w+2)%W][0]!=0 and
                  TT[(x+0)%X][(y+3)%Y][(z+1)%Z][(w+2)%W][0]!=0 and
                  TT[(x+0)%X][(y+2)%Y][(z+1)%Z][(w+3)%W][0]!=0 and
                  TT[(x+0)%X][(y+3)%Y][(z+1)%Z][(w+3)%W][0]!=0): kana_ywz=1
               
            if(pol_zw):
               if(dział_wxz and dział_zxw and
                  TT[(x+1)%X][(y+0)%Y][(z+2)%Z][(w+2)%W][0]!=0 and
                  TT[(x+1)%X][(y+0)%Y][(z+2)%Z][(w+3)%W][0]!=0 and
                  TT[(x+1)%X][(y+0)%Y][(z+3)%Z][(w+2)%W][0]!=0 and
                  TT[(x+1)%X][(y+0)%Y][(z+3)%Z][(w+3)%W][0]!=0): kana_zwx=1
               if(dział_wyz and dział_zyw and
                  TT[(x+0)%X][(y+1)%Y][(z+2)%Z][(w+2)%W][0]!=0 and
                  TT[(x+0)%X][(y+1)%Y][(z+2)%Z][(w+3)%W][0]!=0 and
                  TT[(x+0)%X][(y+1)%Y][(z+3)%Z][(w+2)%W][0]!=0 and
                  TT[(x+0)%X][(y+1)%Y][(z+3)%Z][(w+3)%W][0]!=0): kana_zwy=1

            #sprawdzanie burgerów x6
            if(kana_xyz and kana_xyw and plazm_x and plazm_y and
               TT[(x+2)%X][(y+2)%Y][(z+1)%Z][(w+1)%W][0]!=0 and
               TT[(x+3)%X][(y+2)%Y][(z+1)%Z][(w+1)%W][0]!=0 and
               TT[(x+2)%X][(y+3)%Y][(z+1)%Z][(w+1)%W][0]!=0 and
               TT[(x+3)%X][(y+3)%Y][(z+1)%Z][(w+1)%W][0]!=0): burg_xy=1
            if(kana_xzy and kana_xzw and plazm_x and plazm_z and
               TT[(x+2)%X][(y+1)%Y][(z+2)%Z][(w+1)%W][0]!=0 and
               TT[(x+3)%X][(y+1)%Y][(z+2)%Z][(w+1)%W][0]!=0 and
               TT[(x+2)%X][(y+1)%Y][(z+3)%Z][(w+1)%W][0]!=0 and
               TT[(x+3)%X][(y+1)%Y][(z+3)%Z][(w+1)%W][0]!=0): burg_xz=1
            if(kana_xwz and kana_xwy and plazm_x and plazm_w and
               TT[(x+2)%X][(y+1)%Y][(z+1)%Z][(w+2)%W][0]!=0 and
               TT[(x+3)%X][(y+1)%Y][(z+1)%Z][(w+2)%W][0]!=0 and
               TT[(x+2)%X][(y+1)%Y][(z+1)%Z][(w+3)%W][0]!=0 and
               TT[(x+3)%X][(y+1)%Y][(z+1)%Z][(w+3)%W][0]!=0): burg_xw=1
            if(kana_yzx and kana_yzw and plazm_z and plazm_y and
               TT[(x+1)%X][(y+2)%Y][(z+2)%Z][(w+1)%W][0]!=0 and
               TT[(x+1)%X][(y+2)%Y][(z+3)%Z][(w+1)%W][0]!=0 and
               TT[(x+1)%X][(y+3)%Y][(z+2)%Z][(w+1)%W][0]!=0 and
               TT[(x+1)%X][(y+3)%Y][(z+3)%Z][(w+1)%W][0]!=0): burg_yz=1
            if(kana_ywz and kana_ywx and plazm_w and plazm_y and
               TT[(x+1)%X][(y+2)%Y][(z+1)%Z][(w+2)%W][0]!=0 and
               TT[(x+1)%X][(y+2)%Y][(z+1)%Z][(w+3)%W][0]!=0 and
               TT[(x+1)%X][(y+3)%Y][(z+1)%Z][(w+2)%W][0]!=0 and
               TT[(x+1)%X][(y+3)%Y][(z+1)%Z][(w+3)%W][0]!=0): burg_yw=1
            if(kana_zwx and kana_zwy and plazm_z and plazm_w and
               TT[(x+1)%X][(y+1)%Y][(z+2)%Z][(w+2)%W][0]!=0 and
               TT[(x+1)%X][(y+1)%Y][(z+2)%Z][(w+3)%W][0]!=0 and
               TT[(x+1)%X][(y+1)%Y][(z+3)%Z][(w+2)%W][0]!=0 and
               TT[(x+1)%X][(y+1)%Y][(z+3)%Z][(w+3)%W][0]!=0): burg_zw=1

            #sprawdzanie sześcianów x4 i wisiorków x4
            if(kana_xyz and kana_yzx and kana_xzy and
               TT[(x+2)%X][(y+2)%Y][(z+2)%Z][(w+0)%W][0]!=0 and
               TT[(x+3)%X][(y+2)%Y][(z+2)%Z][(w+0)%W][0]!=0 and
               TT[(x+2)%X][(y+3)%Y][(z+2)%Z][(w+0)%W][0]!=0 and
               TT[(x+3)%X][(y+3)%Y][(z+2)%Z][(w+0)%W][0]!=0 and
               TT[(x+2)%X][(y+2)%Y][(z+3)%Z][(w+0)%W][0]!=0 and
               TT[(x+3)%X][(y+2)%Y][(z+3)%Z][(w+0)%W][0]!=0 and
               TT[(x+2)%X][(y+3)%Y][(z+3)%Z][(w+0)%W][0]!=0 and
               TT[(x+3)%X][(y+3)%Y][(z+3)%Z][(w+0)%W][0]!=0): szsc_xyz=1
            if(burg_xy and burg_yz and burg_xz and szsc_xyz and
               TT[(x+2)%X][(y+2)%Y][(z+2)%Z][(w+1)%W][0]!=0 and
               TT[(x+3)%X][(y+2)%Y][(z+2)%Z][(w+1)%W][0]!=0 and
               TT[(x+2)%X][(y+3)%Y][(z+2)%Z][(w+1)%W][0]!=0 and
               TT[(x+3)%X][(y+3)%Y][(z+2)%Z][(w+1)%W][0]!=0 and
               TT[(x+2)%X][(y+2)%Y][(z+3)%Z][(w+1)%W][0]!=0 and
               TT[(x+3)%X][(y+2)%Y][(z+3)%Z][(w+1)%W][0]!=0 and
               TT[(x+2)%X][(y+3)%Y][(z+3)%Z][(w+1)%W][0]!=0 and
               TT[(x+3)%X][(y+3)%Y][(z+3)%Z][(w+1)%W][0]!=0): taxi_xyz=1

            if(kana_xyw and kana_ywx and kana_xwy and
               TT[(x+2)%X][(y+2)%Y][(z+0)%Z][(w+2)%W][0]!=0 and
               TT[(x+3)%X][(y+2)%Y][(z+0)%Z][(w+2)%W][0]!=0 and
               TT[(x+2)%X][(y+3)%Y][(z+0)%Z][(w+2)%W][0]!=0 and
               TT[(x+3)%X][(y+3)%Y][(z+0)%Z][(w+2)%W][0]!=0 and
               TT[(x+2)%X][(y+2)%Y][(z+0)%Z][(w+3)%W][0]!=0 and
               TT[(x+3)%X][(y+2)%Y][(z+0)%Z][(w+3)%W][0]!=0 and
               TT[(x+2)%X][(y+3)%Y][(z+0)%Z][(w+3)%W][0]!=0 and
               TT[(x+3)%X][(y+3)%Y][(z+0)%Z][(w+3)%W][0]!=0): szsc_xyw=1
            if(burg_xy and burg_yw and burg_xw and szsc_xyw and
               TT[(x+2)%X][(y+2)%Y][(z+1)%Z][(w+2)%W][0]!=0 and
               TT[(x+3)%X][(y+2)%Y][(z+1)%Z][(w+2)%W][0]!=0 and
               TT[(x+2)%X][(y+3)%Y][(z+1)%Z][(w+2)%W][0]!=0 and
               TT[(x+3)%X][(y+3)%Y][(z+1)%Z][(w+2)%W][0]!=0 and
               TT[(x+2)%X][(y+2)%Y][(z+1)%Z][(w+3)%W][0]!=0 and
               TT[(x+3)%X][(y+2)%Y][(z+1)%Z][(w+3)%W][0]!=0 and
               TT[(x+2)%X][(y+3)%Y][(z+1)%Z][(w+3)%W][0]!=0 and
               TT[(x+3)%X][(y+3)%Y][(z+1)%Z][(w+3)%W][0]!=0): taxi_xyw=1

            if(kana_xzw and kana_zwx and kana_xwz and
               TT[(x+2)%X][(y+0)%Y][(z+2)%Z][(w+2)%W][0]!=0 and
               TT[(x+3)%X][(y+0)%Y][(z+2)%Z][(w+2)%W][0]!=0 and
               TT[(x+2)%X][(y+0)%Y][(z+3)%Z][(w+2)%W][0]!=0 and
               TT[(x+3)%X][(y+0)%Y][(z+3)%Z][(w+2)%W][0]!=0 and
               TT[(x+2)%X][(y+0)%Y][(z+2)%Z][(w+3)%W][0]!=0 and
               TT[(x+3)%X][(y+0)%Y][(z+2)%Z][(w+3)%W][0]!=0 and
               TT[(x+2)%X][(y+0)%Y][(z+3)%Z][(w+3)%W][0]!=0 and
               TT[(x+3)%X][(y+0)%Y][(z+3)%Z][(w+3)%W][0]!=0): szsc_xzw=1
            if(burg_xz and burg_zw and burg_xw and szsc_xzw and
               TT[(x+2)%X][(y+1)%Y][(z+2)%Z][(w+2)%W][0]!=0 and
               TT[(x+3)%X][(y+1)%Y][(z+2)%Z][(w+2)%W][0]!=0 and
               TT[(x+2)%X][(y+1)%Y][(z+3)%Z][(w+2)%W][0]!=0 and
               TT[(x+3)%X][(y+1)%Y][(z+3)%Z][(w+2)%W][0]!=0 and
               TT[(x+2)%X][(y+1)%Y][(z+2)%Z][(w+3)%W][0]!=0 and
               TT[(x+3)%X][(y+1)%Y][(z+2)%Z][(w+3)%W][0]!=0 and
               TT[(x+2)%X][(y+1)%Y][(z+3)%Z][(w+3)%W][0]!=0 and
               TT[(x+3)%X][(y+1)%Y][(z+3)%Z][(w+3)%W][0]!=0): taxi_xzw=1

            if(kana_yzw and kana_zwy and kana_ywz and
               TT[(x+0)%X][(y+2)%Y][(z+2)%Z][(w+2)%W][0]!=0 and
               TT[(x+0)%X][(y+3)%Y][(z+2)%Z][(w+2)%W][0]!=0 and
               TT[(x+0)%X][(y+2)%Y][(z+3)%Z][(w+2)%W][0]!=0 and
               TT[(x+0)%X][(y+3)%Y][(z+3)%Z][(w+2)%W][0]!=0 and
               TT[(x+0)%X][(y+2)%Y][(z+2)%Z][(w+3)%W][0]!=0 and
               TT[(x+0)%X][(y+3)%Y][(z+2)%Z][(w+3)%W][0]!=0 and
               TT[(x+0)%X][(y+2)%Y][(z+3)%Z][(w+3)%W][0]!=0 and
               TT[(x+0)%X][(y+3)%Y][(z+3)%Z][(w+3)%W][0]!=0): szsc_yzw=1
            if(burg_yz and burg_zw and burg_yw and szsc_yzw and
               TT[(x+1)%X][(y+2)%Y][(z+2)%Z][(w+2)%W][0]!=0 and
               TT[(x+1)%X][(y+3)%Y][(z+2)%Z][(w+2)%W][0]!=0 and
               TT[(x+1)%X][(y+2)%Y][(z+3)%Z][(w+2)%W][0]!=0 and
               TT[(x+1)%X][(y+3)%Y][(z+3)%Z][(w+2)%W][0]!=0 and
               TT[(x+1)%X][(y+2)%Y][(z+2)%Z][(w+3)%W][0]!=0 and
               TT[(x+1)%X][(y+3)%Y][(z+2)%Z][(w+3)%W][0]!=0 and
               TT[(x+1)%X][(y+2)%Y][(z+3)%Z][(w+3)%W][0]!=0 and
               TT[(x+1)%X][(y+3)%Y][(z+3)%Z][(w+3)%W][0]!=0): taxi_yzw=1

            #sprawdzanie dużego tesseraktu
            if(taxi_xyz and taxi_yzw and taxi_xzw and taxi_xyw):
                tesserakt = 1
                for i in range(len(TK)):
                   if(TK[i][0]==0):
                       tesserakt=0
                       break;

            if(tesserakt==0):
                if(taxi_xyz):                       #taxi
                    grupa=grupuj(4,4,4,2,x,y,z,w)
                    lista.append(grupa)
                else:
                    if(szsc_xyz):                   #szsc
                        grupa=grupuj(4,4,4,1,x,y,z,w)
                        lista.append(grupa)
                if(taxi_xyw):
                    grupa=grupuj(4,4,2,4,x,y,z,w)
                    lista.append(grupa)
                else:
                    if(szsc_xyw):
                        grupa=grupuj(4,4,1,4,x,y,z,w)
                        lista.append(grupa)
                if(taxi_xzw):
                    grupa=grupuj(4,2,4,4,x,y,z,w)
                    lista.append(grupa)
                else:
                    if(szsc_xzw):
                        grupa=grupuj(4,1,4,4,x,y,z,w)
                        lista.append(grupa)
                if(taxi_yzw):
                    grupa=grupuj(2,4,4,4,x,y,z,w)
                    lista.append(grupa)
                else:
                    if(szsc_yzw):
                        grupa=grupuj(1,4,4,4,x,y,z,w)
                        lista.append(grupa)
                
                if(burg_xy):                       #burg
                    grupa=grupuj(4,4,2,2,x,y,z,w)
                    lista.append(grupa)
                else:
                    if(kana_xyz):                   #kana
                        grupa=grupuj(4,4,2,1,x,y,z,w)
                        lista.append(grupa)
                    if(kana_xyw):
                        grupa=grupuj(4,4,1,2,x,y,z,w)
                        lista.append(grupa)
                    elif(pol_xy):                   #pol
                        grupa=grupuj(4,4,1,1,x,y,z,w)
                        lista.append(grupa)
                if(burg_xz):
                    grupa=grupuj(4,2,4,2,x,y,z,w)
                    lista.append(grupa)
                else:
                    if(kana_xzy):
                        grupa=grupuj(4,2,4,1,x,y,z,w)
                        lista.append(grupa)
                    if(kana_xzw):
                        grupa=grupuj(4,1,4,2,x,y,z,w)
                        lista.append(grupa)
                    elif(pol_xz):
                        grupa=grupuj(4,1,4,1,x,y,z,w)
                        lista.append(grupa)
                if(burg_xw):
                    grupa=grupuj(4,2,2,4,x,y,z,w)
                    lista.append(grupa)
                else:
                    if(kana_xwy):
                        grupa=grupuj(4,2,1,4,x,y,z,w)
                        lista.append(grupa)
                    if(kana_xwz):
                        grupa=grupuj(4,1,2,4,x,y,z,w)
                        lista.append(grupa)
                    elif(pol_xw):
                        grupa=grupuj(4,1,1,4,x,y,z,w)
                        lista.append(grupa)
                if(burg_yz):
                    grupa=grupuj(2,4,4,2,x,y,z,w)
                    lista.append(grupa)
                else:
                    if(kana_yzx):
                        grupa=grupuj(2,4,4,1,x,y,z,w)
                        lista.append(grupa)
                    if(kana_yzw):
                        grupa=grupuj(1,4,4,2,x,y,z,w)
                        lista.append(grupa)
                    elif(pol_yz):
                        grupa=grupuj(1,4,4,1,x,y,z,w)
                        lista.append(grupa)
                if(burg_yw):
                    grupa=grupuj(2,4,2,4,x,y,z,w)
                    lista.append(grupa)
                else:
                    if(kana_ywx):
                        grupa=grupuj(2,4,1,4,x,y,z,w)
                        lista.append(grupa)
                    if(kana_ywz):
                        grupa=grupuj(1,4,2,4,x,y,z,w)
                        lista.append(grupa)
                    elif(pol_yw):
                        grupa=grupuj(1,4,1,4,x,y,z,w)
                        lista.append(grupa)
                if(burg_zw):
                    grupa=grupuj(2,2,4,4,x,y,z,w)
                    lista.append(grupa)
                else:
                    if(kana_zwx):
                        grupa=grupuj(2,1,4,4,x,y,z,w)
                        lista.append(grupa)
                    if(kana_zwy):
                        grupa=grupuj(1,2,4,4,x,y,z,w)
                        lista.append(grupa)
                    elif(pol_zw):
                        grupa=grupuj(1,1,4,4,x,y,z,w)
                        lista.append(grupa)
       
                
                if(plazm_x):                    #plazm
                    grupa=grupuj(4,2,2,2,x,y,z,w)
                    lista.append(grupa)
                else:
                    if(dział_xyz):              #dział
                        grupa=grupuj(4,2,2,1,x,y,z,w)
                        lista.append(grupa)
                    elif(lufa_xy):              #lufa
                        grupa=grupuj(4,2,1,1,x,y,z,w)
                        lista.append(grupa)
                    if(dział_xyw):
                        grupa=grupuj(4,2,1,2,x,y,z,w)
                        lista.append(grupa)
                    elif(lufa_xw):
                        grupa=grupuj(4,1,1,2,x,y,z,w)
                        lista.append(grupa)
                    if(dział_xzw):
                        grupa=grupuj(4,1,2,2,x,y,z,w)
                        lista.append(grupa)
                    elif(lufa_xz):
                        grupa=grupuj(4,1,2,1,x,y,z,w)
                        lista.append(grupa)
                    elif(kij_x):                #kij
                        grupa=grupuj(4,1,1,1,x,y,z,w)
                        lista.append(grupa)
                    else:
                        if(pillz_x):            #pillz
                            grupa=grupuj(2,1,1,1,x,y,z,w)
                            lista.append(grupa)
                        else:
                            grupa=grupuj(1,1,1,1,x,y,z,w)
                            lista.append(grupa) #solo
                if(plazm_y):
                    grupa=grupuj(2,4,2,2,x,y,z,w)
                    lista.append(grupa)
                else:
                    if(dział_yxz):
                        grupa=grupuj(2,4,2,1,x,y,z,w)
                        lista.append(grupa)
                    elif(lufa_yx):
                        grupa=grupuj(2,4,1,1,x,y,z,w)
                        lista.append(grupa)
                    if(dział_yxw):
                        grupa=grupuj(2,4,1,2,x,y,z,w)
                        lista.append(grupa)
                    elif(lufa_yw):
                        grupa=grupuj(1,4,1,2,x,y,z,w)
                        lista.append(grupa)
                    if(dział_yzw):
                        grupa=grupuj(1,4,2,2,x,y,z,w)
                        lista.append(grupa)
                    elif(lufa_yz):
                        grupa=grupuj(1,4,2,1,x,y,z,w)
                        lista.append(grupa)
                    elif(kij_y):
                        grupa=grupuj(1,4,1,1,x,y,z,w)
                        lista.append(grupa)
                    else:
                        if(pillz_y):
                            grupa=grupuj(1,2,1,1,x,y,z,w)
                            lista.append(grupa)
                if(plazm_z):
                    grupa=grupuj(2,2,4,2,x,y,z,w)
                    lista.append(grupa)
                else:
                    if(dział_zxy):
                        grupa=grupuj(2,2,4,1,x,y,z,w)
                        lista.append(grupa)
                    elif(lufa_zx):
                        grupa=grupuj(2,1,4,1,x,y,z,w)
                        lista.append(grupa)    
                    if(dział_zxw):
                        grupa=grupuj(2,1,4,2,x,y,z,w)
                        lista.append(grupa)
                    elif(lufa_zw):
                        grupa=grupuj(1,1,4,2,x,y,z,w)
                        lista.append(grupa)    
                    if(dział_zyw):
                        grupa=grupuj(1,2,4,2,x,y,z,w)
                        lista.append(grupa)
                    elif(lufa_zy):
                        grupa=grupuj(1,2,4,1,x,y,z,w)
                        lista.append(grupa)
                    elif(kij_z):
                        grupa=grupuj(1,1,4,1,x,y,z,w)
                        lista.append(grupa)
                    else:
                        if(pillz_z):
                            grupa=grupuj(1,1,2,1,x,y,z,w)
                            lista.append(grupa)
                if(plazm_w):
                    grupa=grupuj(2,2,2,4,x,y,z,w)
                    lista.append(grupa)
                else:
                    if(dział_wxy):
                        grupa=grupuj(2,2,1,4,x,y,z,w)
                        lista.append(grupa)
                    elif(lufa_wx):
                        grupa=grupuj(2,1,1,4,x,y,z,w)
                        lista.append(grupa)
                    if(dział_wxz):
                        grupa=grupuj(2,1,2,4,x,y,z,w)
                        lista.append(grupa)
                    elif(lufa_wz):
                        grupa=grupuj(1,1,2,4,x,y,z,w)
                        lista.append(grupa)
                    if(dział_wyz):
                        grupa=grupuj(1,2,2,4,x,y,z,w)
                        lista.append(grupa)
                    elif(lufa_wy):
                        grupa=grupuj(1,2,1,4,x,y,z,w)
                        lista.append(grupa)
                    elif(kij_w):
                        grupa=grupuj(1,1,1,4,x,y,z,w)
                        lista.append(grupa)
                    else:
                        if(pillz_w):
                            grupa=grupuj(1,1,1,2,x,y,z,w)
                            lista.append(grupa)
                
                if(m_tese):                             #m_tese
                    grupa=grupuj(2,2,2,2,x,y,z,w)
                    lista.append(grupa)
                else:
                    if(kost_xyz):                       #kost
                        grupa=grupuj(2,2,2,1,x,y,z,w)
                        lista.append(grupa)
                    elif(kafel_xy):                     #kafel
                        grupa=grupuj(2,2,1,1,x,y,z,w)
                        lista.append(grupa)
                    if(kost_xyw):
                        grupa=grupuj(2,2,1,2,x,y,z,w)
                        lista.append(grupa)
                    elif(kafel_yw):
                        grupa=grupuj(1,2,1,2,x,y,z,w)
                        lista.append(grupa)
                    if(kost_xzw):
                        grupa=grupuj(2,1,2,2,x,y,z,w)
                        lista.append(grupa)
                    elif(kafel_xz):
                        grupa=grupuj(2,1,2,1,x,y,z,w)
                        lista.append(grupa)
                    if(kost_yzw):
                        grupa=grupuj(1,2,2,2,x,y,z,w)
                        lista.append(grupa)
                    elif(kafel_zw):
                        grupa=grupuj(1,1,2,2,x,y,z,w)
                        lista.append(grupa)
                    if(kafel_xw):
                        grupa=grupuj(2,1,1,2,x,y,z,w)
                        lista.append(grupa)
                    if(kafel_yz):
                        grupa=grupuj(1,2,2,1,x,y,z,w)
                        lista.append(grupa)
            else:
                #grupa=grupuj(4,4,4,4,x,y,z,w)
                #lista.append(grupa)
                return 1
                
    return lista
                                    
def grupuj(x,y,z,w,px,py,pz,pw):
    global X,Y,Z,W
    grupa = []
    for l in range(w):
        for k in range(z):
            for j in range(y):
                for i in range(x):
                    grupa.append([(i+px)%X,(j+py)%Y,(k+pz)%Z,(l+pw)%W])
    return grupa

def Filtruj(lista):
    if(lista==1): return 1;
    if not lista: return 0;

    for l in range(len(lista)):
        #for m in range(len(lista[l])-1):
        #    for p in range(m+1,len(lista[l])):
        #        if(lista[l][m]==lista[l][p]):
        #            del lista[l][p]; p-=1
        plista = []
        [plista.append(m) for m in lista[l] if m not in plista]
        lista[l] = plista
        
    #print(lista)

    for k in range(len(lista)-1):
        for j in range(len(lista)):
            if(j!=k and len(lista[k])>=len(lista[j])):
                
                for i in range(len(lista[j])):
                    if(lista[j][i] not in lista[k]):
                        break;
                    elif(i==len(lista[j])-1):
                        lista[j]=[]
                    else:
                        continue
            else:
                continue

    while([] in lista):
        lista.remove([])

    return lista

def Filtr_2(lista,TK,TT):
    if not lista: return 0;
    jede = 0; zero = 0;
    for i in range(len(TK)):
        if(TK[i][0]==1):
            jede=1
            break;
        if(TK[i][0]==0): zero=1
    if(not jede):
        if(zero): return 0;
        else: return 2;
    if(lista==1):
        return 1;
    else:
        for j in range(len(lista)):
            jede = 0
            for i in range(len(lista[j])):
                if(TT[lista[j][i][0]][lista[j][i][1]]
                   [lista[j][i][2]][lista[j][i][3]][0]==1):
                    jede=1
                    break;
            if(not jede):
                lista[j]=[]
                
    while([] in lista):
        lista.remove([])
    return lista


def Minim(n,zbiór,TT):
    if(zbiór==2): return 2;
    if(zbiór==1): return 1;
    if not zbiór: return 0;
    lista = []
    for j in range(len(zbiór)):
        cr=zbiór[j][0]; x=cr[0];
        y=cr[1];z=cr[2];w=cr[3];
        iloc = Bin(n,TT,x,y,z,w)
        for i in range(1,len(zbiór[j])):
            cr=zbiór[j][i]; x=cr[0];
            y=cr[1];z=cr[2];w=cr[3];
            ilcc= Bin(n,TT,x,y,z,w)
            for k in range(len(iloc)):
                if(ilcc[k]!=iloc[k]):
                    ilist = list(iloc)
                    ilist[k] = '-'
                    iloc = ''.join(ilist)
        lista.append(iloc)
    return lista

def Bin(n,TT,x,y,z,w):
    nr=TT[x][y][z][w][1]
    nr='{0:08b}'.format(nr)
    nr=nr[8-int(n):]
    return nr

def Drukuj(n,lista):
    wynik = 'f('
    if(n>0):
        wynik+='A'
        if(n>1):
            wynik+=',B'
            if(n>2):
                wynik+=',C'
                if(n>3):
                    wynik+=',D'
                    if(n>4):
                        wynik+=',E'
                        if(n>5):
                            wynik+=',F'
                            if(n>6):
                                wynik+=',G'
                                if(n>7):
                                    wynik+=',H'
    wynik+=') = '
    if(lista==2):
        wynik+='X'
        print(wynik); return wynik
    if(lista==1):
        wynik+='1'
        print(wynik); return wynik
    if not lista:
        wynik+='0'
        print(wynik); return wynik
        
    for j in range(len(lista)):
        #l = len(lista[j])
        if(n>0):
            if(lista[j][-1]=='1'):
                wynik+='A'
            elif(lista[j][-1]=='0'):
                wynik+="A'"
            else:
                pass
        if(n>1):
            if(lista[j][-2]=='1'):
                wynik+='B'
            elif(lista[j][-2]=='0'):
                wynik+="B'"
            else:
                pass
        if(n>2):
            if(lista[j][-3]=='1'):
                wynik+='C'
            elif(lista[j][-3]=='0'):
                wynik+="C'"
            else:
                pass
        if(n>3):
            if(lista[j][-4]=='1'):
                wynik+='D'
            elif(lista[j][-4]=='0'):
                wynik+="D'"
            else:
                pass
        if(n>4):
            if(lista[j][-5]=='1'):
                wynik+='E'
            elif(lista[j][-5]=='0'):
                wynik+="E'"
            else:
                pass
        if(n>5):
            if(lista[j][-6]=='1'):
                wynik+='F'
            elif(lista[j][-6]=='0'):
                wynik+="F'"
            else:
                pass
        if(n>6):
            if(lista[j][-7]=='1'):
                wynik+='G'
            elif(lista[j][-7]=='0'):
                wynik+="G'"
            else:
                pass
        if(n>7):
            if(lista[j][-8]=='1'):
                wynik+='H'
            elif(lista[j][-8]=='0'):
                wynik+="H'"
            else:
                pass
        if(j<len(lista)-1): wynik+='+'

    print(wynik)    
    return wynik
                        
    
#============================================================================##
    
#1.dobieranie odpowiedniej tablicy zależne od liczby zmiennych:
while True:
    n=input("Podaj liczbę zmiennych funkcji (0-8):")
    if(n=='q'): quit()
    elif(0<=int(n)<=8): break;
    
X,Y,Z,W = Siatka(int(n)); n=int(n)
nn=1
for i in range(n): nn=nn*2;

#2.zbieranie iloczynów pełnych równych 1:
dane = []; print("Podaj iloczyny pełne, dla który funcja zwarca 1, "+
                 "gdy zakończysz, wpisz 'q'")
while True:
    inp=input("> ")
    if(inp=='q'):
        break;
    elif(int(inp)<nn):
        dane.append(int(inp))
    else:
        pass
#2,5.zbieranie iloczynów równych '?'
ndane = []; print("Podaj iloczyny pełne, dla który funcja zwarca ?, "+
                 "gdy zakończysz, wpisz 'q'")
while True:
    inp=input("> ")
    if(inp=='q'):
        break;
    elif(int(inp)<nn):
        ndane.append(int(inp))
    else:
        pass

#3.tworzenie TK, przechowywanie wartości i położenia:
for l in range(W):
    for k in range(Z):
        for j in range(Y):
            for i in range(X):
                TK.append(['-',ST[i],ST[j],ST[k],ST[l],'d','b'])

''' 0 - wartość 0/1/-
    1 - położenie na osi x
    2 - położenie na osi y
    3 - położenie na osi z
    4 - położenie na osi w
    5 - id iloczynu
    6 - id iloczynu (bin)'''

#4.wypełnainie tablicy na podstawie dostarczonych danych:
for i in range(len(TK)):
    if(i in dane): TK[i][0]=1
    elif(i in ndane): TK[i][0]='?'
    else: TK[i][0]=0
    TK[i][5]=int(i)
    TK[i][6]="{0:b}".format(i)


#5.transformacja tablicy
TT=Trans(TK); print(); Wypisz(TT)
rTT=Trans_Rev(TT)
#5,5.grupowanie
Grupy = Lista(TK,rTT)
Grupy = Filtruj(Grupy)
Grupy = Filtr_2(Grupy,TK,rTT)
#6.Odczyt i wypisanie wyniku
Grupy = Minim(int(n),Grupy,rTT)
wynik = Drukuj(int(n),Grupy)




                
                
