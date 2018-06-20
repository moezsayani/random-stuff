def sudokuSolver(A):

  X = [[] for i in range(9)]
  Y = [[] for i in range(9)]
  Z = [[] for i in range(9)]
    
  def a(S,v):
    if v in S: return False
    S.append(v)
    return True
    
  def r(S,v):
    S.remove(v)
    
  def g(x,y):
    if x>8: return True    
    if y>8: return g(x+1,0)
    if (A[x][y]!=0):
        return g(x,y+1)
    else:
        for d in range(1,10):
            A[x][y] = d
            if a(X[x],d):
                if a(Y[y],d): 
                    if a(Z[(x//3)*3+(y//3)],d):
                        if g(x,y+1): return True
                        r(Z[(x//3)*3+(y//3)],d)
                    r(Y[y],d)
                r(X[x],d)
            A[x][y]=0
    return False

  for x in range(9):
    for y in range(9):
        if A[x][y]>0:
            a(X[x],A[x][y])
            a(Y[y],A[x][y])
            a(Z[(x//3)*3+(y//3)],A[x][y])
  print g(0,0)
  return A
