def solution(a, b):

    day_of_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    week_cycle = ['FRI', 'SAT', 'SUN','MON','TUE','WED','THU']

    answer = week_cycle[(sum(day_of_month[:a-1]) + b)%7 - 1]

    return answer