#pytale入れてみた

import pytale
import sys
import random

scenario = pytale.Scenario()

code = """
raise ValueError("^^")
"""

# code = """
# for i in range(500):
#   print(random.randint(0, i * 100))
# sys.exit(1)
# """

a = scenario.input(eval(compile(code, "", "exec")))
print(a)