from itertools import combinations_with_replacement
import time
import multiprocessing
from collections import Counter

powers_lst = []

def isPosible(N):
    return N not in {2, 12, 13, 15, 18, 22, 26, 28, 30, 36}

def precalcPowers(N):
    return [i**N for i in range(10)]

def sum_of_powers(num):
    return sum(powers_lst[digit] for digit in num)

def isValid(lst, num):
    # Copy lst to avoid modifying the original list
    # Iterate through each digit of num
    lst = list(lst)
    while num > 0:
        digit = num % 10  # Extract the last digit of num
        if digit in lst:
            lst.remove(digit)
        else:
            return False
        num //= 10  # Remove the last digit from num
    return True

def main(N):
    global powers_lst
    powers_lst = []
    if isPosible(N):
        NNPs = []
        powers_lst = precalcPowers(N)
        combinations = combinations_with_replacement(range(10), N)
        for element in combinations:
            num = sum_of_powers(element)
            if len(str(num)) == N and isValid(element, num):
                NNPs.append(num)
        print(f"N={N}: {NNPs}")
        return NNPs

def main_aux(max):
    counter=2
    while counter <= max:
        print(counter, main(counter))

        counter+=1

def run_multi(N):
    processes = [multiprocessing.Process(target=main, args=[i]) for i in range(3,N+1)]
    for process in processes:
        process.start()
    for process in processes:
        process.join()

if __name__ == '__main__':
    start_time = time.time()
    run_multi(39)
    end_time = time.time()
    print("Execution time:", end_time - start_time)
