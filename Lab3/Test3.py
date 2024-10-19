import unittest
import task3
class TestTask3(unittest.TestCase):
    def test_che(self):
        a,b,c = 'п а р'.split()
        dist = 2
        data = 'ПынАваР РааРыФ ПонАзоР ТевРрЛ'
        result = ['поназор']
        self.assertEqual(result, task3.solve(data,dist,a,b,c))
    def test_cursed(self):
        a,b,c = 'й г а'.split()
        dist = 2
        data = 'Йога Йогурт Йоугуоарт Йоог-Сарон'
        result = ['йоугуоарт', 'йоог-сарон']
        self.assertEqual(result, task3.solve(data,dist,a,b,c))
    def test_FarEastBranch(self):
        a,b,c = 'т а л'.split()
        dist = 1
        data = 'отрасль Отраасль мтпарлс ветраплан '
        result = ['отрасль', 'мтпарлс']
        self.assertEqual(result, task3.solve(data,dist,a,b,c))
    def test_LENOZAVR(self):
        a,b,c = 'л о в'.split()
        dist = 2
        data = 'ЛенОзаВ ОпвНрвН ЛипОзаВ КорАоБ'
        result = ['ленозав', 'липозав']
        self.assertEqual(result, task3.solve(data,dist,a,b,c))
    def test_OAOrealko(self):
        a,b,c = 'р а к'.split()
        dist = 1
        data = 'Релакс коллонтай риалк'
        result = ['риалк']
        self.assertEqual(result, task3.solve(data,dist,a,b,c))
        
unittest.main()

