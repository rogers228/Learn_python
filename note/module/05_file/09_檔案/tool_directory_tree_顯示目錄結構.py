import os
import fnmatch

def describe_directory_tree(path, ignore=None, prune=None):

    if ignore is None:
        ignore = [
            ".git", ".gitattributes",
            "__pycache__", "*.pyc",
        ]

    if prune is None:
        prune = ["node_modules"]

    def match(name, rules):
        return any(fnmatch.fnmatch(name, rule) for rule in rules)

    def walk(current_path, prefix):
        lines = []

        try:
            entries = sorted(
                os.listdir(current_path),
                key=lambda name: (
                    not os.path.isdir(os.path.join(current_path, name)),
                    name.lower()
                )
            )
        except PermissionError:
            return lines

        entries = [e for e in entries if not match(e, ignore)]

        for index, name in enumerate(entries):
            full_path = os.path.join(current_path, name)
            is_last = index == len(entries) - 1

            connector = "└─ " if is_last else "├─ "
            display_name = name + "/" if os.path.isdir(full_path) else name
            lines.append(prefix + connector + display_name)

            if os.path.isdir(full_path) and not match(name, prune):
                extension = "   " if is_last else "│  "
                lines.extend(
                    walk(full_path, prefix + extension)
                )

        return lines

    root_name = os.path.basename(os.path.abspath(path))
    result = [f"{root_name}/"]
    result.extend(walk(path, ""))

    return "\n".join(result)


def test1():
    target = r'C:\Users\user\Documents\Rogers\ispc_mailbot'
    print(describe_directory_tree(target))

if __name__ == '__main__':
    test1()