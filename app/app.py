# app/app.py：PDF要求的dedupe去重代码 + 新增加法功能
def dedupe(lst):
    """去重函数：接收列表，返回无重复元素的新列表（保持原顺序）"""
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

def add(a, b):
    """新增功能：接收两个数字，返回求和结果；非数字输入抛异常"""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("输入必须为整数或浮点数")
    return a + b

# 本地运行测试（可选，用于VSCode中直接验证）
if __name__ == "__main__":
    print("dedupe去重测试：", dedupe([1, 2, 2, 3, 4, 4]))  # 预期输出 [1,2,3,4]
    print("加法功能测试：", add(3, 5))                      # 预期输出 8