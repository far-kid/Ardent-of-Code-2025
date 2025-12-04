row_count = 0
col_count = 0


def get_8_values(row, col_index):
    ##row edge cases
    checking_matrix = [[0] * 2 for _ in range(8)]    
    for i in range(3):
        checking_matrix[i][0]=row-1
        checking_matrix[i][1]=col_index-1+i
    for i in range(3, 6):
        checking_matrix[i][0]=row+1
        checking_matrix[i][1]= col_index-4+i
    for i in range(6,8):
        checking_matrix[i][0]=row
        if i==6:
            checking_matrix[i][1]= col_index-1
        else:
            checking_matrix[i][1]= col_index+1
    return checking_matrix
    
def main():
    paper_rolls = []
    with open(r"F:\Ardent-of-Code-2025\Day4\input.txt") as f:
        paper_rolls = f.read().splitlines()
    
    paper_rolls = [list(line) for line in paper_rolls]
    global row_count
    global col_count

    row_count = len(paper_rolls)
    col_count = len(paper_rolls[0])
        
    # for row in range(row_count):
    #     for col_index in range(col_count):
    #         get_8_values(row,col_index)
    
    paper_count  = 0
    paper_count_old = -1
    for _ in range(100):
        for row in range(row_count):
            for col_index in range(col_count):
                
                if paper_rolls[row][col_index]!='@':
                    continue
                
                else:
                    values = get_8_values(row,col_index)
                    adj_count = 0
                    for value in values:
                        r, c = value[0], value[1]
                        if r < 0 or c < 0 or r >= row_count or c >= col_count:
                            continue
                        else:
                            if paper_rolls[r][c] == '@':
                                adj_count += 1
                    if adj_count<4:
                       # print(row, col_index)
                        paper_count+=1
                        paper_rolls[row][col_index]='.'
        
    print(paper_count)

               
if __name__ == "__main__":
    main()