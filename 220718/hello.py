# 모듈 형태로 되어 있는 함수들의 집합

# 간단한 함수
# def 키워드 함수이름(매개변수)
def say_hello_name(name):             # 함수의 선언부(헤더)
    print("안녕하세요, ", name)   # 함수의 구현부(정의부, 몸체)
# 위와 같이 함수를 정의만 했다면 출력값은 없다. 출력값이 나오게 하려면 호출(call)을 해야한다.

def say_hello_name_msg(name, msg):             # 함수의 선언부(헤더)
    print("안녕하세요, ", name, msg)   # 함수의 구현부(정의부, 몸체)

# 값을 반환하는 함수 예제
# start 부터 end 까지의 누적합을 구하는 함수
def get_sum(start, end):
    hap = 0
    for i in range(start, end+1):
        hap += i
    return hap