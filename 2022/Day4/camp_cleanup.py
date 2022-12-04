def main():

    lines = None
    sums = 0

    with open(r'inputs/camp_cleanup_input.txt', 'r') as f:
        lines = f.readlines()

    for line in lines:
        line = line.replace("\n", "")
        elves = line.split(",")
        elf_1 = elves[0].split("-")
        elf_2 = elves[1].split("-")

        # Part 1: Check for Fully Contains
        # if checkContains(elf_1, elf_2):
        #     print(elf_1, elf_2)
        #     sums += 1

        # Part 2: Check for overlaps
        if checkOverlap(elf_1, elf_2):
            print(elf_1, elf_2)
            sums += 1

    print(sums)
        
def checkContains(a, b):
    lo_a = int(a[0])
    lo_b = int(b[0])

    hi_a = int(a[1])
    hi_b = int(b[1])

    if (lo_b <= lo_a <= hi_b) and (lo_b <= hi_a <= hi_b):
        return True
    elif (lo_a <= lo_b <= hi_a) and (lo_a <= hi_b <= hi_a):
        return True
    return False

def checkOverlap(a, b):
    lo_a = int(a[0])
    lo_b = int(b[0])

    hi_a = int(a[1])
    hi_b = int(b[1])

    if (lo_b <= lo_a <= hi_b) or (lo_b <= hi_a <= hi_b):
        return True
    elif (lo_a <= lo_b <= hi_a) or (lo_a <= hi_b <= hi_a):
        return True
    return False

if __name__ == "__main__":
    main()