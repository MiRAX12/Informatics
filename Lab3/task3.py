import re
#Необходимо выбрать три любых буквы и расстояние между ними. С помощью
#регулярного выражения нужно найти все слова (последовательность символов,ограниченная пробелами), в которых:
#• встречаются эти буквы в заданной последовательности и расстоянии (например, через один друг от друга);
#• не встречаются на других позициях.

#Рабочий блок
if __name__=='__main__':
    a,b,c = input("Введите буквы через пробел ").split()
    dist=int(input("Введите расстояние между буквами "))
    data = input().lower()
    pattern=fr'\b(?:[^{a}{b}{c} ]*[{a}]){{1}}'\
             fr'(?:[^{a}{b}{c} ]{{{dist}}}[{b}]){{1}}'\
             fr'(?:[^{a}{b}{c} ]{{{dist}}}[{c}]){{1}}[^{a}{b}{c} ]*\b'
    for i in re.findall(pattern,data):
        print(i,end=' ')

#Тестовый блок
def solve(data,dist,a,b,c):
    pattern=fr'\b(?:[^{a}{b}{c} ]*[{a}]){{1}}'\
             fr'(?:[^{a}{b}{c} ]{{{dist}}}[{b}]){{1}}'\
             fr'(?:[^{a}{b}{c} ]{{{dist}}}[{c}]){{1}}[^{a}{b}{c} ]*\b'
    data = data.lower()
    return re.findall(pattern, data)
