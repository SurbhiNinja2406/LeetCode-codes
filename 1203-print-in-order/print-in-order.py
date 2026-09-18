import threading
class Foo(object):
    def __init__(self):
        self.event1 = threading.Event()
        self.event2 = threading.Event()
    def first(self, printFirst):
        """
        :type printFirst: method
        :rtype: void
        """
        printFirst()
        self.event1.set()
    def second(self, printSecond):
        """
        :type printSecond: method
        :rtype: void
        """
        self.event1.wait()
        printSecond()
        self.event2.set()
    def third(self, printThird):
        """
        :type printThird: method
        :rtype: void
        """
        self.event2.wait()
        printThird()
if __name__ == "__main__":
    import functools
    import itertools
    def run_test(nums):
        result = []
        lock = threading.Lock()
        def make_printer(word):
            def printer():
                with lock:
                    result.append(word)
            return printer
        foo = Foo()
        method_map = {
            1: functools.partial(foo.first, make_printer("first")),
            2: functools.partial(foo.second, make_printer("second")),
            3: functools.partial(foo.third, make_printer("third")),
        }
        threads = [threading.Thread(target=method_map[n]) for n in nums]
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        return "".join(result)
    nums1 = [1, 2, 3]
    output1 = run_test(nums1)
    print('Input: nums = {}'.format(nums1))
    print('Output: "{}"'.format(output1))
    assert output1 == "firstsecondthird"
    print('PASSED\n')
    nums2 = [1, 3, 2]
    output2 = run_test(nums2)
    print('Input: nums = {}'.format(nums2))
    print('Output: "{}"'.format(output2))
    assert output2 == "firstsecondthird"
    print('PASSED\n')
    print('Stress testing all permutations x 100 runs each...')
    for perm in itertools.permutations([1, 2, 3]):
        for _ in range(100):
            out = run_test(list(perm))
            assert out == "firstsecondthird", 'FAILED for {}: got {}'.format(perm, out)
    print('All stress tests PASSED')
print(__name__)