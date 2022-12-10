class Solution:

    visited = []
    visited_count = 0

    lines = None

    head = (0, 0)
    tail = (0, 0)

    def main(self):

        with open(r'inputs/rope_bridge_inputs.txt', 'r') as f:
            self.lines = f.readlines()

        self.visited.append(self.tail)
        self.visited_count += 1

        for line in self.lines:
            line = line.strip()
            splitted_line = line.split()
            
            direction = splitted_line[0]
            amount = int(splitted_line[1])

            self.move(direction, amount)

        print(self.visited_count)

        # print(self.visited)

    def move(self, direction, amount):

        if amount == 0:
            return 0
            
        match direction:
            case "R":
                self.head = (self.head[0] + 1, self.head[1])
            case "L":
                self.head = (self.head[0] - 1, self.head[1])
            case "U":
                self.head = (self.head[0], self.head[1] + 1)
            case "D":
                self.head = (self.head[0], self.head[1] - 1)
        
        if not self.is_following():
            # do something
            if self.is_following_x() and not self.is_following_y(): #PROBLEMATIC HERE
                self.tail = (self.head[0], self.tail[1] + self.adjustment(1))
            elif self.is_following_y() and not self.is_following_x():
                self.tail = (self.tail[0] + self.adjustment(0), self.head[1])
            # print(self.is_following_x())
            # print(self.is_following_y())
            # print(self.head)
            # print(self.tail)
            if self.tail not in self.visited:
                self.visited.append(self.tail)
                self.visited_count += 1

        return self.move(direction, amount - 1)
    
    def is_following(self):
        return self.is_following_x() and self.is_following_y()

    def is_following_x(self):
        return -1 <= self.head[0] - self.tail[0] <= 1
    
    def is_following_y(self):
        return -1 <= self.head[1] - self.tail[1] <= 1

    def adjustment(self, num):
        return (self.head[num] - self.tail[num]) // 2

if __name__ == "__main__":
    Solution().main()