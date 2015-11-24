Warsztaty PYAGH z testowania
============================

Start
=====

Na początek stworzymy wirtualne środowisko pythona.

    virtualenv venv

Następnie je aktywujemy:

    source venv/bin/activate

Oraz zainstalujemy zależności:

    pip install pip --upgrade
    pip install -r requirements.txt


Co chcemy zaimplementować?
==========================

Bibliotekę (lib) kantora walut.

Jak chcemy jej używać?
======================

```python

    from exchange import CurrencyExchanger

    e = CurrencyExchanger()
    e.exchange(1, 'eur', 'pln')
    >>> 4.24
    e.exchange(value=1, input_currency='eur', output_currency='usd')
    >>> 1.064

    e = CurrencyExchanger(default_currency='pln')
    e.exchange(1, 'eur')
    >>> 4.24

```

Jak chcemy tego używać w przypadku dynamicznych danych?

Wykorzystamy API https://currency-api.appspot.com (pod tym linkiem też dokumentacja).

Działa ono tak, że konstruując urla np. `https://currency-api.appspot.com/api/eur/pln.json`

Dostajemy w odpowiedzi `jsona` z przelicznikiem eur/pln.

    {"success":true,"source":"EUR","target":"PLN","rate":4.2609367,"amount":4.26,"message":""}


Przykładowe użycie może wyglądać tak:

```python

    from exchange import CurrencyExchanger, OnlineRates

    exchange_rates = OnlineRates(src='https://currency-api.appspot.com/api/eur/pln.json').get_data()
    e = CurrencyExchanger(exchange_rates=exchange_rates)
    e.exchange(1, 'eur')
    >>> 4.26

```

Lub jeszcze bardziej dynamicznie:

```python

    from exchange import CurrencyExchanger, OnlineRates

    exchange_rates = OnlineRates(src='https://currency-api.appspot.com/api/%(input_currency)s/%(output_currency)s.json')
    e = CurrencyExchanger(exchange_rates=exchange_rates)
    e.exchange(1, 'eur')
    >>> 4.26

```

W unittestach nie chcemy łączyć się z siecią, zalecane jest więc użycie `mock` (patrz zakomentowany test).



Uruchomienie testów
===================

    py.test

Pobieranie aktualnych kursów przez API
======================================

Użyjemy biblioteki requests
