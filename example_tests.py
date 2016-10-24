import logging
import unittest

from hypothesis import given
import hypothesis.strategies as st

from example import sum_numbers


logging.basicConfig(level=logging.INFO)
log = logging.getLogger('HYPOTHESIS')


class TestEncoding(unittest.TestCase):

    @given(st.integers(), st.integers())
    def test_ints_sum(self, x, y):
        log.info('Testing {} plus {}'.format(x, y))

        assert x + y == sum_numbers(x, y)


if __name__ == '__main__':
    unittest.main()
