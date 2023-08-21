def solution(line):
    answer = []
    a = set()
    x_list = []
    y_list = []
    for i in range(len(line)-1):
        for j in range(i,len(line)):
            try:
                x,y = star(line[i],line[j])
                x = int(x)
                y = int(y)
                x_list.append(x)
                y_list.append(y)
                a.add((x,y))
            except:
                continue
    a = list(a) 
    xmax = max(x_list)
    ymax = max(y_list)
    xmin = min(x_list)
    ymin = min(y_list)
    
    print(a)
    p = [['.' for _ in range(xmin,xmax+1)] for _ in range(ymin,ymax+1)] 
    for i in range(len(a)):
        x = a[i][0] - xmin
        y = ymax - a[i][1]
        p[y][x] = '*'
    for i in range(len(p)):
        p[i] = "".join(p[i])
    return p    

def star(a,b):
    A,B,E = a
    C,D,F = b
    x = (B*F-E*D) / (A*D-B*C)
    y = (E*C-A*F) / (A*D-B*C)
    if int(x) == x and int(y) == y:
        return x,y
