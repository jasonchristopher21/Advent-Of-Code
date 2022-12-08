def main():

    lines = None

    with open(r'inputs/treetop_tree_house_inputs.txt', 'r') as f:
        lines = f.readlines()

    rows = len(lines)
    cols = len(lines[0].strip())

    trees = []
    max_scenic = -1

    # Initialise 2D List from inputs
    for line in lines:
        tree_row = []
        line = line.strip()
        for tree in line:
            tree_row.append(int(tree))
        trees.append(tree_row)

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            tree = trees[i][j]

            left_count = 0
            right_count = 0
            top_count = 0
            bottom_count = 0

            for u in range(i):
                top_count += 1
                if trees[i - u - 1][j] >= tree:
                    break
            
            for d in range(rows - i - 1):
                bottom_count += 1
                if trees[i + d + 1][j] >= tree:
                    break

            for l in range(j):
                left_count += 1
                if trees[i][j - l - 1] >= tree:
                    break
            
            for r in range(cols - j - 1):
                right_count += 1
                if trees[i][j + r + 1] >= tree:
                    break

            scenic = top_count * bottom_count * left_count * right_count
            max_scenic = max(max_scenic, scenic)
    
    print(max_scenic)

if __name__ == "__main__":
    main()