def farey( n, asc=True ):
    """Python function to print the nth Farey sequence, either ascending or descending."""
    if asc: 
        a, b, c, d = 0, 1,  1  , n     # (*)
    else:
        a, b, c, d = 1, 1, n-1 , n     # (*)
    #print "%d/%d" % (a,b)
    aTmp, bTmp = 0,0
    while (asc and c <= n) or (not asc and a > 0):
        k = int((n + b)/d)
        a, b, c, d = c, d, k*c - a, k*d - b

        if a == 3 and b == 7:
            print(aTmp, bTmp)
            return
        aTmp, bTmp = a, b
        #print "%d/%d" % (a,b)

farey(10**6)