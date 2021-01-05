'''
다양한 종류와 다양한 길이의 문자열을 보고 숫자가 있는 부분을 잘라서 실수로 변환하는 프로그램 만들기
'''

str = 'X-DSPAM-Confidence: 0.8475'

ipos = str.find(":")
print(ipos)
print(str[19:].strip())
value = float(str[19:].strip())
print(value)
