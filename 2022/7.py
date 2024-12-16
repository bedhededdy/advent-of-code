# NOTE: MIGHT BE LESS OF A PAIN IN THE ASS AND REQUIRE LESS PASSES IF DONE ITERATIVELY

# n-ary tree object that stores it's parent
# stores it's children as a dict of names (strings) that map to their
# associated Trees
class Tree:
    def __init__(self, name, parent=None, bytes=0):
        self.name = name
        self.parent = parent
        self.bytes = bytes

        self.children = {}

    def add_child(self, child, parent, bytes=0):
        self.children[child] = Tree(child, parent, bytes)

    def is_dir(self):
        return len(self.children) > 0

def get_input():
    with open('7.txt', 'r') as f:
        inp_lines = f.read().splitlines()
    return inp_lines

def fill_dir_sizes(root):
    # directory we haven't calculated the size of
    if root.bytes == 0:
        sz = 0
        for _, child in root.children.items():
            if child.is_dir():
                fill_dir_sizes(child)
            sz += child.bytes
        root.bytes = sz

def sum_small_dirs(root):
    sm = 0
    if root.bytes <= 100_000:
        sm += root.bytes
    for _, child in root.children.items():
        if child.is_dir():
            sm += sum_small_dirs(child)
    return sm

def part1():
    inp_lines = get_input()

    root = Tree('/')
    cwd = root

    for line in inp_lines:
        # command
        if line[0] == '$':
            line = line.split(' ')

            # cd
            if len(line) == 3:
                if line[2] == '..':
                    cwd = cwd.parent
                elif line[2] == '/':
                    cwd = root
                else:
                    cwd = cwd.children[line[2]]
            # ls
            else:
                pass
        # ls output
        else:
            line = line.split(' ')

            if line[0] == 'dir':
                cwd.add_child(line[1], cwd)
            else:
                cwd.add_child(line[1], cwd, int(line[0]))

    print(fill_dir_sizes(root))
    print(sum_small_dirs(root))
    return root

# finds all directories large enough such that if they were to be deleted
# the update could be installed
def update_directories(root, lst, mem):
    if 30_000_000 <= 70_000_000 - mem + root.bytes:
        lst.append(root.bytes)
        for _, child in root.children.items():
            if child.is_dir():
                update_directories(child, lst, mem)
    return lst

def part2():
    root = part1()
    lst = []
    update_directories(root, lst, root.bytes)
    print(min(lst))

# both parts done in O(n), but use many passes where less would suffice
def main():
    part2()

if __name__ == '__main__':
    main()
