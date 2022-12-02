def main():

    dimensions = None
    max_sum, curr_sum = 0, 0

    f = open("E:\Jason\Code\Advent-Of-Code\\2015\day2inputs.txt","r")
    dimensions = f.readlines()

    sums = 0

    for d in dimensions:
        dims = d.split("x")

        l = int(dims[0])
        w = int(dims[1])
        h = int(dims[2])

        a1 = l * w
        a2 = l * h
        a3 = w * h

        slack = min(a1, a2, a3)
        sums += 2 * (a1 + a2 + a3) + slack
    
    print(sums)

if __name__ == '__main__':
    main()