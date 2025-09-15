class Solution:
    """
    为了找到自己满意的工作，牛牛收集了每种工作的难度和报酬。牛牛选工作的标准是在难度不超过自身能力
    值的情况下，牛牛选择报酬最高的工作。在牛牛选定了自己的工作后，牛牛的小伙伴们来找牛牛帮忙选工作，
    牛牛依然使用自己的标准来帮助小伙伴们。牛牛的小伙伴太多了，于是他只好把这个任务交给了你。
    class Job {
    public int money;// 该工作的报酬
    public int hard; // 该工作的难度
    public Job(int money, int hard) {
    this.money = money;
    this.hard = hard;
    }
    }
    给定一个Job类型的数组jobarr，表示所有的工作。给定一个int类型的数组arr，表示所有小伙伴的能力。
    返回int类型的数组，表示每一个小伙伴按照牛牛的标准选工作后所能获得的报酬。
    """
    def choose_work(self, jobs, ability):
        jobs.sort(key=lambda x:(x[0], -x[1])) # x[0]表示难度，x[1]表示报酬
        mapping = []
        mapping.append(jobs[0])
        pre = jobs[0]
        for i in range(1, len(jobs)):
            if jobs[i][0] != pre[0] and jobs[i][1] > pre[1]:
                pre = jobs[i]
                mapping.append(pre)
        ans = []
        def binary_search(job_list, ability):
            l, r = 0, len(job_list) - 1
            res = -1
            while l <= r:
                mid = l + (r - l) // 2
                if job_list[mid][0] == ability:
                    return job_list[mid][1]
                elif job_list[mid][0] < ability:
                    res = job_list[mid][1]
                    l = mid + 1
                else:
                    r = mid - 1
            return res
        for val in ability:
            ans.append(binary_search(mapping, val))
        return ans
