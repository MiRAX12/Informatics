def start():
    scheduleXml = open('schedule.xml', mode='r', encoding='utf-8')
    scheduleYaml = open('schedule.yaml', mode='w', encoding='utf-8')
    schedule = [line.rstrip() for line in scheduleXml]
    for line in range(len(schedule)):
        s = schedule[line]
        for symbol in range(0, len(schedule[line])-1):
            if s[symbol] == '<' and s[symbol + 1] == '/':
                s = s[:symbol]
                break
            if s[symbol] == '<':
                s = s.replace(s[symbol], '*', 1)
            if s[symbol+1] == '>':
                s = s.replace(s[symbol+1], '&', 1)
            if s[symbol] == s[symbol+1] == ' ':
                s = s.replace(s[symbol], '?', 1)
                s = s.replace(s[symbol+1], '^', 1)

        s = s.replace('*', '').replace('&', ': ').replace('?^', ' ')
        if s == '      class: ':
            s = '    - class: '
        if s == '  day name="Вторник": ':
            s = "- day: \n    '@name': Вторник"
        if s == '  day name="Четверг": ':
            s = "- day: \n    '@name': Четверг"


        scheduleYaml.write(s + '\n')
    scheduleXml.close()
    scheduleYaml.close()

start()