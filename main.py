def has_duplicates(lst):
    """
    检查列表中是否有重复元素
    参数: lst - 任意列表
    返回: bool - 如果有重复元素返回 True，否则返回 False
    """
    # 利用集合不可包含重复元素的特性，比较长度
    return len(set(lst)) != len(lst)

# 主程序 - 测试函数
if __name__ == "__main__":
    # 测试用例（包含题目要求的各类场景）
    test_cases = [
        [1, 2, 3],          # 无重复
        [1, 2, 2],          # 有重复
        ["a", "b", "a"],    # 字符串重复
        [],                 # 空列表
        [1.0, 2.0, 1.0],    # 浮点数重复
        [True, False],      # 布尔值无重复
        [None, None],       # None值重复
        [5]                 # 单元素列表
    ]
    
    # 测试每个用例并输出结果
    for case in test_cases:
        result = has_duplicates(case)
        if result:
            print(f"列表 {case}：有重复元素")
        else:
            print(f"列表 {case}：没有重复元素")
