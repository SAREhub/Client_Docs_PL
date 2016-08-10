## Podstawowe typy zdarzeń obsługiwane przez SAREhub

Każde zdarzenie w systemie SAREhub powinno posiadać swoją ścieżkę routingu, która definiuje gdzie (do jakiego modułu) 
komunikat zostanie dostarczony. Klucz routingu składa się z od dwóch do pięciu elementów oddzielonych kropką:

- _hub[hub_id].destination_
- _hub[hub_id].destination.key1_
- _hub[hub_id].destination.account_id.key1_
- _hub[hub_id].destination.account_id.type.key1_
- _hub[hub_id].destination.type.key1_
- _hub[hub_id].type.key1_

Pierwszy element (hubId) oznacza identyfikator huba do którego chcemy publikować dane (np. hub112).

Element destination oznacza miejsce docelowe (moduł) gdzie zdarzenie ma trafić.

Element account_id oznacza idetyfikator zintegrowanego konta klienta w zdalnym systemie (module) do którego 
publikujemy dane.

Część type definiuje typ zdarzenia:

- **discover** – wiadomości z prośbą o informacje użytkowniku,
- **user** – wiadomości przekazujące informacje na temat użytkownika,
- **message** – wiadomości zawierające przekaz (wiadomość dla użytkownika).

Ostatni element służy do określenia typu klucza użytkownika. Aktualnie są obsługiwane następujące rodzaje kluczy:

- **email**
- **emailmd5**
- **cookie**
- **mobile**
- **phone**
- **postal**

Poprawnymi kluczami routingu są, np.:

- _hub122.sare_
- _hub123.sare.1_
- _hub234.sare.1.message.email_
- _hub100.message.email_
- _hub987.user.cookie_
