import os

def make_file(typ,level,file_name):
    path = os.path.join('/Users/jaewon/Documents/algorithms',typ,level,file_name)
    os.makedirs(path, exist_ok = True)
    # main.py 파일 생성
    with open(os.path.join(path, 'main.py'), 'w') as file:
        file.write("import sys\n")
        file.write(f"sys.stdin = open('./{typ}/{level}/{file_name}/input.txt', 'r')\n")
        file.write("input = sys.stdin.readline")
    # input.txt 파일 생성
    with open(os.path.join(path, 'input.txt'), 'w'):
        pass
    # README.md 파일 생성
    with open(os.path.join(path, 'README.md'), 'w'):
        pass
    
make_file('solved.ac','level3','9375_패션왕')