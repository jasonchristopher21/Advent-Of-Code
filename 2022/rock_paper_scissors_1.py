def main():

    lines = None
    sums = 0

    with open(r'inputs/rock_paper_scissors_input.txt', 'r') as f:
        lines = f.readlines()
        lines.append("\n")

    for line in lines:

        opp, you = 0, 0

        inputs = line.split()

        if not inputs:
            break
        
        match inputs[0]:
            case "A":
                opp = 1
            case "B":
                opp = 2
            case "C":
                opp = 3
        
        match inputs[1]:
            case "X":
                you = 1
            case "Y":
                you = 2
            case "Z":
                you = 3
        
        if (you - opp) % 3 == 1:
            sums += 6
        elif you == opp:
            sums += 3
        
        sums += you
    
    print(sums)

if __name__ == "__main__":
    main()