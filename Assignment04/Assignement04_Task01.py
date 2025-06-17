#TASK - READ A FILE AND HANDLE ERRORS

filename = "sample.txt"
try:
    with open(filename,'r') as filestream:
        print("Reading file content:")
        n = 1
        while(line := filestream.readline()):
            print("line",n,":",line.strip() )
            n+=1
except FileNotFoundError:
   print("Error: File at specified path is not found. Please check the Path and try again")