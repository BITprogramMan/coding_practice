# import glob


# read_file_list = glob.glob('./*/*py')
# print(len(read_file_list))
import heapq
def compare_replace_methods():
    print("\n=== heapreplace vs heappushpop 对比 ===")
    
    # heapreplace: 先弹出最小值，再插入新值
    heap1 = [2, 4, 5, 8, 9]
    print(f"原始堆1: {heap1}")
    result1 = heapq.heapreplace(heap1, 10)
    print(f"heapreplace(1): 弹出 {result1}, 堆变为 {heap1}")
    
    # heappushpop: 先插入新值，再弹出最小值
    heap2 = [2, 4, 5, 8, 9]
    print(f"原始堆2: {heap2}")
    result2 = heapq.heappushpop(heap2, 1)
    print(f"heappushpop(1): 弹出 {result2}, 堆变为 {heap2}")
    
    print("\n关键区别:")
    print("- heapreplace: 总是执行一次弹出和一次插入")
    print("- heappushpop: 可能只插入不弹出（如果新元素就是最小值）")

compare_replace_methods()