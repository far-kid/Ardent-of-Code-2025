import numpy as np

def main():
    input_arr=[]
    operators = None
    with open(r"F:\Ardent-of-Code-2025\Day6\input.txt") as file:
        for line in file:
            parts = line.split()
            try:
                row = list(map(int, parts))
                input_arr.append(row)
            except ValueError:
                # skip lines that contain non-integer values
                operators = parts
    numpy_in_arr = np.array(input_arr)
    transposed = numpy_in_arr.T
    final_sum = 0
    for i in range(len(transposed)):
        op = operators[i]
        if op =='*':
            mult  = 1
            for j in range(len(transposed[0])):
                mult*=transposed[i][j]
            final_sum+=mult
        else:
            addn = 0
            for j in range(len(transposed[0])):
                addn+=transposed[i][j]
            final_sum+=addn    
    # print(input_arr[0])
    print(final_sum)

if __name__=="__main__":
    main() 