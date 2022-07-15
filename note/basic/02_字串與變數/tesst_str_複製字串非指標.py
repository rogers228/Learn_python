def test26():
    a = "Python"
    b = a[ : : -1 ][ : : -1 ]
    print( "a =" , a )
    print( "b =" , b )

    print(id( a ))
    print(id( b )) 