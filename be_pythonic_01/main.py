import sys, os

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)

# sys.path.append('../be_pythonic_01')
from be_pythonic_01.global_settings import INT_NUMBER


def main():
    if INT_NUMBER > 0:
        print("ok")
    
    if INT_NUMBER == 90:
        print('ok')
    
    if INT_NUMBER == 99:
        print('good')
    
    if INT_NUMBER == 89:
        print('greate')


if __name__ == '__main__':
    main()
