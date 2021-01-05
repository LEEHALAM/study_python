'''
텍스트 파일을 읽어서 From으로 시작하는 줄을 찾아 세 번째 단어 추출하기
'''

han = open('mbox-short.txt')

for line in han:
    line = line.rstrip()
    wds = line.split()
    # 가디언 패턴
    # 해당 줄에 3개 미만의 단어가 있거나 첫 번째 단어가 From이 아니면 continue 하는 것
    if len(wds) < 3 or wds[0] != 'From':
        continue
    print(wds[2])
