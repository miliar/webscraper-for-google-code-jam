import googlers
import tongues

__author__ = 'dmorgant'

import unittest

class CodeJammer(unittest.TestCase):
    def test_store_credit_small(self):
        self.read_and_process("tongues", "A-small-attempt0", lambda x: tongues.process(x))

    def test_googlers_small(self):
        self.read_and_process("googlers", "B-small-attempt0", lambda x: googlers.process(x))

    def test_googlers_large(self):
        self.read_and_process("googlers", "B-large-attempt0", lambda x: googlers.process(x))

    def read_and_process(self, problemName, size, processor):
        with open(problemName + "-files/" + size + ".in", 'r') as f:
            contents = f.read()
            f.close()
        output = processor(contents)
        with open(problemName + "-files/" + problemName + "-" + size + ".out", 'w') as f:
            f.write(output)


if __name__ == '__main__':
    unittest.main()