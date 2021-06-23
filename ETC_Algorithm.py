
import math
### 소수의 판별 ###

# 소수는 2보다 큰 자연수 중에서 1과 자기자신을 제외한 자연수로는 나누어ㄸ러어지지 않는 자연수
# ex) 2, 3, 5, 7, 11 13
def prime_number():
    n = 8
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

# 특정 수까지의 모든 소수를 출력하는 프로그램
def eratosthenes():
    n = 26
    result = [True] * (n + 1)

    for i in range(2, int(math.sqrt(n) + 1)):
        if result[i]:
            j = 2
            while i * j <= n:
                result[i*j] = False
                j += 1

    for i in range(2, n):
        if result[i]:
            print(i, end='')

# 투 포인터
# 리스트에 순차적으로 접근해야 할 때 2개의 점 위치를 기록하면서 처리

def solution1():
    n = 5
    m = 5
    data = [1, 2, 3, 2, 5]
    count = 0
    interval_sum = 0
    end = 0

    for start in range(n):

        while interval_sum < m or end > n:
            interval_sum += data[end]
            end += 1

        if interval_sum == m:
            count += 1

        interval_sum -= data[end]

    print(count)

def solution2():
    n, m = 3, 4
    a = [1, 3, 5]
    b = [2, 4, 6, 8]

    result = [0] * (n + m)
    i, j, k = 0, 0, 0

    while k < (n + m):
        if j >= m or (i < n and a[i] <= b[j]):
            result[k] = a[i]
            i += 1
        else:
            result[k] = b[j]
            j += 1
        k += 1

    print(result)

def interval_sum():
    n = 5
    data = [10, 20, 30, 40, 50]
    sum_value = 0
    result = [0]

    left = 3
    right = 4

    for i in data:
        sum_value += i
        result.append(sum)

    print(result[right] - result[left - 1])

def q1():
    n, m = 3, 16
    result = [True] * (m+1)

    for i in range(2, int(math.sqrt(m) + 1)):
        if result[i]:
            j = 2
            while i * j <= m:
                result[i * j] = False
                j += 1

    for i in range(n, m + 1):
        if result[i]:
            print(i)

[1, 2, 3]
# 원소 중복 X 순서 상관 X ==> [1, 2], [1, 3], [2, 3]
from itertools import combinations
# 원소 중복 X 순서 상관 O ==> [1, 2], [1, 3], [2, 1], [2, 3], [3, 1], [3, 2]
from itertools import permutations
# 원소 중복 O 순서 상관 O ==> [1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3]
from itertools import product # 중복 포함

def q2():
    n, m = 4, 6
    data = ['a', 't', 'c', 'i', 's', 'w']
    vowels = ['a', 'e', 'i', 'o', 'u']
    data.sort()

    for password in combinations(data, n):
        count = 0
        for i in password:
            if i in vowels:
                count += 1

        if 1 <= count <= n - 2:
            print(''.join(password))
