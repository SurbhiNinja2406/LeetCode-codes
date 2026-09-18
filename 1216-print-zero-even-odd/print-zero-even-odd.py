import threading
class ZeroEvenOdd(object):
    def __init__(self, n):
        self.n = n
        self.zeroSemaphore = threading.Semaphore(1)
        self.evenSemaphore = threading.Semaphore(0)
        self.oddSemaphore = threading.Semaphore(0)
    def zero(self, printNumber):
        for i in range(1, self.n + 1):
            self.zeroSemaphore.acquire()
            printNumber(0)
            if i % 2 == 1:
                self.oddSemaphore.release()
            else:
                self.evenSemaphore.release()
    def even(self, printNumber):
        for i in range(2, self.n + 1, 2):
            self.evenSemaphore.acquire()
            printNumber(i)
            self.zeroSemaphore.release()
    def odd(self, printNumber):
        for i in range(1, self.n + 1, 2):
            self.oddSemaphore.acquire()
            printNumber(i)
            self.zeroSemaphore.release()
if __name__ == "__main__":
    def run_test(n):
        result = []
        lock = threading.Lock()
        def make_printer():
            def printer(x):
                with lock:
                    result.append(str(x))
            return printer
        zeo = ZeroEvenOdd(n)
        printer = make_printer()
        threadA = threading.Thread(target=zeo.zero, args=(printer,))
        threadB = threading.Thread(target=zeo.even, args=(printer,))
        threadC = threading.Thread(target=zeo.odd, args=(printer,))
        threadA.start()
        threadB.start()
        threadC.start()
        threadA.join()
        threadB.join()
        threadC.join()
        return "".join(result)
    n1 = 2
    output1 = run_test(n1)
    print('Input: n = {}'.format(n1))
    print('Output: "{}"'.format(output1))
    assert output1 == "0102"
    print('PASSED\n')
    n2 = 5
    output2 = run_test(n2)
    print('Input: n = {}'.format(n2))
    print('Output: "{}"'.format(output2))
    assert output2 == "0102030405"
    print('PASSED\n')
    print('Stress testing...')
    for trial in range(200):
        n = 7
        out = run_test(n)
        expected = "".join("0" + str(i) for i in range(1, n + 1))
        assert out == expected, 'FAILED trial {}: got {}'.format(trial, out)
    print('All stress tests PASSED')
print(__name__)