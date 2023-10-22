def gen(intput: str) -> List[str]:
    if len(intput) == 1:
        return [intput]  # 如果字串長度為1，直接返回該字串
    
    result = []
    for char in intput:
        remain = list(intput)#列表
        remain.remove(char)  # 去除字串中的特定字符
        remain = ''.join(remain)  # 以''為分隔儲存
        for perm in gen(remain):
            result.append(char + perm)#將所有可能的排列組合起來
    
    return result  # 返回所有排列的列表

intput = input("請輸入一段數字: ")#輸入數字
print(gen(intput))  # 將所有排列印出來
