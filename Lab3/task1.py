import re
#466823 % 6 = 5 => Глаза: [
#466823 % 4 = 3 => Нос: <{
#466823 % 8 = 7 => Рот: =
#Смайлик [<{=

def solve(string):
    pattern = r'\[<\{='
    return len(re.findall(pattern, string))

