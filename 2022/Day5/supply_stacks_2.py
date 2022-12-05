class Main:

    stacks = {}
    lines = None
    stack_temp = []

    def main(self):

        res = ""

        with open(r'inputs/supply_stacks_input.txt', 'r') as f:
            self.lines = f.readlines()

        for line in self.lines:
            # Start to initiate the stacks if encounter the row with stack numbers
            if line[1] == "1":
                self.initiateStacks(line.strip())
                break
            # Before encountering this row, keep all "containers" in a separate stack
            else:
                self.stack_temp.append(line)
        
        for line in self.lines:
            # Only evaluate the moving of containers if the string starts with "move"
            # Assume all inputs are valid based on the provided input
            if line[0] != "m":
                continue

            line = line.strip().split()

            amount = int(line[1])
            src = line[3]
            dest = line[5]
                
            # PART 2 LOGIC:
            # Keep the popped elements in a temporary stack, then pop each element from this
            # stack to retain the order. Trade-off: More memory needed
            # Alternative considered: Replacing all stack logic in self.stacks with a queue
            temp_stack = []
            for i in range(amount):
                temp_stack.append(self.stacks[src].pop())
            while temp_stack:
                self.stacks[dest].append(temp_stack.pop())
            
        for key in self.stacks.keys():
            item = self.stacks[key].pop()
            res += item[1]

        print(res)

        
    def initiateStacks(self, line: str):
        """
        Initiates the stack of containers

        Parameters
        ----------
        line: str
            The line containing the containers
        """
        stack_numbers = line.split()

        for num in stack_numbers:
            self.stacks[num] = []

        while self.stack_temp:
            row = self.stack_temp.pop()

            for i in range(len(row)):
                if row[i] == "[":
                    num = i // 4 + 1
                    self.stacks[str(num)].append(row[i:i+3])


if __name__ == "__main__":
    Main().main()