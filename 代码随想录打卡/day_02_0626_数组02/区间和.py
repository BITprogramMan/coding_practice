def main():
    n = int(input())
    nums = []
    subsums = []
    for i in range(n):
        nums.append(int(input()))
        if i == 0:
            subsums.append(nums[-1])
        else:
            subsums.append(subsums[-1] + nums[-1])
    
    input_idx_list = []
    while True:
        input_idx = input().strip()
        if not input_idx:
            break
        else:
            input_idx_list.append(list(map(int, input_idx.split(' '))))
    for start, end in input_idx_list:
        res = subsums[end] - subsums[start - 1] if start > 0 else subsums[end]
        print(res)

if __name__ == '__main__':
    main()