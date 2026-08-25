
class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        buf4 = [''] * 4
        total_read = 0
        while total_read < n:
            count = read4(buf4)  
            if not count:
                break
            chars_to_copy = min(count, n - total_read)
            for i in range(chars_to_copy):
                buf[total_read + i] = buf4[i]
            total_read += chars_to_copy
            if count < 4:
                break
        return total_read
class FileReader(object):
    def __init__(self, file_content):
        self.file_content = file_content
        self.pointer = 0
    def read_chars(self, buf4):
        count = 0
        while count < 4 and self.pointer < len(self.file_content):
            buf4[count] = self.file_content[self.pointer]
            self.pointer += 1
            count += 1
        return count
def run_test(file_content, n):
    reader = FileReader(file_content)
    global read4
    read4 = reader.read_chars 
    obj = Solution()
    buf = [''] * n
    chars_read = obj.read(buf, n)
    result_str = ''.join(buf[:chars_read])
    print("chars_read =", chars_read, ", buf content =", repr(result_str))
    return chars_read, result_str
if __name__ == "__main__":
    run_test("abc", 4)
    run_test("abcde", 5)
    run_test("abcdABCD1234", 12)