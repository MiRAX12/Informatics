import unittest
import task1
#[<{=
class TestTask1(unittest.TestCase):
    def test_emojispam(self):
        data = '[<{=[<{=[<{=[<{=[<{='
        result = 5
        self.assertEqual(result, task1.solve(data))
    def test_wyutnenko(self):
        data = 'Направо-[<{= Налевобед-8<{'
        result = 1
        self.assertEqual(result, task1.solve(data))
    def test_keyboardface(self):
        data = '^$%[<{=^&[<{=YUCFG[<{=tyuuiokjfh[[<{=<{=jkg789*I'
        result = 4
        self.assertEqual(result, task1.solve(data))
    def test_Jade_code(self):
        data = '[习近平<重要贡{=[<方{=方愿[<{=高铁成为双[<{=[<{=地区[<{=[<{=广大发[<{=[<{稳定=[<尼共{='
        result = 6
        self.assertEqual(result, task1.solve(data))
    def test_Rolton(self):
        data = 'Состав: ве[м<{=ль, масло по^&(*ное, вода п(*итьеv[<=aя, !!!соль!!!, витами[>{='
        result = 0
        self.assertEqual(result, task1.solve(data))
        
unittest.main()
