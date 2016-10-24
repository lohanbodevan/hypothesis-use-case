# Hypothesis example

This is a simple example to show how to use [Hyposthesis](https://hypothesis.readthedocs.io/en/latest/index.html) library that generates random data to your tests.

## Install
```
    $ make install
```

## Test
```
    $ make test
```

Just one unit test like this:
```
    @given(st.integers(), st.integers())
    def test_ints_sum(self, x, y):
        logging.basicConfig(level=logging.INFO)
        logging.getLogger('HYPOTHESIS').info('Testing {} plus {}'.format(x, y))

        assert x + y == sum_numbers(x, y)
```

Can be covered by many different inputs:

<img alt="Tests" src="http://res.cloudinary.com/lbodevan/image/upload/v1477284272/Captura_de_Tela_2016-10-24_a%CC%80s_02.43.38_zgkoww.png">
