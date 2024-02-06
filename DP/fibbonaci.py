# Memorization technique
num = 6
memory = [0,1] + [-1]*(num -1)
def get_fibbonaci(num):
    if num < 0:
        print("Incorrect input")

    else:
        if memory[num]!= -1:
            return memory[num]
        else:
            fib = get_fibbonaci(num-2) + get_fibbonaci(num-1)
            memory[num] = fib
            return memory[num]
    
print(get_fibbonaci(6))
print(memory)



FibArray = [0, 1]
 
def fibonacci(n):
   
    # Check is n is less 
    # than 0
    if n < 0:
        print("Incorrect input")
         
    # Check is n is less 
    # than len(FibArray)
    elif n < len(FibArray):
        return FibArray[n]
    else:        
        FibArray.append(fibonacci(n - 1) + fibonacci(n - 2))
        return FibArray[n]
 
# Driver Program
print(fibonacci(9))
print(FibArray)



# Tabulation technique
num = 6

def get_fibbonaci(num):
    fib_table = []
    if num < 0:
        print("Incorrect input")

    else:
        fib_table.append(0)
        fib_table.append(1)
        for n in range(2, num+1):
            fib_num = fib_table[n-2] + fib_table[n-1]
            fib_table.append(fib_num)
        return fib_table
    
print(get_fibbonaci(6))
