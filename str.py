# 한 줄 문자열 정의
s = ''
print(type(s))

str1 = 'Hello World'
print(type(s), type(str1))
print(isinstance(str1, str))

# 여러줄 문자열
str2 = '''ABC
1234
가나다라
'''

print(str2)

# 여러줄 주석으로 활용 가능
'''
여기는 주석 입니다.
여러 라인 주석을 대체할 수 있습니다.
'''

# escape
print("Hello\nWorld\nI Say \"Hello World\"")
print('Hello\nWorld\nI Say "Hello World"')


#
# 문자열 연산
#

str1 = 'First String'
str2 = 'Second String'

# 1. 인덱싱
print(str1[0], str1[1], str1[2])
print(str1[-1], str1[-2], str1[-3])

# 2. Slicing
# s[start:stop:step]
str3 = str2[2:5]
print(str3)
# print(str2[2:len(str2):1])
print(str2[2:])

s = "Python"
print(s[-1])        # 마지막 문자
print(s[-2:])       # 마지막 2개 문자
print(s[:-2])       # 마지막 2개 문자 제외한 전체문자열

print(s[::-1])      # reverse
print(s[1::-1])     # 1번째, 2번째 문자 s[1:0:-1]
print(s[:-3:-1])    # 마지막 두개 문자
print(s[-3::-1])    # 마지막 2개 문자 제외한 전체문자열

# 연결(+)
print(str1 + ' ' + str2)
# 리터럴 연결시 + 생략 가능
# str3 = '1st' + ' ' + '2nd'
str3 = '1st' ' ' '2nd'
print(str3)

# 문자열 객체 연결은 문자열끼리만 할 수 있다.
name = '둘리'
age = 10
# print(name + 10)

# 반복(*)
print(str1 * 3)

# len() 함수
print(len(str1))

# in, not in 연산
print('F' in str1)
print('S' not in str1)

# str 객체는 Immutable이다
# str1[0] = 'f'

print("name:" + name + ", age:" + str(age))

# 서식(formatting) = format 함수
print("name:" + format(name, "s") + ", age:" + format(age, "d"))

# 서식: 튜플을 사용한 방식
f = "name: %s, age: %d"
print(f % (name, age))
print(f % ("또치", 20))

# 서식: 딕셔너리를 사용한 방식
f = "name: %(n)s, age: %(a)d"
print(f % {'n': '둘리', 'a': 10})
print(f % {'a': 20, 'n': '또치'})


#
# 객체함수
#

# 1. 대소문자 관련
s = 'i like Python'

print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.capitalize())
print(s.title())

# 2. 검색
s = 'I Like Python, I Like Java Also'
print(s.count("Like"))
print(s.find('Like'))
print(s.find('Like', 5))
print(s.find('JavaScript'))
print(s.rfind('Like'))

# 발견하지 못하면 예외가 발생하다.
# print(s.index("JavaScript"))
print(s.rindex("Like"))
print(s.startswith("I Like"))
print(s.startswith("Like", 2))
print(s.endswith("Also"))
print(s.endswith("Java", 0, 26))

# 편집과 치환
s = '   spam ans ham    '
print('-------' + s.strip() + '-------')
print('-------' + s.rstrip() + '-------')
print('-------' + s.lstrip() + '-------')

s =  '<><abc><><defg><><>'
print('-------' + s.strip('<>') + '-------')

s = 'Hello Java'
print(s.replace('Java', 'Python'))

# 분리 & 결합
s = 'spam and ham'
l = s.split(' and ')
print(l, type(l))

s2 = ':'.join(l)
print(s2)

s3 = 'one:two:three:four:five'
print(s3.split(':'))
print(s3.split(':', 2))
print(s3.rsplit(':', 2))

lines = '''1st line
2nd line
3rd line
4th line
'''

print(lines.split('\n'))
print(lines.splitlines())

# 판별
print('1234'.isdigit())
print('abc'.isalpha())
print('1234'.isalpha())
print('abcd'.isalpha())

print('\r\n'.isspace())
# '0' 채우기
print('20'.zfill(5))
print('1234'.zfill(5))


# 서식: 객체함수
print('name:{}, age:{}'.format('둘리'))
print('name:{0}, age:{1}'.format('둘리'))
print('name:{1}, age:{0}'.format(10, '둘리'))
print('{:3}의 제곱근은 {:.7}'.format(2, 2**0.5))
print('name:{[n]}, age:{}'.format('둘리'))