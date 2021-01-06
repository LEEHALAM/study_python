'''
가장 빈도가 높은 단어들을 튜플을 사용하여 나타내고, 값을 기준으로 딕셔너리를 정렬하는 프로그램
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

# 여기까지 딕셔너리
# 밑에서부터는 리스트 만들고 값과 키의 순으로 튜플 내에서 순서 뒤집음.

tmp = list()
for k, v in di.items():
    newt = (v, k)
    tmp.append(newt)

tmp = sorted(tmp, reverse=True)  # 정렬할 수 있도록 순서를 바꿔줌.

for v, k in tmp[:5]:    # 한번 정렬된 다음 다시 k, v 순으로 순서를 바꿔줌.
    print(k, v)

# 정렬할 때는 값과 키의 쌍으로 정렬하고 정렬된 후에는 키와 값의 쌍으로 출력한 것.
