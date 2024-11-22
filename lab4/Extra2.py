import re

def start():
    openTag = r'<([^/]\w+)>'
    closeTag = r'</\w+>'
    lstClass = r'            <class>'
    lstDay = r'    <day name="(\w+)">'
    tab = r'    '

    scheduleXml = open('schedule.xml', mode='r', encoding='utf-8')
    scheduleYaml = open('scheduleX2.yaml', mode='a', encoding='utf-8')

    s = scheduleXml.read()

    s = re.sub(lstClass, '      - class:', s)
    s = re.sub(lstDay, "- day:\n      '@name': \\1", s)
    s = re.sub(openTag, '\\1: ', s)
    s = re.sub(closeTag, '', s)
    s = re.sub(tab, '  ', s)

    scheduleYaml.write(s)
    scheduleXml.close()
    scheduleYaml.close()

start()