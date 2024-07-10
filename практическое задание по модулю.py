def find_password(n):
    pairs = [ ]
    for i in range ( 1 , 21 ):
        for j in range ( i + 1 , 21 ):  
            if i + j != n:
                continue
            pairs.append ( (i , j) )

    result = ''.join ( [ str ( pair[ 0 ] ) + str ( pair[ 1 ] ) for pair in pairs ] )
    return result


n = 15
result = find_password ( n )
print ( result )