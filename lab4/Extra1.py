import xmlplain
def start():
    with open('schedule.xml', encoding='utf-8') as inf:
        xmlSchedule = xmlplain.xml_to_obj(inf, strip_space=True)

    with open('task2_schedule.yaml', 'a', encoding='utf-8') as outf:
        xmlplain.obj_to_yaml(xmlSchedule, outf)



start()