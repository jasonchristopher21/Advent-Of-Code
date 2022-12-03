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
                opp = 0
            case "B":
                opp = 1
            case "C":
                opp = 2
        
        match inputs[1]:
            case "X":
                # "lose case"
                you = (opp - 1) % 3 + 1
                sums += you
            case "Y":
                # "draw case"
                you = opp + 1
                sums += 3 + you
            case "Z":
                # "win case"
                you = (opp + 1) % 3 + 1
                sums += 6 + you
                
    print(sums)

if __name__ == "__main__":
    main()