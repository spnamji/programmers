def solution(money):
    answer = []
    cost = money//5500
    mon = money%5500
    answer.extend([money//5500, money%5500])
    return answer