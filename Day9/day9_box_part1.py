def main():
    input_array=[]
    with open("F:\Ardent-of-Code-2025\Day9\input_sample.txt") as file:
        for line in file.readlines():
            l , r = line.split(',')
            input_array.append([int(l),int(r)])

    input_array.sort()
    
    print(input_array)
    
    
if __name__=="__main__":
    main()