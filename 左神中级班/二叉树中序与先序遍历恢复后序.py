class Solution:
    """
    已知一棵二叉树中没有重复节点，并且给定了这棵树的中序遍历数组和先序遍历
    数组，返回后序遍历数组。
    比如给定：
    int[] pre = { 1, 2, 4, 5, 3, 6, 7 };
    int[] in = { 4, 2, 5, 1, 6, 3, 7 };
    返回：
    {4,5,2,6,7,3,1}
    """
    def process(self, nums_in, nums_pre):
        n = len(nums_in)
        nums_post = [None] * n
        map = dict()
        for i in range(n):
            map[nums_in[i]] = i
        def recursive(nums_pre, nums_in, nums_post, map, pre_start, pre_end, in_start, in_end, post_start, post_end):
            if post_start == post_end:
                nums_post[post_end] = nums_in[in_start]
                return
            nums_post[post_end] = nums_pre[pre_start]
            root_idx = map[nums_pre[pre_start]]
            left_tree_node_num = root_idx - in_start
            right_tree_node_num = in_end - root_idx
            recursive(nums_pre, nums_in, nums_post, map, pre_start + 1, pre_start + left_tree_node_num, in_start, in_start + left_tree_node_num - 1, post_start, post_start + left_tree_node_num - 1)
            recursive(nums_pre, nums_in, nums_post, map, pre_end - right_tree_node_num + 1, pre_end, root_idx + 1, in_end, post_end - 1 - right_tree_node_num + 1, post_end - 1)
        recursive(nums_pre, nums_in, nums_post, map, 0, n - 1, 0, n - 1, 0, n - 1)
        return nums_post

if __name__ == '__main__':
    solution = Solution()
    res = solution.process([4, 2, 5, 1, 6, 3, 7], [1, 2, 4, 5, 3, 6, 7])
    print(res)

