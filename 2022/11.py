class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = Node(0)
        self.tail = self.head
        self.length = 0

    def append(self, val):
        self.tail.next = Node(val)
        self.tail = self.tail.next
        self.length += 1

    def poll(self):
        tmp = self.head.next.val
        self.head.next = self.head.next.next
        self.length -= 1
        if self.length == 0:
            self.tail = self.head
        return tmp

    def __len__(self):
        return self.length

    def __str__(self):
        node = self.head.next
        ret = ''
        while node:
            print(type(node.val))
            ret += str(node.val) + ' '
            node = node.next
        return ret

class Monkey:
    def __init__(self, items, operation, test):
        self.items = LinkedList()
        for item in items:
            self.items.append(item)
        self.operation = operation
        self.test = test

        self.true_monkey = None
        self.false_monkey = None

    def inspect(self):
        val = self.items.poll()
        val = self.operation(val)
        #val //= 3          # PART 1 only
        # if we divide by the lcm of all the test values
        # we get no change in the results of the tests
        # and keep our numbers workably big.
        # without mod, they get too large for part 2
        val %= 2*3*5*7*11*13*17*19
        if self.test(val):
            self.true_monkey.items.append(val)
        else:
            self.false_monkey.items.append(val)  


def get_input():
    with open('11.txt', 'r') as f:
        inp_lines = f.read().splitlines()
    return inp_lines

def part1():
    m0 = Monkey([91, 58, 52, 69, 95, 54], lambda x: x*13, lambda x: x%7 == 0)
    m1 = Monkey([80, 80, 97, 84], lambda x: x*x, lambda x: x%3 == 0)
    m2 = Monkey([86, 92, 71], lambda x: x+7, lambda x: x%2 == 0)
    m3 = Monkey([96, 90, 99, 76, 79, 85, 98, 61], lambda x: x+4, lambda x: x%11 == 0)
    m4 = Monkey([60, 83, 68, 64, 73], lambda x: x*19, lambda x: x%17 == 0)
    m5 = Monkey([96, 52, 52, 94, 76, 51, 57], lambda x: x+3, lambda x: x%5 == 0)
    m6 = Monkey([75], lambda x: x+5, lambda x: x%13 == 0)
    m7 = Monkey([83, 75], lambda x: x+1, lambda x: x%19 == 0)

    m0.true_monkey = m1
    m0.false_monkey = m5
    m1.true_monkey = m3
    m1.false_monkey = m5
    m2.true_monkey = m0
    m2.false_monkey = m4
    m3.true_monkey = m7
    m3.false_monkey = m6
    m4.true_monkey = m1
    m4.false_monkey = m0
    m5.true_monkey = m7
    m5.false_monkey = m3
    m6.true_monkey = m4
    m6.false_monkey = m2
    m7.true_monkey = m2
    m7.false_monkey = m6

    inspections = [0] * 8
    monkeys = [m0, m1, m2, m3, m4, m5, m6, m7]

    for _ in range(20):
        for i, monkey in enumerate(monkeys):
            inspections[i] += len(monkey.items)
            while len(monkey.items) > 0:
                monkey.inspect()

    inspections = sorted(inspections)
    print(inspections[-1] * inspections[-2])

def part2():
    m0 = Monkey([91, 58, 52, 69, 95, 54], lambda x: x*13, lambda x: x%7 == 0)
    m1 = Monkey([80, 80, 97, 84], lambda x: x*x, lambda x: x%3 == 0)
    m2 = Monkey([86, 92, 71], lambda x: x+7, lambda x: x%2 == 0)
    m3 = Monkey([96, 90, 99, 76, 79, 85, 98, 61], lambda x: x+4, lambda x: x%11 == 0)
    m4 = Monkey([60, 83, 68, 64, 73], lambda x: x*19, lambda x: x%17 == 0)
    m5 = Monkey([96, 52, 52, 94, 76, 51, 57], lambda x: x+3, lambda x: x%5 == 0)
    m6 = Monkey([75], lambda x: x+5, lambda x: x%13 == 0)
    m7 = Monkey([83, 75], lambda x: x+1, lambda x: x%19 == 0)

    m0.true_monkey = m1
    m0.false_monkey = m5
    m1.true_monkey = m3
    m1.false_monkey = m5
    m2.true_monkey = m0
    m2.false_monkey = m4
    m3.true_monkey = m7
    m3.false_monkey = m6
    m4.true_monkey = m1
    m4.false_monkey = m0
    m5.true_monkey = m7
    m5.false_monkey = m3
    m6.true_monkey = m4
    m6.false_monkey = m2
    m7.true_monkey = m2
    m7.false_monkey = m6

    inspections = [0] * 8
    monkeys = [m0, m1, m2, m3, m4, m5, m6, m7]

    for _ in range(10_000):
        for i, monkey in enumerate(monkeys):
            inspections[i] += len(monkey.items)
            while len(monkey.items) > 0:
                monkey.inspect()

    inspections = sorted(inspections)
    print(inspections[-1] * inspections[-2])

def main():
    part1()
    part2()

if __name__ == '__main__':
    main()
