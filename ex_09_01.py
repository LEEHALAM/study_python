'''
단어 수를 세는 프로그램
'''

fname = input("Enter File: ")
if len(fname) < 1:
    fname = "clown.txt"  # 아무것도 누르지 않고 엔터를 누르면 clown.txt 파일이 열리게 한다.
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()  # rstrip으로 각 문장의 오른쪽 개행 문자를 지운다.
    wds = lin.split()   # split 함수로 공백을 기준으로 나눈다.
    for w in wds:     # 단어의 빈도수를 센다.

        # if w in di:   # 기존에 있는 단어일 경우 카운트를 1 추가한다.
        #     di[w] = di[w] + 1
        # else:
        #     di[w] = 1

        # 위에 4줄을 한 줄로 줄일 수 있다.
        di[w] = di.get(w, 0) + 1


# 가장 많이 등장하는 단어 찾기
largest = -1
theword = None
for k, v in di.items():  # items는 모든 딕셔너리에 있는 키와 값 쌍을 반환하는 메소드로 두 개의 반복변수가 필요하다.
    if v > largest:    # 최대값 구하기
        largest = v
        theword = k    # 최대빈도수 키 단어 저장

print(theword, largest)
