'''
done을 입력할 때까지 숫자를 입력 받고, 입력 받은 숫자들의 합계, 개수, 평균을 구하는 프로그램 만들기
예외처리를 사용해서 숫자가 아닌 문자를 입력하면 'Invalid input'을 출력하게 하기

Enter a number: 4
Enter a number: 5
Enter a number: bad data
Invalid input
Enter a number: 7
Enter a number: done
16 3 5.333333333333333
'''
nsum = 0
count = 0
while True:
    num = input("Enter a number: ")
    if num == "done":
        break

    try:
        inum = int(num)
    except:
        print("Invalid input")
        continue

    nsum = nsum + inum
    count += 1

ave = nsum/count
print(nsum, count, ave)
