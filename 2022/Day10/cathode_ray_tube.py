def main():

    count = -1
    x = 1

    stall = 0
    temp = 0

    lines = None

    sums = 0

    text = ""

    with open(r'inputs/cathode_ray_tube_inputs.txt', 'r') as f:
        lines = f.readlines()

    while True:

        # start of cycle
        count += 1

        # during cycle, check if cycle num is 20 or 60 or 100 or etc.
        if count % 40 == 20:
            sums += x * count

        # PART 2 --------------------------------------------
        if x - 1 <= (count - 1) % 40 <= x + 1:
            text += "#"
        else:
            text += "."
        
        if count > 20 and count % 40 == 0:
            text += "\n"

        # PART 1 --------------------------------------------
        if stall:
            stall -= 1
            continue

        if temp:
            x += temp
            temp = 0

        if not lines:
            break

        line = lines.pop(0)

        if line[:4] == "addx":
            line = line.strip().split()
            temp = int(line[1])
            stall = 1   # set stall value to 1 cycle
            continue

    # PART 1
    print("Part 1:", sums)

    # PART 2
    print("Part 2:")
    print(text[1:])

if __name__ == "__main__":
    main()

