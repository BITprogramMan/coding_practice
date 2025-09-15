class Solution:
    """
    给你一个字符串类型的数组arr，譬如：
    String[] arr = { "b\\cst", "d\\", "a\\d\\e", "a\\b\\c" };
    你把这些路径中蕴含的目录结构给画出来，子目录直接列在父目录下面，并比父目录
    向右进两格，就像这样:
    a
        b
            c
        d
            e
    b
        cst
    d
    同一级的需要按字母顺序排列，不能乱。
    """
from collections import OrderedDict

class Node:
    def __init__(self, name):
        self.name = name
        # 使用 OrderedDict 模拟 Java 的 TreeMap（按键排序）
        self.next_map = OrderedDict()

def print_folder_tree(folder_paths):
    if folder_paths is None or len(folder_paths) == 0:
        return
    head = generate_folder_tree(folder_paths)
    print_process(head, 0)

def generate_folder_tree(folder_paths):
    head = Node("")
    for fold_path in folder_paths:
        # Java 中是 "\\"，但在 Python 字符串中需转义为 "\\\\"
        # 实际在 Python 中用单反斜杠分割，直接用 "\\" 即可（因为字符串字面量中 \ 是转义符）
        paths = fold_path.split("\\")
        cur = head
        for path in paths:
            if path not in cur.next_map:
                cur.next_map[path] = Node(path)
            cur = cur.next_map[path]
    return head

def print_process(node, level):
    if level != 0:
        print(get_2n_space(level) + node.name)
    # 遍历子节点（按插入顺序，因为用的是 OrderedDict）
    for child in node.next_map.values():
        print_process(child, level + 1)

def get_2n_space(n):
    res = ""
    for i in range(1, n):  # 注意：原 Java 是 i < n，从 1 开始，所以是 n-1 个 "  "
        res += "  "
    return res

if __name__ == "__main__":
    arr = ["b\\cst", "d\\", "a\\d\\e", "a\\b\\c"]
    print_folder_tree(arr)