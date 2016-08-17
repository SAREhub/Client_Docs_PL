########
REST API
########

Wstęp
=====
Dokumentacja dla SAREhub REST API które umożliwia wysyłanie oraz pobieranie
danych z danych do/z SAREhuba.

Ścieżka
-------
Każde poniższe zapytanie zaczyna się od poniższego adresu URL: https://api.sarehub.com/v1

Format
------
Wszystkie zapytania zwracają dane w formacie **JSON**.

Kody statusów
-------------

* **200** Pomyślny GET.
* **201** Pomyślny POST i PUT.
* **401** Nieuwierzytelniony.
* **403** Zabroniony.
* **400** Będne zapytanie.

Zabezpieczenia
--------------

* REST API jest dozwolone tylko dla adresów IP dopisanych do whitelisty.
* Każda metoda jest zabezpieczona poprzez uwierzytelnienie Basic Auth.

Publish
=======
**POST /publish/routing/:routing**

Metoda umożliwia wysłanie (opublikowanie) danych do szyny SAREhub. Parametr :routing powinien
przyjąć ciąg routingu, np. hub1.message.email

**Treść zapytania**

W treści zapytania należy wysłać dane w formacie JSON zgodne z komunikatami SAREhub.

**Nagłówki**

Dodatkowo jest możliwość przesłania specjalnych nagłówków które dodają dodatkowe
opcje do komunikatu:

* **SAREhub-reply_to** - Parametr, który powinien zawierać ciąg routingu gdzie ma zostać wysłana odpowiedź na wysłany komunikat,
* **SAREhub-correlation_id** - Parametr przyjmujący dowolną wartość, umożliwia powiązanie komunikatu odpowiedzi z zapytaniem,
* **SAREhub-priority** - Parametr określający priorytet komunikatu (int),
* **SAREhub-delay** - Opóźnienie po jakim czasie (w sekundach) komunikat ma trafić do szyny SAREhub.

**Przykadowe zapytanie**

.. code-block:: bash

  $ curl -u module:secret https://api.sarehub.com/publish/routing/hub1.message.email
  \
  -H "Content-Type: application/json" \
  -X POST \
  -d
  '{"type":"message","user":{"email":"hub@sarehub.com"},"params":{"to":"hub@sarehub.com",
  "from":"test@sarehub.com","subject":"test","body":{"html":"test","txt":"test"}}}'

**Odpowiedź**

.. code-block:: json

  {
    "state": "success"
  }

**Odpowiedź w przypadku błędu**

.. code-block:: json

  {
    "state": "error",
    "message": "Treść błędu"
  }

Consume
=======
**GET /consume**

Metoda umożliwia pobieranie komunikatów z domyślnej kolejki. Obsługiwany moduł
powinien być skonfigurowany sposób kolejkowania w trybie "single".

**GET /consume/hub/:id**

Metoda umożliwia pobieranie komunikatów z kolejki huba o podanym identyfikatorze.
Obsługiwany moduł powinien być skonfigurowany sposób kolejkowania w trybie "single".

**GET /consume/queue/:queue_name**

Metoda umożliwia pobieranie komunikatów z dodatkowej kolejki o podanej nazwie. Obsługiwany
moduł powinien być skonfigurowany sposób kolejkowania w trybie "single".

**GET /consume/hub/:id/queue/:queue_name**

Obydwie powyższe metody jednocześnie.

**Parametry**

Do zapytania można dostać następujące parametry:

* **limit** - maksymalna liczba komunikautów jaka ma zostać pobrana (domyślnie 100).

**Przykadowe zapytanie**

.. code-block:: bash

   $ curl -u module:secret https://api.sarehub.com/consume?limit=2 \
   -H "Content-Type: application/json" \
   -X POST

Odpowiedź

.. code-block:: json

  {
    "state": "success",
    "count": 2,
    "statements": [
        {
          "type": "message",
          "user": {
            "email":"hub@sarehub.com"
          },
          "params": {
            "to": "hub@sarehub.com",
            "from": "test@sarehub.com",
            "subject": "test",
            "body": {
              "html": "test",
              "txt": "test"
            }
          }
        },
        {
          "type": "message",
          "user": {
            "email":"hub+test@sarehub.com"
          },
          "params": {
            "to": "hub+test@sarehub.com",
            "from": "test+test@sarehub.com",
            "subject": "test2",
            "body": {
              "html": "test2",
              "txt": "test2"
            }
          }
        }
      ]
    }

**Odpowiedź w przypadku błędu**

.. code-block:: json

  {
    "state": "error",
    "message": "Treść błędu"
  }
