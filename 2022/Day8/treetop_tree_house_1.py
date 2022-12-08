def main():

    lines = None

    with open(r'inputs/treetop_tree_house_inputs.txt', 'r') as f:
        lines = f.readlines()

    rows = len(lines)
    cols = len(lines[0].strip())

    visited = []
    trees = []

    count = 0

    for line in lines:
        tree_row = []
        visited_row = []

        line = line.strip()

        for tree in line:
            tree_row.append(int(tree))
            visited_row.append(False)

        trees.append(tree_row)
        visited.append(visited_row)

    for i in range(rows):

        row = trees[i]

        maxval = -float('inf')
        for j in range(cols):
            if row[j] > maxval:
                maxval = row[j]
                if not visited[i][j]:
                    visited[i][j] = True
                    count += 1

        maxval = -float('inf')

        for j in range(cols):
            col = cols - j - 1
            if row[col] > maxval:
                maxval = row[col]
                if not visited[i][col]:
                    visited[i][col] = True
                    count += 1
    
    for j in range(cols):

        maxval = -float('inf')

        for i in range(rows):
            if trees[i][j] > maxval:
                maxval = trees[i][j]
                if not visited[i][j]:
                    visited[i][j] = True
                    count += 1
                    
        maxval = -float('inf')

        for i in range(rows):
            row = rows - i - 1
            if trees[row][j] > maxval:
                maxval = trees[row][j]
                if not visited[row][j]:
                    visited[row][j] = True
                    count += 1

    print(count)

if __name__ == "__main__":
    main()