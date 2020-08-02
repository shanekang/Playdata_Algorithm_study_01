'''함수 solution은 정수 n을 매개변수로 입력받습니다. n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요. 예를들어 n이 118372면 873211을 리턴하면 됩니다.

제한 조건
n은 1이상 8000000000 이하인 자연수입니다.
입출력 예
n	return
118372	873211
'''


def solution(n):
    answer = 0
    print_reverse = []
    sorted_one = []
    string_change= str(n)
    list_change = string_change.split()
    
    for i in range(0, len(string_change)):
        print_reverse.append(list_change[0][i])
        
    print_reverse.sort()
    sorted_one = print_reverse[::-1]
    list_result = ''.join(sorted_one)
    int_result = int(list_result)
    
    return int_result