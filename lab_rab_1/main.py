import re
import sys
from task1_stat import text_statistics
from task2_sorts import sorts
from task3_storage import storage
from task4_fib import fib


def main():
    if len(sys.argv) == 1:
        print('---------------------')
        print('|Available commands:|')
        print('---------------------')
        print('|  stat             |')
        print('|  sort             |')
        print('|  storage          |')
        print('|  fibo             |')
        print('---------------------')
        return

    if sys.argv[1] == 'stat':
        text = ''.join(open(sys.argv[2]).readlines())
        sentences = re.split(r' *[\.\?!][\'"\)\]]* *', text)
        stats = text_statistics(sentences, 10, 4)
        print('1) Word usage:')
        print(stats[1])
        print('2) the average number of words in sentences:')
        print(stats[3])
        print('3) the median number of words:')
        print(stats[2])
        print('4) 4 - grams top 10:')
        print(stats[0])

    elif sys.argv[1] == 'sort':
        print(sorts(sys.argv[2]))

    elif sys.argv[1] == 'storage':
        storage()

    elif sys.argv[1] == 'fibo':
        n = int(sys.argv[2])
        for num in fib(n):
            print(num)
    else:
        print('Unknown command. Please, try again.')

main()


