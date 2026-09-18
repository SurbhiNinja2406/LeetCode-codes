import threading
class FooBar(object):
    def __init__(self, n):
        self.n = n
        self.fooSemaphore = threading.Semaphore(1)
        self.barSemaphore = threading.Semaphore(0)
    def foo(self, printFoo):
        """
        :type printFoo: method
        :rtype: void
        """
        for i in range(self.n):
            self.fooSemaphore.acquire()
            printFoo()
            self.barSemaphore.release()
    def bar(self, printBar):
        """
        :type printBar: method
        :rtype: void
        """
        for i in range(self.n):
            self.barSemaphore.acquire()
            printBar()
            self.fooSemaphore.release()
if __name__ == "__main__":
    import functools
    def run_test(n):
        result = []
        lock = threading.Lock()
        def make_printer(word):
            def printer():
                with lock:
                    result.append(word)
            return printer
        foobar = FooBar(n)
        threadA = threading.Thread(target=foobar.foo, args=(make_printer("foo"),))
        threadB = threading.Thread(target=foobar.bar, args=(make_printer("bar"),))
        threadA.start()
        threadB.start()
        threadA.join()
        threadB.join()
        return "".join(result)
    n1 = 1
    output1 = run_test(n1)
    print('Input: n = {}'.format(n1))
    print('Output: "{}"'.format(output1))
    assert output1 == "foobar"
    print('PASSED\n')
    n2 = 2
    output2 = run_test(n2)
    print('Input: n = {}'.format(n2))
    print('Output: "{}"'.format(output2))
    assert output2 == "foobarfoobar"
    print('PASSED\n')
    print('Stress testing...')
    for trial in range(200):
        n = 5
        out = run_test(n)
        expected = "foobar" * n
        assert out == expected, 'FAILED trial {}: got {}'.format(trial, out)
    print('All stress tests PASSED')
print(__name__)