#################################################
Zdarzenia koszykowe
#################################################
Zdarzenia koszykowe wysyłane podczas procesu zaupowego.

Format zdarzenia koszykowego
============================

Każde zdarzenie koszykowe ma następujący format:

.. code-block:: json

  {
    "type": "object",
    "description": "Zdarzenie użytkownika",
    "required": [
        "type",
        "user",
        "time",
        "data"
    ],
    "properties": {
        "type": {
            "type": "string",
            "title": "Typ zdarzenia"
        },
        "user": {
            "type": "object",
            "title": "Klucze identyfikujące użytkownika.",
            "properties": {}
        },
        "time": {
            "type": "integer",
            "title": "Czas wystąpienia zdarzenia."
        },
        "data": {
            "type": "object",
            "title": "Atrybuty opisujące konkretne zdarzenie.",
            "properties": {}
        }
    }
  }

Lista zdarzeń oraz atrybutów je opisujących
===========================================

* **category_seen** - zdarzenie wysyłane w momencie wejścia w daną kategorię

.. code-block:: json

  {
    "type": "object",
    "title": "Atrybuty zdarzenia category_seen",
    "properties": {
      "id": {
        "type": "string",
        "title": "Id kategrii."
      },
      "country": {
        "type": "string",
        "title": "Kraj docelowy.",
        "description": "Kraj docelowy product feeda w formacie ISO 3166-1 alfa-2."
      },
      "language": {
        "type": "string",
        "title": "Język product feeda.",
        "description": "Język w jakim przygotowany jest product feed w formacie ISO 639-1."
      }
    },
    "required": [
      "id",
      "country",
      "language"
    ]
  }

Przykład:

.. code-block:: json

  {
    "type": "category_seen",
    "user": {
        "cookie": "22281308789088642"
    },
    "time": "1469988000",
    "data": {
        "id": "nazwa kategorii",
        "country": "PL",
        "language": "pl"
    }
  }

* **product_seen** - zdarzenie wysyłane w momencie wejścia na dany produkt

.. code-block:: json

  {
    "type": "object",
    "title": "Atrybuty zdarzenia product_seen",
    "properties": {
        "id": {
            "type": "integer",
            "title": "Id Produktu."
        },
        "name": {
            "type": "string",
            "title": "Nazwa produktu."
        },
        "price": {
            "type": "integer",
            "title": "Cena produktu",
            "description": "Cena produktu podana w najniższym nominale"
        },
        "currency": {
            "type": "string",
            "title": "Kod waluty"
        },
        "url": {
            "type": "string",
            "title": "URL produktu."
        },
        "category": {
            "type": "array",
            "title": "Kategorie produktu.",
            "items": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "string",
                        "title": "Id kategorii."
                    }
                },
                "required": [
                    "id"
                ]
            }
        },
        "country": {
            "type": "string",
            "title": "Kraj docelowy.",
            "description": "Kraj docelowy product feeda w formacie ISO 3166-1 alfa-2."
        },
        "language": {
            "type": "string",
            "title": "Język product feeda.",
            "description": "Język w jakim przygotowany jest product feed w formacie ISO 639-1."
        }
    },
    "required": [
        "id",
        "name",
        "price",
        "currency",
        "url",
        "category",
        "country",
        "language"
    ]
  }

Przykład:

.. code-block:: json

  {
    "type": "product_seen",
    "user": {
        "cookie": "22281308789088642"
    },
    "time": 1469988000,
    "data": {
        "country": "PL",
        "language": "pl",
        "id": 1,
        "name": "Samochód zabawka",
        "price": 15900,
        "currency": "pln",
        "url": "http://urlproduktu.pl/samochod",
        "category": [
            {
                "id": "zabawki"
            },
            {
                "id": "samochody"
            }
        ]
    }
  }

* **cart_added_product** - zdarzenie wysyłane w momencie dodania produktu do koszyka

.. code-block:: json

  {
    "type": "object",
    "title": "Atrybuty zdarzenia cart_added_product",
    "properties": {
        "cart_id": {
            "type": "string",
            "title": "Id koszyka"
        },
        "product_id": {
            "type": "integer",
            "title": "Id Produktu."
        },
        "name": {
            "type": "string",
            "title": "Nazwa produktu."
        },
        "url": {
            "type": "string",
            "title": "URL produktu."
        },
        "price": {
            "type": "integer",
            "title": "Cena produktu",
            "description": "Cena produktu podana w najniższym nominale"
        },
        "currency": {
            "type": "string",
            "title": "Kod waluty"
        },
        "quantity": {
            "type": "integer",
            "title": "Ilość produktu",
            "description": "Ilość produktu dodanego do koszyka"
        },
        "extra": {
            "type": "object",
            "title": "Dodatowe parametry",
            "description": "Dodatkowe parametry produktu np. rozmiar, kolor itd",
            "properties": {}
        },
        "category": {
            "type": "array",
            "title": "Kategorie produktu.",
            "items": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "string",
                        "title": "Id kategorii."
                    }
                },
                "required": [
                    "id"
                ]
            }
        },
        "country": {
            "type": "string",
            "title": "Kraj docelowy.",
            "description": "Kraj docelowy product feeda w formacie ISO 3166-1 alfa-2."
        },
        "language": {
            "type": "string",
            "title": "Język product feeda.",
            "description": "Język w jakim przygotowany jest product feed w formacie ISO 639-1."
        }
    },
    "required": [
        "cart_id",
        "product_id",
        "price",
        "currency",
        "quantity",
        "url",
        "category",
        "country",
        "language"
    ]
  }

Przykład:

.. code-block:: json

  {
    "type": "cart_added_product",
    "user": {
        "cookie": "22281308789088642"
    },
    "time": 1469988000,
    "data": {
        "cart_id": "1",
        "product_id": 5578,
        "price": 9900,
        "currency": "pln",
        "quantity": 1,
        "name": "Nazwa produktu",
        "url": "http://urlproduktu.pl/samochod",
        "extra": {
            "size": "L",
            "color": "czerwony"
        },
        "category": [
            {
                "id": "zabawki"
            },
            {
                "id": "samochody"
            }
        ],
        "country": "PL",
        "language": "pl"
    }
  }

* **cart_removed_product** - zdarzenie wysyłane w momencie usunięcia produktu do koszyka

.. code-block:: json

  {
    "type": "object",
    "title": "Atrybuty zdarzenia cart_removed_product",
    "properties": {
        "cart_id": {
            "type": "string",
            "title": "Id koszyka"
        },
        "product_id": {
            "type": "integer",
            "title": "Id Produktu."
        },
        "price": {
            "type": "integer",
            "title": "Cena produktu",
            "description": "Cena produktu podana w najniższym nominale"
        },
        "currency": {
            "type": "string",
            "title": "Kod waluty"
        },
        "quantity": {
            "type": "integer",
            "title": "Ilość produktu",
            "description": "Parametr ten przyjmuje wartość aktualnego stanu ilości produktu w koszyku."
        },
        "country": {
            "type": "string",
            "title": "Kraj docelowy.",
            "description": "Kraj docelowy product feeda w formacie ISO 3166-1 alfa-2."
        },
        "language": {
            "type": "string",
            "title": "Język product feeda.",
            "description": "Język w jakim przygotowany jest product feed w formacie ISO 639-1."
        }
    },
    "required": [
        "cart_id",
        "product_id",
        "price",
        "currency",
        "quantity",
        "country",
        "language"
    ]
  }

Przykład:

.. code-block:: json

  {
    "type": "cart_removed_product",
    "user": {
        "cookie": "22281308789088642"
    },
    "time": 1469988000,
    "data": {
        "cart_id": "1",
        "product_id": 5578,
        "price": 9900,
        "currency": "pln",
        "quantity": 1,
        "country": "PL",
        "language": "pl"
    }
  }

* **cart_changed_product_quantity** - zdarzenie wysyłane w momencie zmiany ilości produktu w koszyku

.. code-block:: json

  {
    "type": "object",
    "title": "Atrybuty zdarzenia cart_changed_product_quantity",
    "properties": {
        "cart_id": {
            "type": "string",
            "title": "Id koszyka"
        },
        "product_id": {
            "type": "integer",
            "title": "Id Produktu."
        },
        "quantity": {
            "type": "integer",
            "title": "Ilość produktu",
            "description": "Parametr ten przyjmuje wartość aktualnego stanu ilości produktu w koszyku."
        },
        "country": {
            "type": "string",
            "title": "Kraj docelowy.",
            "description": "Kraj docelowy product feeda w formacie ISO 3166-1 alfa-2."
        },
        "language": {
            "type": "string",
            "title": "Język product feeda.",
            "description": "Język w jakim przygotowany jest product feed w formacie ISO 639-1."
        }
    },
    "required": [
        "cart_id",
        "product_id",
        "quantity",
        "country",
        "language"
    ]
  }

Przykład:

.. code-block:: json

  {
    "type": "cart_changed_product_quantity",
    "user": {
        "cookie": "22281308789088642"
    },
    "time": 1469988000,
    "data": {
        "cart_id": "1",
        "product_id": "5578",
        "quantity": 1,
        "country": "PL",
        "language": "pl"
    }
  }

* **cart_checkout_started** - zdarzenie wysyłane w momencie rozpoczęcia procesu zamówienia

.. code-block:: json

  {
    "type": "object",
    "title": "Atrybuty zdarzenia cart_checkout_started",
    "properties": {
        "cart_id": {
            "type": "string",
            "title": "Id koszyka."
        }
    },
    "required": [
        "cart_id"
    ]
  }

Przykład:

.. code-block:: json

  {
    "type": "cart_checkout_started",
    "user": {
        "cookie": "22281308789088642"
    },
    "time": 1469988000,
    "data": {
        "cart_id": "1"
    }
  }

* **cart_checkout_step** - zdarzenie wysyłane w momencie kolejnego kroku procesu zamówienia

.. code-block:: json

  {
    "type": "object",
    "title": "Atrybuty zdarzenia cart_checkout_step",
    "properties": {
        "cart_id": {
            "type": "string",
            "title": "Id koszyka."
        }
    },
    "required": [
        "cart_id"
    ]
  }

Przykład:

Krok wypełnienia danych do wysyłki:

.. code-block:: json

  {
    "type": "cart_checkout_step",
    "user": {
        "cookie": "22281308789088642"
    },
    "time": 1469988000,
    "data": {
        "step_id": "registration",
        "cart_id": "1"
    }
  }

Krok zapłaty za zamówienie:

.. code-block:: json

  {
      "type": "cart_checkout_step",
      "user": {
          "cookie": "22281308789088642"
      },
      "time": 1469988000,
      "data": {
          "step_id": "payment",
          "cart_id": "1"
      }
  }

* **cart_checkout_completed** - zdarzenie wysyłane w momencie zakończenia procesu zamówienia

.. code-block:: json

    {
      "type": "object",
      "title": "Atrybuty zdarzenia cart_checkout_completed",
      "properties": {
          "cart_id": {
              "type": "string",
              "title": "Id koszyka."
          }
      },
      "required": [
          "cart_id"
      ]
    }

Przykład:

.. code-block:: json

    {
      "type": "cart_checkout_completed",
      "user": {
          "cookie": "22281308789088642"
      },
      "time": 1469988000,
      "data": {
          "cart_id": "1"
      }
    }
