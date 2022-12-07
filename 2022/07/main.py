class Directory:
    def __init__(self, name: str, parent=None, _depth=0):
        self.name = name
        self.content = []
        self.parent = parent
        self.depth = _depth

    def add(self, item):
        self.content.append(item)

    def get_name(self):
        return f"[{self.name}]"

    def tree(self, level=0, with_size=False):
        print("  " * level + self.get_name())
        for item in self.content:
            item.tree(level + 2, with_size)

    def get_size(self):
        return sum([item.get_size() for item in self.content])


class File:
    def __init__(self, name: str, _size: int, _depth=0):
        self.name = name
        self.size = _size
        self.depth = _depth

    def get_size(self):
        return self.size

    def get_name(self):
        return self.name

    def tree(self, level=0, with_size=False):
        print("  " * level + self.get_name() + (f" ({self.size})" if with_size else ""))


def find_dirs(directory: Directory):
    directories = []
    for item in directory.content:
        if isinstance(item, Directory):
            directories.append(item)
            directories += find_dirs(item)
    return directories


data = [line.strip() for line in open("input", "r").readlines()]
root = Directory("/")
current_dir = root
commands, current_command = [], None
for line in data:
    if line.startswith("$"):
        if current_command is not None:
            commands.append(current_command)
        current_command = {
            "command": line.split(" ")[1], "params": line.split(" ")[2:], "output": [],
        }
    else:
        current_command["output"].append(line)
commands.append(current_command)

for command in commands:
    match command["command"]:
        case "cd":
            if command["params"][0] == "..":
                current_dir = current_dir.parent
            elif command["params"][0] == "/":
                current_dir = root
            else:
                current_dir = Directory(command["params"][0], current_dir, current_dir.depth + 1)
                if current_dir not in current_dir.parent.content:
                    current_dir.parent.add(current_dir)
        case "ls":
            for line in command["output"]:
                if not line.startswith("dir "):
                    size, file = line.split(" ")
                    current_dir.add(File(file, int(size), current_dir.depth + 1))


# Part 1

directories = find_dirs(root)
directories = [directory for directory in directories if directory.get_size() <= 100000]
print(sum([directory.get_size() for directory in directories]))

# Part 2

needed = 30000000 - (70000000 - root.get_size())
directories = find_dirs(root)
directories = [directory for directory in directories if directory.get_size() >= needed]
directories.sort(key=lambda directory: directory.get_size())
print(directories[0].get_size())
