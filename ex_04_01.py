'''
예제

월급 계산 프로그램을 다시 프로그램하기.
근무 시간이 40시간이 넘으면 초과 근무 시간에는 시급의 1.5배를 지급한다.
이름이 computepay이고 2개의 매개변수 (시간과 시급)를 받는 함수를 작성하기.

Enter Hour: 45
Enter Rate: 10

Pay: 475.0                         475 = 40 * 10 + 5 * 15
'''


def computepay(hours, rate):
    if hours > 40:
        pay = 40 * rate + (hours-40) * rate * 1.5
    else:
        pay = hours * rate
    return pay


temph = float(input("Enter Hours: "))
tempr = float(input("Enter Rate: "))

pay = computepay(temph, tempr)

print("Pay: ", pay)
