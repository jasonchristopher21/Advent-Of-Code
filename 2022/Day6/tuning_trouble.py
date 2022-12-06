def main():

    lines = None

    with open(r'inputs/tuning_trouble_inputs.txt', 'r') as f:
        lines = f.readlines()[0].strip()

    # Part 1
    if len(lines) < 4:
        print("Part 1 not fulfilled: Length less than 4. Received length: ", len(lines))
        return None

    for i in range(len(lines) - 3):
        sample_set = set([lines[i], lines[i + 1], lines[i + 2], lines[i + 3]])
        if len(sample_set) == 4:
            print("Part 1: ", i + 4)
            break

    # Part 2    
    if len(lines) < 14:
        print("Part 2 not fulfilled: Length less than 14. Received length: ", len(lines))
        return None

    for i in range(len(lines) - 13):
        sample_set = set()
        for j in range(i, i + 14):
            sample_set.add(lines[j])
        if len(sample_set) == 14:
            print("Part 2: ", i + 14)
            return None

    print(-1)

if __name__ == "__main__":
    main()