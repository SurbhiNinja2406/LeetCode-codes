# The read4 API is already defined for you.
# @param buf4, List[str]
# @return an integer
# def read4(buf4):
class Solution(object):
    def __init__(self):
        # These need to persist across multiple calls to read(),
        # since a read4() call might fetch more characters than
        # the current read() call actually needs.
        self.buf4 = [''] * 4   # internal buffer holding leftover chars from read4
        self.buf4_size = 0     # how many valid characters are currently in buf4
        self.buf4_index = 0    # pointer to the next unused character in buf4

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        total_read = 0
        while total_read < n:
            if self.buf4_index == self.buf4_size:
                self.buf4_size = read4(self.buf4)
                self.buf4_index = 0
                if self.buf4_size == 0:
                    break
            while total_read < n and self.buf4_index < self.buf4_size:
                buf[total_read] = self.buf4[self.buf4_index]
                total_read += 1
                self.buf4_index += 1
        return total_read
print(__name__)
        