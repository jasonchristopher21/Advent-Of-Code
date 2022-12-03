def main():

    lines = None
    sums = 0

    with open(r'inputs/rucksack_reorganisation_input.txt', 'r') as f:
        lines = f.readlines()

    for i in range(len(lines) // 3):
        elf_1 = set(lines[3 * i])
        elf_2 = set(lines[3 * i + 1])
        elf_3 = set(lines[3 * i + 2])
        intersection = elf_1.intersection(elf_2, elf_3)
        print(intersection)
        for item in intersection:
            sums += toPriorityValue(item)

    print(sums)
        
def toPriorityValue(letter):
    if letter == "\n":
        return 0
    elif letter == letter.lower():
        return ord(letter) - ord("a") + 1
    elif letter == letter.upper():
        return ord(letter) - ord("A") + 27
    return 0

if __name__ == "__main__":
    main()