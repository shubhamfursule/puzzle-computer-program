lpuzzle=[13234,32131,52416,92405,92321,32344,22454,72345,52085,62422]
def puzzle_program(listpuzzle):
    a=[]
    for i in range(len(listpuzzle)):
        a.append(str(listpuzzle[i]))
    z=0
    for x in range(len(a[z])):
        list_puz=[]
        for y in range(len(a)):
            list_puz.append(a[y][x])
        if list_puz.count(list_puz[x])==len(a):
            return int(list_puz[x]), x+1
            break
    else :
        return "there is no value common in digits","\n try another"
common_no,position  =  puzzle_program(lpuzzle)
print(f"the common number is :{common_no} on index of {position}")    

