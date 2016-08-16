#################################################
Podstawowe typy zdarzeń obsługiwane przez SAREhub
#################################################
Każde zdarzenie w systemie SAREhub powinno posiadać swoją ścieżkę routingu, która definiuje gdzie (do jakiego modułu) 
komunikat zostanie dostarczony. Klucz routingu składa się z od dwóch do pięciu elementów oddzielonych kropką:

* _hub[hub_id].destination_
* _hub[hub_id].destination.key1_
* _hub[hub_id].destination.account_id.key1_
* _hub[hub_id].destination.account_id.type.key1_
* _hub[hub_id].destination.type.key1_
* _hub[hub_id].type.key1_

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

* _hub122.sare_
* _hub123.sare.1_
* _hub234.sare.1.message.email_
* _hub100.message.email_
* _hub987.user.cookie_

Podstawowe zdarzenia
====================
* dla zdarzeń typu user:
    - **online** - informuje, że użytkownik właśnie pojawił się online. Obiekt params _MUSI_ zawierać atrybut time 
    zawierający timestamp zdarzenia. W przypadku jeżeli użytkownik odwiedza stronę WWW, obiekt params _POWINIEN_ zawierać
    atrybut url zawierający URL odwiedzaną stronę,
    - **info** - obiekt params _MOŻE_ zawierać wartości innych kluczy, które powiązane są z tym użytkownikiem,
    - **tag** - użytkownik został oznaczony tagiem. Obiekt params _MUSI_ zawierać atrybut name . Wartością atrybutu name 
    może być nazwa tagu lub tablica tagów,
    - **funnel** - użytkownik wszedł w lejek sprzedażowy. Obiekt params _MUSI_ zawierać atrybut time zawierający 
    timestamp zdarzenia oraz _POWINIEN_ zawierać atrybut level z wartością     określającą poziom zaangażowania 
    użytkownika w wartościach od 0 do 100 (osiągnięto cel).
* dla zdarzeń typu discover:
    - **discover** - payload _MUSI_ zawierać przynajmniej jeden z kluczy. Jest to komunikat z prośbą o informacje o 
    użytkowniku identyfikowanym przez klucz. Obiekt params może zawierać atrybut search. Jego wartością jest string 
    (lub tablica stringów) określający szukane parametry, w szczególności klucze (email, emailmd5, cookie, mobile, phone, 
    postal).
* dla zdarzeń typu message:
    - **message** – payload _MUSI_ zawierać przynajmniej jeden z kluczy. Obiekt params _POWINIEN_ zawierać atrybut body, 
    którego wartością jest treść wiadomości skierowanej do użytkownika. Obiekt params może zawierać również atrybuty będące 
    nazwami kluczy których wartościami są obiekty.
    
Dla klucza **email** obiekt params _POWINIEN_ być zbudowany wg następującego schematu (dopuszczalne są dodatkowe argumenty):

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


Dla klucza **mobile** obiekt params _POWINIEN_ być zbudowany wg następującego schematu (dopuszczalne są dodatkowe argumenty):
.. code-block:: json

{  
  "from": "nadawca sms",  
  "to": "odbiorca sms",  
  "body": "treść sms"  
}
