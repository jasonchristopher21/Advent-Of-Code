class Main:

    max_sums = []
    lines = None

    def main(self):

        curr_sum = 0
        
        with open(r'inputs/calorie_counting_input.txt', 'r') as f:
            self.lines = f.readlines()
            self.lines.append("\n")

        for line in self.lines:
            if line == "\n":
                self.update_array(curr_sum)
                curr_sum = 0
                continue

            curr_sum += int(line)
        
        print(self.sum())
                    
    def update_array(self, value):
        
        for i in range(len(self.max_sums)):
            if value > self.max_sums[i]:
                self.max_sums.insert(i, value)
                self.remove_last_element()
                return None

        self.max_sums.append(value)
        self.remove_last_element()
        
    def remove_last_element(self):
        if (len(self.max_sums) > 3):
            self.max_sums.pop()
                
    def sum(self):
        sums = 0
        for num in self.max_sums:
            sums += num
        return sums

if __name__ == '__main__':
    Main().main()