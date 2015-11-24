import pytest
from exchange import CurrencyExchanger, UnsupportedExchangeRateError


# example exchange rates for testing
exchange_rates = {
    ('eur', 'pln'): 4.24,
    ('pln', 'eur'): 0.25,
    ('usd', 'pln'): 3.8,
}


def test_euro_to_pln():
    e = CurrencyExchanger(exchange_rates=exchange_rates)
    assert e.exchange(value=1, input_currency='eur', output_currency='pln') == 4.24
    assert e.exchange(2, 'eur', 'pln') == 8.48


def test_pln_to_euro():
    e = CurrencyExchanger(exchange_rates=exchange_rates)
    assert e.exchange(1, input_currency='pln', output_currency='eur') == 0.25


def test_euro_to_pln_with_default_pln():
    # TODO: implement
    assert False


def test_unsupported_exchange_rates():
    e = CurrencyExchanger(exchange_rates={('eur', 'pln'): 4.24})
    assert e.exchange(1, 'eur', 'pln') == 4.24
    with pytest.raises(UnsupportedExchangeRateError):
        e.exchange(1, 'pln', 'usd')


def test_wrong_value():
    # TODO: implement
    assert False


def test_pln_to_pln():
    # TODO: implement
    assert False


# TODO: write your own test cases


# uncomment for example test using mock
# remember to import mock :)
# @mock.patch('exchange.OnlineRates.get_data', mock.Mock(return_value={('eur', 'pln'): 4.24, }))
# def test_eur_to_pln_with_data_from_external_api():
#     online_rates = OnlineRates(src='https://currency-api.appspot.com/api/eur/pln.json').get_data()
#     assert ('eur', 'pln') in online_rates
#    e = CurrencyExchanger(exchange_rates=online_rates)
#    assert e.exchange(1, 'eur', 'pln') == 4.24
#    assert e.exchange(2, 'eur', 'pln') == 8.48
