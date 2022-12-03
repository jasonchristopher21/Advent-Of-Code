def main():

    lines = None
    max_sum, curr_sum = 0, 0

    with open(r'inputs/calorie_counting_input.txt', 'r') as f:
        lines = f.readlines()
        lines.append("\n")

    for line in lines:

        if line == "\n":
            max_sum = max(max_sum, curr_sum)
            curr_sum = 0
            continue

        curr_sum += int(line)
    
    print(max_sum)

if __name__ == '__main__':
    main()