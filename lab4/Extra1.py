import xmlplain
def start():
    with open('schedule.xml', encoding='utf-8') as inf:
        xmlSchedule = xmlplain.xml_to_obj(inf, strip_space=True, fold_dict=True)

    with open('scheduleX1.yaml', 'w', encoding='utf-8') as outf:
        xmlplain.obj_to_yaml(xmlSchedule, outf)

start()