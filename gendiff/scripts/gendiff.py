import argparse

parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument('first_file')
parser.add_argument('second_file')
args = parser.parse_args()



def main():
    print('Welcome to the Gendiff!')


if __name__ == '__main__':
    main()
