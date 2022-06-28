"""
MLE 电面纯data structure coding。
给了一个list的人 每个人都有一个相对应的开始和结束工作时间。
要求写一个function output结果是列出所有可能的时间interval 并且在每个interval里面写出这个时间段在工作的人。和leetcode meeting room II有点像

Example:
time = [[1,3], [2,4], [5,6]]

output:
{
[1,4]: [0,1]
[5,6]: [2] 
}
"""
def findWorkTime(intervals):
    intervals.sort(key = lambda x: x[0])

    merged = []

    for i, interval in enumerate(intervals):
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
            intervals[i] = merged[-1]
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
            intervals[i] = merged[-1]

    res = {}

    for i, v in enumerate(intervals):
        if tuple(v) in res:
            res[tuple(v)].append(i)
        else:
            res[tuple(v)] = [i]
            
    return res

intervals = [[1,3], [2,4], [5,6]]
print(findWorkTime(intervals))

