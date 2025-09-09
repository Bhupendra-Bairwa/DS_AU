# combination of a given number 123
def combination(s):
    result = []
    n = len(s)
    
    def backtrack(start, path):
        if path:
            result.append(''.join(path))
        for i in range(start, n):
            path.append(s[i])
            backtrack(i + 1, path)
            path.pop()
    
    backtrack(0, [])
    print(result)
a = combination("123")