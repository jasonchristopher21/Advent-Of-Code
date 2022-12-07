class Directory:

    # Constructs a Directory instance
    def __init__(self, dir_name, parent_dir):
        self.name = dir_name
        self.size = 0
        self.parent_dir = parent_dir
        self.subdirectories = {}
        self.count = 0
        self.minimum = float('inf')
    
    def add_directory(self, dirs):
        dir_name = dirs.name
        self.subdirectories[dir_name] = dirs
    
    def add_file(self, file):
        file = file.split()
        size = int(file[0])
        self.update_size(size)

    def update_size(self, size):
        self.size += size
        if self.parent_dir:
            self.parent_dir.update_size(size)
    
    def change_directory(self, dir_name):
        return self.subdirectories[dir_name]

    # PART 1
    def traverse(self): 
        """
        Traverses each directory in the sub-directories to find the required sizes.

        Traverses each directory in the sub-direcotries to find the sizes of subdirectories
        that are less than 100000, before checking to the current directory.
        Algorithm is similar to Depth-First Search traversal

        Returns
        -------
        int
            The total sizes of the current directory and subdirectories whose respective size
            is less than 100,000
        """
        for key in self.subdirectories.keys():
            dirs = self.subdirectories[key]
            dirs.traverse()
            self.count += dirs.count
        if self.size <= 100000:
            self.count += self.size
        # print("Directory: ", self.name, " Size: ", self.size)
        return self.count    

    # PART 2:
    def traverse_minimum(self, min_to_delete): 
        """
        Traverses each directory in the sub-directories to find the minimum size sufficient to delete.

        Similar to the traverse function in Part 1, traverse_minimum stores the running minimum
        size as a `minimum` field stored in each Directory object. The `minimum` field is updated
        if a directory of size greater than or equal to the minimum size to delete is found.

        Parameters
        ----------
        min_to_delete
            An integer to represent the minimum size of the directory required to delete

        Returns
        -------
        int
            The size of the directory with the lowest sufficient size to be deleted
        """
        for key in self.subdirectories.keys():
            dirs = self.subdirectories[key]
            dirs.traverse_minimum(min_to_delete)
            self.minimum = min(self.minimum, dirs.minimum)
        if self.size >= min_to_delete:
            self.minimum = min(self.minimum, self.size)
        return self.minimum
             
class Solution:

    past_dir_stack = []
    main_dir = Directory("/", None)
    curr_dir = main_dir

    lines = None

    def main(self):

        with open(r'inputs/no_space_left_inputs.txt', 'r') as f:
            self.lines = f.readlines()

        while self.lines:
            line = self.lines.pop(0)
            if line[0] == "$":
                self.parse_command(line.strip())
            elif line[0] == "d":
                self.parse_directory(line.strip())
            else:
                self.parse_file(line.strip())

        # PART 1
        part1_value = self.main_dir.traverse()
        print("Part 1: ", part1_value)

        # PART 2
        min_to_delete = self.main_dir.size - 40000000
        part2_value = self.main_dir.traverse_minimum(min_to_delete)
        print("Part 2: ", part2_value)
        
    def parse_command(self, line):
        line = line.split()
        if line[1] == "cd":
            self.parse_change_directory(line[2])

    def parse_change_directory(self, target_dir):
        if target_dir == "..":
            self.curr_dir = self.past_dir_stack.pop()
        elif target_dir == "/":
            self.curr_dir = self.main_dir
            self.past_dir_stack = []
        else:
            self.past_dir_stack.append(self.curr_dir)
            self.curr_dir = self.curr_dir.change_directory(target_dir)

    def parse_directory(self, line):
        line = line.split()
        dirs = Directory(line[1], self.curr_dir)
        self.curr_dir.add_directory(dirs)
    
    def parse_file(self, line):
        self.curr_dir.add_file(line)

if __name__ == "__main__":
    Solution().main()