import threading
class H2O(object):
    def __init__(self):
        self.hydrogenSemaphore = threading.Semaphore(2)
        self.oxygenSemaphore = threading.Semaphore(1)
        self.condition = threading.Condition()
        self.count = 0
        self.generation = 0
    def _wait_at_barrier(self):
        with self.condition:
            my_generation = self.generation
            self.count += 1
            if self.count == 3:
                self.count = 0
                self.generation += 1
                self.condition.notify_all()
            else:
                while my_generation == self.generation:
                    self.condition.wait()
    def hydrogen(self, releaseHydrogen):
        self.hydrogenSemaphore.acquire()
        self._wait_at_barrier()
        releaseHydrogen()
        self.hydrogenSemaphore.release()
    def oxygen(self, releaseOxygen):
        self.oxygenSemaphore.acquire()
        self._wait_at_barrier()
        releaseOxygen()
        self.oxygenSemaphore.release()
if __name__ == "__main__":
    def run_test(water):
        result = []
        lock = threading.Lock()
        def make_printer(letter):
            def printer():
                with lock:
                    result.append(letter)
            return printer
        h2o = H2O()
        threads = []
        for ch in water:
            if ch == 'H':
                t = threading.Thread(target=h2o.hydrogen, args=(make_printer('H'),))
            else:
                t = threading.Thread(target=h2o.oxygen, args=(make_printer('O'),))
            threads.append(t)
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        return "".join(result)
    def is_valid_h2o_output(output, n):
        if len(output) != 3 * n:
            return False
        if output.count('H') != 2 * n or output.count('O') != n:
            return False
        for i in range(0, len(output), 3):
            group = output[i:i + 3]
            if group.count('O') != 1 or group.count('H') != 2:
                return False
        return True
    water1 = "HOH"
    output1 = run_test(water1)
    print('Input: water = "{}"'.format(water1))
    print('Output: "{}"'.format(output1))
    assert is_valid_h2o_output(output1, 1), "FAILED example 1"
    print('PASSED\n')
    water2 = "OOHHHH"
    output2 = run_test(water2)
    print('Input: water = "{}"'.format(water2))
    print('Output: "{}"'.format(output2))
    assert is_valid_h2o_output(output2, 2), "FAILED example 2"
    print('PASSED\n')
    print('Stress testing...')
    for trial in range(200):
        n = 6
        water = "O" * n + "H" * (2 * n)
        out = run_test(water)
        assert is_valid_h2o_output(out, n), 'FAILED trial {}: got {}'.format(trial, out)
    print('All stress tests PASSED')
print(__name__)