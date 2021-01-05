'''
텍스트 파일을 읽고 읽은 내용을 대문자로 변환하기
'''

fhand = open('ex_07_01_mbox-short.txt', 'r')
for i in fhand:
    j = i.rstrip()
    print(j.upper())
