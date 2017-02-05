import re


def storage():
    st = set()
    while True:
        line = raw_input('Input command: \n')

        if line[:4] == 'add ':
            commands = line[4:].split()
            for command in commands:
                st.add(command)

        elif line[:7] == 'remove ':
            element = line[7:]
            if element in st:
                st.remove(element)
            else:
                print('No such element!')

        elif line[:5] == 'find ':
            commands = line[5:].split()
            for element in commands:
                if element in st:
                    print(element)

        elif line == 'list':
            for element in st:
                print(element)

        elif line[:5] == 'save ':
            try:
                with open(line[5:], 'w') as file_handle:
                    for element in st:
                        file_handle.write(element + '\n')
            except Exception, e:
                print e

        elif line[:5] == 'load ':
            try:
                with open(line[5:]) as file_handle:
                    st.clear()
                    for element in file_handle:
                        st.add(element.strip())
            except Exception, e:
                print e

        elif line[:5] == 'grep ':
            reg_exp = re.compile(line[5:])
            for element in st:
                if reg_exp.search(element):
                    print(element)

        else:
            print('Unknown command. Please, try again.')
