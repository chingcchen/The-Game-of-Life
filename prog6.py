## prog6
## Ching Chen
## Mar 11, 2016

## The Game of Life part1

def count_neighbor(glider):
    """this function counts the number of the neighbors of each cell"""
    m = len(glider)
    n = len(glider[0])
    C = [[0,]*m for i in range(n)]
    for x in range(1,m-1):
        for y in range(1,n-1):
            C[x][y] = glider[x-1][y-1] +glider[x][y-1] +glider[x+1][y-1] \
                     +glider[x-1][y]                   +glider[x+1][y] \
                     +glider[x-1][y+1] +glider[x][y+1] +glider[x+1][y+1]                     
    return C

def nextGen(glider):
    """this function expects only one argument which is a two-dimensional table
       (i.e., a list of lists) with m rows and n columns, representing the
       current grid. The elements of the table are either 0 (empty square)
       or 1 (occupied square) """
    m = len(glider)
    n = len(glider[0])
    C = count_neighbor(glider)
    nextG = [[0 for col in glider[0]] for row in glider]
    for x in range(1, m-1):
        for y in range(1, n-1):
            if glider[x][y] == 0 and C[x][y] == 3:
                nextG[x][y] = 1
            elif glider[x][y] == 1 and (C[x][y] == 2 or C[x][y] == 3):
                nextG[x][y] = 1
    return nextG


def graph(data):
    """this function expect an argument which is data text form, and it will
       tranform the data to a two-dimensional graph composed of '.' & '*'"""
    output = ""
    m = len(data)
    n = len(data[0])
    for x in range(0, m):
        for y in range(0, n):
            if data[x][y] == 0:
                output += ' .'
            else:
                output += ' *'
        output += '\n'

    return output

            

## The Game of Life part2
def life():
    """This function reads data for the initial grid from a text file,
       prints some number of generations of new grids, and then saves the most
       recent generation to a text file. """
    while True:
        filename = input("Enter input file name: ")
        try:
            inFile = open(filename, "r")
            break
        except:
            print("No such file. Try again.")

    while True:
        gen = input("How many new generations would you like to print? ")
        try:
            gen = int(gen)
            break
        except:
            print("Not a valid number.")
            

    new_glider = []
    for line in inFile:
        new_row = [0]
        for value in line:
            if value != "\n": 
                new_row.append(int(value))
        new_row.append(0)
        new_glider.append(new_row)

    zero_row = [0 for col in range(len(new_glider[0]))]
    new_glider.append(zero_row)
    new_glider.insert(0, zero_row)
    

        
    
    count = 0
    while count <= gen:
        small_glider = []
        for i in range(1, len(new_glider)-1):
            new_row = []
            for j in range(1, len(new_glider[0])-1):
                new_row.append(new_glider[i][j])
            small_glider.append(new_row)


        print("\n" + "Generation: ", count)
        print(graph(small_glider))
        new_glider = nextGen(new_glider)
        count += 1 
                    



    ans = input("Would you like to save the latest generation? ('y' to save): ")
    if ans == 'y':
        while True:
            dfilename = input("Enter destination file name: ")
            try:
                open(dfilename, "r")
                ny = input("Do you want to overwrite that file? ('y' to continue): ")
                if ny != "y":
                    pass
                else:
                    break
         
            except:
                break
        print("\n"+"Saving data to ", dfilename, "\n")
                

        with open(dfilename, "w") as outputfile:
            for row in small_glider:
                row_string = ""
                for char in row:
                    row_string = row_string + str(char)
                outputfile.write(row_string + "\n")

    print("End of program.")

