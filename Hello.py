

def generate_fibonacii(no_of_elements: int):

    fib_series = [0,1]

    if( no_of_elements == 2 ):
        return fib_series
    else:
        i = 3
        while( i <= no_of_elements ):
            fib_series.append( fib_series[-1]  + fib_series[-2] )
            i = i + 1

    return fib_series

if __name__ == '__main__':    
    no_of_elements = input("Enter the total number of elements in the series: ")
    print( generate_fibonacii( int(no_of_elements) ) )