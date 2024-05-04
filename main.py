def deco(func):
    def NewNum():
        print('decorator-test')
        func()
        
    return NewNum  # 괄호를 제거하여 함수 자체를 반환하도록 수정

@deco
def one():
    print('1')

one()  # 이후에 one()을 호출하여 실행

