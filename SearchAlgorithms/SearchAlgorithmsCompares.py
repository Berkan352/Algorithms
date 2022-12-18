import BinarySearch, LinearSearch, JumpSearch, InterpolationSearch, FibonacciSearch, ExponentialSearch, SublistSearch,IntervalSearch, random
import timeit
from some_trainings.data_structres.Tree import Tree

tree = Tree()


def main():
    data = random.sample(range(1, 100000), 10000)
    data = sorted(data)
    target = random.randint(1, 100000)

    for i in data:
        tree.add(i)

    print('Binary Search: ', timeit.timeit(lambda: BinarySearch.binary_search(data, target), number=10000))
    print('Linear Search: ', timeit.timeit(lambda: LinearSearch.linear_search(data, target), number=10000))
    print('Jump Search: ', timeit.timeit(lambda: JumpSearch.jump_search(data, target), number=10000))
    print('Interpolation Search: ', timeit.timeit(lambda: InterpolationSearch.interpolation_search(data, target), number=10000))
    print('Fibonacci Search: ', timeit.timeit(lambda: FibonacciSearch.fibonacci_search(data, target), number=10000))
    print('Exponential Search: ', timeit.timeit(lambda: ExponentialSearch.exponential_search(data, len(data),target), number=10000))
    print('Interval Search: ', timeit.timeit(lambda: IntervalSearch.interval_search(data, target), number=10000))
    print('BST Search: ', timeit.timeit(lambda: tree.search(target), number=10000))



if __name__ == '__main__':
    main()
