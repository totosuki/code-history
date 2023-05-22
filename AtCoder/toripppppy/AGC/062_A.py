from inputter import inp
import re

# テストケースの数
T = int(inp())

def f(_, s: str):
    if s[-1] == "B":
        if not re.search("BA", s):
            return "B"
        
    return "A"

for _ in range(T):
    N = int(inp())
    S = inp()

    print(f(N, S))
