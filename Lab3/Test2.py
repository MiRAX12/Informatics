import unittest
import task2

class TestTask2(unittest.TestCase):
    def test_CollectiveConsciousness(self):
        data =(
        'что повышение уровня гражданского сознания позволяет выполнить '
        'важные задания по разработке как самодостаточных')
        result = ['повышение уровня', 'важные задания']
        self.assertEqual(result, task2.solve(data))
    def test_DerVerfahren(self):
        data = 'Господа, существующая теория влечет за собой процесс '
        result = ['существующая теория']
        self.assertEqual(result, task2.solve(data))
    def test_POV(self):
        data =(
        'Имеется спорная точка зрения, гласящая примерно следующее: '
        'сделанные на базе интернет-аналитики')
        result = ['спорная точка', 'сделанные на']
        self.assertEqual(result, task2.solve(data))
    def test_wha(self):
        data =(
        'С другой стороны, начало повседневной работы по формированию '
        'позиции играет важную роль в формировании первоочередных требований')
        result = ['формированию позиции', 'играет важную']
        self.assertEqual(result, task2.solve(data))
    def test_DeepThoughts(self):
        data = 'определяющее значение для глубокомысленных рассуждений '
        result = ['значение для']
        self.assertEqual(result, task2.solve(data))
        
unittest.main()
