#################################################
Podstawowe typy zdarzeń
#################################################
Każde zdarzenie w systemie SAREhub powinno posiadać swoją ścieżkę routingu, która definiuje gdzie (do jakiego modułu)
komunikat zostanie dostarczony. Klucz routingu składa się z od dwóch do pięciu elementów oddzielonych kropką:

* hub[hub_id].destination
* hub[hub_id].destination.key1
* hub[hub_id].destination.account_id.key1
* hub[hub_id].destination.account_id.type.key1
* hub[hub_id].destination.type.key1
* hub[hub_id].type.key1

Pierwszy element (hubId) oznacza identyfikator huba do którego chcemy publikować dane (np. hub112).

Element destination oznacza miejsce docelowe (moduł) gdzie zdarzenie ma trafić.

Element account_id oznacza idetyfikator zintegrowanego konta klienta w zdalnym systemie (module) do którego
publikujemy dane.

Część type definiuje typ zdarzenia:

* **discover** – wiadomości z prośbą o informacje użytkowniku,
* **user** – wiadomości przekazujące informacje na temat użytkownika,
* **message** – wiadomości zawierające przekaz (wiadomość dla użytkownika).

Ostatni element służy do określenia typu klucza użytkownika. Aktualnie są obsługiwane następujące rodzaje kluczy:

* **email**
* **emailmd5**
* **cookie**
* **mobile**
* **phone**
* **postal**

Poprawnymi kluczami routingu są, np.:

* hub122.sare
* hub123.sare.1
* hub234.sare.1.message.email
* hub100.message.email
* hub987.user.cookie

Podstawowe zdarzenia
====================
* dla zdarzeń typu user:

 * **online** - informuje, że użytkownik właśnie pojawił się online. Obiekt params **MUSI** zawierać atrybut time zawierający timestamp zdarzenia. W przypadku jeżeli użytkownik odwiedza stronę WWW, obiekt params **POWINIEN** zawierać atrybut url zawierający URL odwiedzaną stronę,
 * **info** - obiekt params **MOŻE** zawierać wartości innych kluczy, które powiązane są z tym użytkownikiem,
 * **tag** - użytkownik został oznaczony tagiem. Obiekt params **MUSI** zawierać atrybut name. Wartością atrybutu name może być nazwa tagu lub tablica tagów,
 * **funnel** - użytkownik wszedł w lejek sprzedażowy. Obiekt params **MUSI** zawierać atrybut time zawierający timestamp zdarzenia oraz **POWINIEN** zawierać atrybut level z wartością określającą poziom zaangażowania użytkownika w wartościach od 0 do 100 (osiągnięto cel).

* dla zdarzeń typu discover:

 * **discover** - payload **MUSI** zawierać przynajmniej jeden z kluczy. Jest to komunikat z prośbą o informacje o użytkowniku identyfikowanym przez klucz. Obiekt params może zawierać atrybut search. Jego wartością jest string (lub tablica stringów) określający szukane parametry, w szczególności klucze (email, emailmd5, cookie, mobile, phone, postal).

* dla zdarzeń typu message:

 * **message** – payload **MUSI** zawierać przynajmniej jeden z kluczy. Obiekt params **POWINIEN** zawierać atrybut body, którego wartością jest treść wiadomości skierowanej do użytkownika. Obiekt params może zawierać również atrybuty będące nazwami kluczy których wartościami są obiekty.

Dla klucza **email** obiekt params **POWINIEN** być zbudowany wg następującego schematu (dopuszczalne są dodatkowe argumenty):

.. code-block:: json

   {
    "from": "nadawca emaila",
    "to": "odbiorca emaila",
    "subject": "tytuł emaila",
    "body": {
     "txt": "string lub object z parametrem url",
     "html": "string lub object z parametrem url"
    }
   }


Dla klucza **mobile** obiekt params **POWINIEN** być zbudowany wg następującego schematu (dopuszczalne są dodatkowe argumenty):

.. code-block:: json

   {
    "from": "nadawca sms",
    "to": "odbiorca sms",
    "body": "treść sms"
   }

Struktura zdarzeń w SAREhub
========================================

Każde zdarzenie ma następujący format:

.. code-block:: json

  {
    "type": "object",
    "title": "Zdarzenie użytkownika.",
    "properties": {
        "type": {
            "type": "string",
            "title": "Typ zdarzenia."
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
        "params": {
            "type": "object",
            "title": "Atrybuty opisujące konkretne zdarzenie.",
            "properties": {}
        }
    },
    "required": [
        "type",
        "user",
        "time",
        "params"
    ]
  }

Lista zdarzeń oraz atrybutów je opisujących
===========================================

* **tag** - Tagowanie użytkownika.

.. code-block:: json

  {
    "type": "object",
    "title": "Atrybuty zdarzenia tag.",
    "properties": {
        "name": {
            "type": "string",
            "title": "Nazwa tagu."
        }
    },
    "required": [
        "name"
    ]
  }

Przykład:

.. code-block:: json

  {
    "type": "tag",
    "user": {
        "cookie": "33413026813181711"
    },
    "time": 1475756549,
    "params": {
        "name": "4|flowchart-filter_previous_block-1461074520658|flowchart-alert-1461074548667"
    }
  }

* **discover** - Prośba o informacje o użytkowniku identyfikowanym przez dany klucz.

.. code-block:: json

  {
    "type": "object",
    "title": "Atrybuty zdarzenia discover.",
    "properties": {
        "search": {
            "type": "string",
            "title": "Typ klucza użytkownika.",
            "description": "Typ Klucza użytkownika dla którego wyszukiwane są informacje."
        },
        "processing_message": {
            "type": "object",
            "title": "Wiadomość zwrotna.",
            "description": "Zdarzenie które ma być wywołane po powrocie komunikatu z szukanymi informacjami. Do niego może zostać wstrzyknięta znaleziona wartość klucza.",
            "properties": {}
        }
    },
    "required": [
        "search"
    ]
  }

Przykład:

.. code-block:: json

  {
    "type": "discover",
    "user": {
        "cookie": "33413026813181711"
    },
    "time": 1475756549,
    "params": {
        "search": "id",
        "processing_message": {
            "type": "tag",
            "user": {
                "cookie": "33413026813181711"
            },
            "time": 1475756549,
            "params": {
                "name": "4|flowchart-filter_previous_block-1461074520658|flowchart-alert-1461074548667"
            }
        }
    }
  }

* **info** - Zawiera informacje na temat danego klucza powiązanym z danym użytkownikiem.

.. code-block:: json

    {
      "type": "object",
      "title": "Atrybuty zdarzenia info.",
      "properties": {}
    }

Przykład:

.. code-block:: json

  {
    "type": "info",
    "user": {
        "cookie": "83966095470796834"
    },
    "time": 1475756549,
    "params": {
        "email": [
            "it@sarehub.com"
        ]
    }
  }

* **online** - Zdarzenie informuje, że użytkownik właśnie pojawił się online.

.. code-block:: json

  {
    "type": "object",
    "title": "Atrybuty zdarzenia online.",
    "description": "Atrybuty zdarzenia online wysyłanego przez system SAREweb.",
    "properties": {
        "url": {
            "type": "string",
            "title": "Url strony."
        },
        "url_norm": {
            "type": "string",
            "title": "Znormalizowany url strony."
        },
        "uri": {
            "type": "string",
            "title": "Uri strony."
        },
        "domain": {
            "type": "string",
            "title": "Domena strony."
        },
        "ref_type": {
            "type": "string",
            "title": "Typ referera."
        },
        "seconds_on_domain": {
            "type": "integer",
            "title": "Czas pobyt na danej domenie."
        },
        "visited_sites": {
            "type": "integer",
            "title": "Liczba odwiedzonych stron"
        },
        "ip": {
            "type": "integer",
            "title": "Ip użytownika.",
            "description": "IP użytkownika zapisane w formie liczby całkowitej."
        },
        "tmp_cookie": {
            "type": "string",
            "title": "Sesja użytkownika."
        },
        "extra": {
            "type": "string",
            "title": "Dodatkowe parametry."
        },
        "utm_source": {
            "type": "string",
            "title": "Tag Google Analitycs utm_source."
        },
        "utm_medium": {
            "type": "string",
            "title": "Tag Google Analitycs utm_medium."
        },
        "utm_term": {
            "type": "string",
            "title": "Tag Google Analitycs utm_term."
        },
        "utm_content": {
            "type": "string",
            "title": "Tag Google Analitycs utm_content."
        },
        "utm_campaign": {
            "type": "string",
            "title": "Tag Google Analitycs utm_campaign."
        },
        "session_referer": {
            "type": "string",
            "title": "Referer pierwszego wejścia na stronę, ustawiany dla całej sesji."
        },
        "session_ref_type": {
            "type": "string",
            "title": "Typ referera pierwszego wejścia na stronę, ustawiany dla całej sesji."
        },
        "session_ref_site": {
            "type": "string",
            "title": "Strona referera pierwszego wejścia na stronę, ustawiany dla całej sesji."
        },
        "session_ref_keywords": {
            "type": "string",
            "title": "Słowa kluczowe pierwszego wejścia na stronę, ustawiany dla całej sesji."
        },
        "session_utm_source": {
            "type": "string",
            "title": "Tag Google Analitycs utm_source pierwszego wejścia na stronę, ustawiany dla całej sesji."
        },
        "session_utm_medium": {
            "type": "string",
            "title": "Tag Google Analitycs utm_medium pierwszego wejścia na stronę, ustawiany dla całej sesji."
        },
        "session_utm_term": {
            "type": "string",
            "title": "Tag Google Analitycs utm_term pierwszego wejścia na stronę, ustawiany dla całej sesji."
        },
        "session_utm_content": {
            "type": "string",
            "title": "Tag Google Analitycs utm_content pierwszego wejścia na stronę, ustawiany dla całej sesji."
        },
        "session_utm_campaign": {
            "type": "string",
            "title": "Tag Google Analitycs utm_campaign pierwszego wejścia na stronę, ustawiany dla całej sesji."
        },
        "known": {
            "type": "boolean",
            "title": "Znany użytkownik.",
            "description": "Informuje o tym czy w systemie SAREweb użytkownik posiada adres email."
        }
    },
    "required": [
        "url",
        "url_norm",
        "uri",
        "domain",
        "ref_type",
        "seconds_on_domain",
        "visited_sites",
        "ip",
        "tmp_cookie",
        "extra",
        "utm_source",
        "utm_medium",
        "utm_term",
        "utm_content",
        "utm_campaign",
        "session_referer",
        "session_ref_type",
        "session_ref_site",
        "session_ref_keywords",
        "session_utm_source",
        "session_utm_medium",
        "session_utm_term",
        "session_utm_content",
        "session_utm_campaign",
        "known"
    ]
  }

Przykład:

.. code-block:: json

  {
    "type": "online",
    "user": {
        "cookie": "22281308789088642"
    },
    "time": 1475756549,
    "params": {
        "url": "http://urlstrony.pl/samochod?utm_source=facebook&utm_medium=test&utm_campaign=zabawki",
        "url_norm": "http://urlstrony.pl/samochod?utm_source=facebook&utm_medium=test&utm_campaign=zabawki",
        "uri": "/?utm_source=facebook&utm_medium=test&utm_campaign=zabawki",
        "domain": "urlstrony.pl",
        "ref_type": "direct",
        "seconds_on_domain": 166,
        "visited_sites": 1,
        "ip": 1408141498,
        "tmp_cookie": "66978568417584187",
        "extra": "",
        "utm_source": "facebook",
        "utm_medium": "test",
        "utm_term": "",
        "utm_content": "",
        "utm_campaign": "zabawki",
        "session_referer": "",
        "session_ref_type": "direct",
        "session_ref_site": "",
        "session_ref_keywords": "",
        "session_utm_source": "facebook",
        "session_utm_medium": "test",
        "session_utm_term": "",
        "session_utm_content": "",
        "session_utm_campaign": "zabawki",
        "known": false
    }
  }

* **offline** - Zdarzenie informuje, że użytkownik przeszedł w tryb offline.

.. code-block:: json

  {
    "type": "object",
    "title": "Atrybuty zdarzenia offline.",
    "description": "Atrybuty zdarzenia offline wysyłanego przez system SAREweb.",
    "properties": {
        "url": {
            "type": "string",
            "title": "Url strony."
        },
        "url_norm": {
            "type": "string",
            "title": "Znormalizowany url strony."
        },
        "uri": {
            "type": "string",
            "title": "Uri strony."
        },
        "domain": {
            "type": "string",
            "title": "Domena strony."
        },
        "tmp_cookie": {
            "type": "string",
            "title": "Sesja użytkownika."
        },
        "seconds_on_url": {
            "type": "integer",
            "title": "Czas pobytu na danej stronie."
        },
        "seconds_on_domain": {
            "type": "integer",
            "title": "Czas pobyt na danej domenie."
        },
        "visited_sites": {
            "type": "integer",
            "title": "Liczba odwiedzonych stron."
        },
        "session_referer": {
            "type": "string",
            "title": "Referer pierwszego wejścia na stronę, ustawiany dla całej sesji."
        },
        "session_ref_type": {
            "type": "string",
            "title": "Typ referera pierwszego wejścia na stronę, ustawiany dla całej sesji."
        },
        "session_ref_site": {
            "type": "string",
            "title": "Strona referera pierwszego wejścia na stronę, ustawiany dla całej sesji."
        },
        "session_ref_keywords": {
            "type": "string",
            "title": "Słowa kluczowe pierwszego wejścia na stronę, ustawiany dla całej sesji."
        },
        "session_utm_source": {
            "type": "string",
            "title": "Tag Google Analitycs utm_source pierwszego wejścia na stronę, ustawiany dla całej sesji."
        },
        "session_utm_medium": {
            "type": "string",
            "title": "Tag Google Analitycs utm_medium pierwszego wejścia na stronę, ustawiany dla całej sesji."
        },
        "session_utm_term": {
            "type": "string",
            "title": "Tag Google Analitycs utm_term pierwszego wejścia na stronę, ustawiany dla całej sesji."
        },
        "session_utm_content": {
            "type": "string",
            "title": "Tag Google Analitycs utm_content pierwszego wejścia na stronę, ustawiany dla całej sesji."
        },
        "session_utm_campaign": {
            "type": "string",
            "title": "Tag Google Analitycs utm_campaign pierwszego wejścia na stronę, ustawiany dla całej sesji."
        }
    },
    "required": [
        "url",
        "url_norm",
        "tmp_cookie",
        "domain",
        "seconds_on_url",
        "seconds_on_domain",
        "visited_sites",
        "session_referer",
        "session_ref_type",
        "session_ref_site",
        "session_ref_keywords",
        "session_utm_source",
        "session_utm_medium",
        "session_utm_term",
        "session_utm_content",
        "session_utm_campaign"
    ]
  }

Przykład:

.. code-block:: json

  {
    "type": "offline",
    "user": {
        "cookie": "63608288842324163"
    },
    "time": 1475756549,
    "params": {
        "url": "http://urlstrony.pl/samochod?utm_source=facebook&utm_medium=test&utm_campaign=zabawki",
        "url_norm": "http://urlstrony.pl/samochod?utm_source=facebook&utm_medium=test&utm_campaign=zabawki",
        "uri": "/?utm_source=facebook&utm_medium=test&utm_campaign=zabawki",
        "domain": "urlstrony.pl",
        "tmp_cookie": "96372242750554029",
        "seconds_on_url": 23,
        "seconds_on_domain": 169,
        "visited_sites": 1,
        "session_referer": "",
        "session_ref_type": "direct",
        "session_ref_site": "",
        "session_ref_keywords": "",
        "session_utm_source": "facebook",
        "session_utm_medium": "test",
        "session_utm_term": "",
        "session_utm_content": "",
        "session_utm_campaign": "zabawki"
    }
  }

* **ping** - Zdarzenie informuje o pobycie użytkownika na stronie.

.. code-block:: json

  {
    "type": "object",
    "title": "Atrybuty zdarzenia ping.",
    "description": "Atrybuty zdarzenia ping wysyłanego przez system SAREweb",
    "properties": {
        "url": {
            "type": "string",
            "title": "Url strony."
        },
        "url_norm": {
            "type": "string",
            "title": "Znormalizowany url strony."
        },
        "uri": {
            "type": "string",
            "title": "Uri strony."
        },
        "domain": {
            "type": "string",
            "title": "Domena strony."
        },
        "tmp_cookie": {
            "type": "string",
            "title": "Sesja użytkownika"
        },
        "seconds_on_url": {
            "type": "integer",
            "title": "Czas pobytu na danej stronie."
        },
        "seconds_on_domain": {
            "type": "integer",
            "title": "Czas pobyt na danej domenie."
        },
        "visited_sites": {
            "type": "integer",
            "title": "Liczba odwiedzonych stron."
        },
        "session_referer": {
            "type": "string",
            "title": "Referer pierwszego wejścia na stronę, ustawiany dla całej sesji."
        },
        "session_ref_type": {
            "type": "string",
            "title": "Typ referera pierwszego wejścia na stronę, ustawiany dla całej sesji."
        },
        "session_ref_site": {
            "type": "string",
            "title": "Strona referera pierwszego wejścia na stronę, ustawiany dla całej sesji."
        },
        "session_ref_keywords": {
            "type": "string",
            "title": "Słowa kluczowe pierwszego wejścia na stronę, ustawiany dla całej sesji."
        },
        "session_utm_source": {
            "type": "string",
            "title": "Tag Google Analitycs utm_source pierwszego wejścia na stronę, ustawiany dla całej sesji."
        },
        "session_utm_medium": {
            "type": "string",
            "title": "Tag Google Analitycs utm_medium pierwszego wejścia na stronę, ustawiany dla całej sesji."
        },
        "session_utm_term": {
            "type": "string",
            "title": "Tag Google Analitycs utm_term pierwszego wejścia na stronę, ustawiany dla całej sesji."
        },
        "session_utm_content": {
            "type": "string",
            "title": "Tag Google Analitycs utm_content pierwszego wejścia na stronę, ustawiany dla całej sesji."
        },
        "session_utm_campaign": {
            "type": "string",
            "title": "Tag Google Analitycs utm_campaign pierwszego wejścia na stronę, ustawiany dla całej sesji."
        }
    },
    "required": [
        "url",
        "url_norm",
        "uri",
        "domain",
        "tmp_cookie",
        "seconds_on_url",
        "seconds_on_domain",
        "visited_sites",
        "session_referer",
        "session_ref_type",
        "session_ref_site",
        "session_ref_keywords",
        "session_utm_source",
        "session_utm_medium",
        "session_utm_term",
        "session_utm_content",
        "session_utm_campaign"
    ]
  }

Przykład:

.. code-block:: json

  {
    "type": "ping",
    "user": {
        "cookie": "46002764640577325"
    },
    "time": 1475756549,
    "params": {
        "url": "http://urlproduktu.pl/samochod?utm_source=facebook&utm_medium=test&utm_campaign=zabawki",
        "url_norm": "http://urlproduktu.pl/samochod?utm_source=facebook&utm_medium=test&utm_campaign=zabawki",
        "uri": "/?utm_source=facebook&utm_medium=test&utm_campaign=zabawki",
        "domain": "urlproduktu.pl",
        "tmp_cookie": "96372242750554029",
        "seconds_on_url": 14,
        "seconds_on_domain": 98,
        "visited_sites": 1,
        "session_referer": "",
        "session_ref_type": "direct",
        "session_ref_site": "",
        "session_ref_keywords": "",
        "session_utm_source": "facebook",
        "session_utm_medium": "medium",
        "session_utm_term": "",
        "session_utm_content": "",
        "session_utm_campaign": "zabawki"
    }
  }
