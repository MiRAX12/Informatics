def start():
    import re

    global lvl
    global recursion_counter
    global parsed_string


    def parse_xml(xml_string):
        main_pattern = re.compile(r'<(\w+)(.*?)>(.*?)</\1>', re.DOTALL)
        attr_pattern = re.compile(r'(\w+)="([^"]+)"')#аттрибуты
        xml_string = xml_string.strip()#обрезка по бокам

        node_match = main_pattern.match(xml_string)
        result = []
        if node_match:
            cursor = 0
            while cursor < len(xml_string):
                temp_count = len(xml_string[cursor::]) #сколько осталось символов
                node_match = main_pattern.match(xml_string[cursor::].lstrip())
                tag_name = node_match.group(1) #значение элемента
                attributes = dict(attr_pattern.findall(node_match.group(2)))#словарь аттрибутов
                text = ''
                children = parse_xml(node_match.group(3).strip())#вложенные элементы
                # print(node_match.group(3).strip())
                if len(children) == 0:
                    text = node_match.group(3)
                result.append({'name': tag_name, 'attributes': attributes, 'text': text, 'children': children})
                cursor += node_match.span()[1] + temp_count - len(xml_string[cursor::].lstrip())
        return result


    def parse_children(obj):
        global lvl
        global recursion_counter
        global parsed_string
        tab = '    '
        has_children = True
        after_attr = False

        for el in range(len(obj)):
            for key in obj[el]:
                if key == 'name':
                    if obj[el][key] != '':
                        if obj[el]['text'] != '':
                            has_children = False #строка точно не имеет вложенных элементов
                            parsed_string += tab * lvl + obj[el][key] + ': ' + obj[el]['text'] + '\n'
                            if el == len(obj) - 1:#переходим на уровень выше
                                lvl -= 1
                            break
                        else:
                            parsed_string += tab * lvl + obj[el][key] + ': ' + '\n' #пустые теги
                    else:
                        continue

                if key == 'attributes':
                    if len(obj[el][key]) == 0:
                        continue
                    else:
                        for attr in obj[el][key]:
                            el_attr = "'" + "@" + attr + "': " + obj[el][key][attr]
                            parsed_string += tab * lvl + el_attr + '\n'
                            after_attr = True #то не вложенный элемент

                if key == 'text':
                    continue

                if key == 'children':
                    if len(obj[el][key]) != 0:
                        if has_children:
                            if not after_attr:
                                lvl += 1#переходим на уровень ниже
                        recursion_counter += 1
                        parse_children(obj[el][key])#парсим следующую вложенность

        recursion_counter -= 1
        if recursion_counter == 1:
            lvl = 1


    def to_string(obj): #p_object=parse_xml
        global lvl
        global recursion_counter
        global parsed_string
        lvl = 1
        recursion_counter = 0
        parsed_string = ''
        root_el = obj[0]['name'] + ':' #корневой элемент
        parsed_string += root_el + '\n'

        root_tag = obj[0]['children']
        if len(root_tag) != 0:
            parse_children(root_tag)


    def parse_to_yaml(s): #s = parsed_string
        s = s.replace('    ', '  ')
        lst_el_pattern = re.compile(r'((\s{2})+(\b\w+\b: ))(.+?\1)+', re.DOTALL)
        match = lst_el_pattern.findall(s)

        for el in range(len(match)):#перебор по дням
            list_element = match[el][0]
            for char in range(len(list_element)-2):#перебор букв "списка"
                if list_element[char] == ' ' and list_element[char+1] == ' ' and list_element[char+2] != ' ':
                    s = re.sub(list_element[char] + list_element[char+1] + match[el][0][match[el][0].find(match[el][0][char+2]):],
                               '-' + list_element[char+1] + match[el][0][match[el][0].find(match[el][0][char+2]):], s)
                    #1 день 1 слово начиная с +2 символа
        return s


    xmlFile = open('schedule.xml', mode='r', encoding='utf-8')
    yamlFile = open('scheduleX3.yaml', mode='w', encoding='utf-8')
    data = xmlFile.read()

    p_object = parse_xml(data)
    to_string(p_object)
    res = parse_to_yaml(parsed_string)
    yamlFile.write(res)

start()