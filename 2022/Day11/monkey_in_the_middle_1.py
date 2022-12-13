class Solution:

    lines = None
    monkeys = []

    curr_monkey = -1

    rounds = 20
    monkey_count = 0

    def main(self):

        with open(r'inputs/monkey_in_the_middle_inputs.txt', 'r') as f:
            self.lines = f.readlines()
        
        for line in self.lines:
            self.parse(line)

        self.curr_monkey = 0

        while self.rounds:

            if self.curr_monkey == len(self.monkeys):
                self.curr_monkey = 0
                self.rounds -= 1
                # if self.rounds == 19:
                #     self.print_monkey_for_debug()
                continue
            
            # Monkey inspect
            monkey = self.monkeys[self.curr_monkey]

            if not monkey["items"]:
                self.curr_monkey += 1
                continue

            while monkey["items"]:

                item = monkey["items"].pop(0)

                new_level, left, right = None, None, None

                operation_tree = monkey["operation"].split()

                # Check left operand
                if operation_tree[2] == "old":
                    left = item
                else:
                    left = int(operation_tree[2])
                
                # Check right operand
                if operation_tree[4] == "old":
                    right = item
                else:
                    right = int(operation_tree[4])

                # Check operand, get new worry level
                match operation_tree[3]:
                    case "+":
                        new_level = left + right
                    case "-":
                        new_level = left - right
                    case "*":
                        new_level = left * right
                    case "/":
                        new_level = left / right

                # Reduce worry level by 1/3
                new_level = new_level // 3

                # Test worry level
                next_monkey_id = -1

                if new_level % int(monkey["test"].split()[2]) == 0:
                    next_monkey_id = monkey["condition"][0]
                else:
                    next_monkey_id = monkey["condition"][1]
                
                next_monkey = self.monkeys[next_monkey_id]
                next_monkey["items"].append(new_level)

                if "activity" not in monkey.keys():
                    monkey["activity"] = 0
                
                monkey["activity"] += 1

            self.monkey_count += 1
            self.curr_monkey += 1

        value = self.retrieve_sorted_value()
        print(value)

    def print_monkey_for_debug(self):
        for monkey in self.monkeys:
            print("Monkey", monkey["id"], ":", monkey["items"])

    def parse(self, line):
        line = line.strip()

        if line.startswith("Monkey"):
            self.monkeys.append({})
            monkey_id = line[7 : len(line) - 1]
            self.curr_monkey = int(monkey_id)
            self.monkeys[self.curr_monkey]["id"] = self.curr_monkey

        elif line.startswith("Starting"):
            items = []
            line = line.replace(",", "").split()

            for i in range(2, len(line)):
                items.append(int(line[i]))
            
            self.monkeys[self.curr_monkey]["items"] = items
        
        elif line.startswith("Operation"):
            self.monkeys[self.curr_monkey]["operation"] = line[11:]
        
        elif line.startswith("Test"):
            self.monkeys[self.curr_monkey]["test"] = line[6:]

        elif line.startswith("If"):
            if "condition" not in self.monkeys[self.curr_monkey].keys():
                self.monkeys[self.curr_monkey]["condition"] = []
            self.monkeys[self.curr_monkey]["condition"].append(int(line[len(line) - 1 :]))

    def retrieve_sorted_value(self):

        activity_levels = []
        
        for monkey in self.monkeys:
            if "activity" not in monkey.keys():
                monkey["activity"] = 0
            activity_levels.append(monkey["activity"])

        activity_levels = list(reversed(sorted(activity_levels)))

        return activity_levels[0] * activity_levels[1]


if __name__ == "__main__":
    Solution().main()