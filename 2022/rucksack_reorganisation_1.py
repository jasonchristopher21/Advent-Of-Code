def main():

    lines = None
    sums = 0

    with open(r'inputs/rucksack_reorganisation_input.txt', 'r') as f:
        lines = f.readlines()

    for line in lines:
        compartment_length = len(line) // 2
        compartment1 = set(line[:compartment_length])
        compartment2 = set(line[compartment_length:])
        intersection = compartment1.intersection(compartment2)
        for item in intersection:
            sums += toPriorityValue(item)

    print(sums)
        
def toPriorityValue(letter):
    if letter == letter.lower():
        return ord(letter) - ord("a") + 1
    return ord(letter) - ord("A") + 27

if __name__ == "__main__":
    main()