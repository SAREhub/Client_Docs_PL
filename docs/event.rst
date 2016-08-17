#########
Zdarzenie
#########

* Określa wystąpienie jakieś akcji np. wejście na stronę internetową.
* Jest generowane przez zintegrowane w SAREhabie systemy.
* Wywołuje odpowiednie akcje w nasłuchujących go systemach podłączonych do SAREhuba.

Specyfikacja zdarzenia
======================
Każde zdarzenie posiada swoją specyfikację, którą dostarcza zintegrowany z SAREhubem system.
Specyfikacja ta określa:

* identyfikator typu zdarzenia
* listę atrybutów zdarzenia
* opis

Magistrala zdarzeń
==================
 Jest to serce platformy SAREhub. Przez nie pomopowane są zdarzenia do zintegrowanych systemów.
 Rolę tej magistrali pełni w SAREhubie broker wiadomości RabbitMQ

Strumienie zdarzeń
=====================================================

* To ciąg zdarzeń.
* Zawiera jeden lub więcej typów zdarzeń.
* Jest przetwarzany przez rurociąg przetwarzania.

Rurociąg(pipeline) przetwarzania
================================
Rurociągiem przetwarzania nazywamy odpowiednie połączenie źródła(source) strumienia zdarzeń ze "zlewami"(sinks)
do których po kolei wpadają zdarzenia.

.. only:: latex

  .. image:: assets/img/diagrams/EventStreamProcessing.png

.. only:: html

  .. image:: assets/img/diagrams/EventStreamProcessing.svg




Źródła zdarzeń
==============
 System podłączony do SAREhuba może generować zdarzenia specyficzne dla siebie
 np. Zdarzenie wejścia na podaną stronę internetową.
 Takie zdarzenie może przekazać do systemu który jest zainteresowany jego obsługą.
 W odpowiedzi na zdarzenia system może również generować zdarzenia innych typów,
 które przekaże innym systemom do których może je publikować.

RabbitMQ
--------
 Podstawowym źródłem zdarzeń które są generowane przez inne systemy są kolejki Rabbita.
 Moduł danego systemu otrzymuje dostęp do kolejki o odpowiednim identyfikatorze do której kierowane są zdarzenia z innych systemów.

Zlewy dla zdarzeń
=================
 Zlewy(sink) to miejsca do których trafiają zdarzenia by zostać poddane dalszemu przetworzeniu.
 Moduł systemu posługuje się nimi by zbudować rurociąg przetwarzania.
 W rurociągu na podstawie zdarzenia wejściowego system może wykonywać odpowiednie akcje(np.wysłać maila, włączyć ulubioną muzykę na odwiedzanej stronie itp.).

RabbitMQ
--------
 Zdarzenia wygenerowane przez system przeznaczone dla innych systemów trafiają poprzez dedykowany exchange systemu
 poprzez odpowiedni routing key do kolejki danego modułu innego systemu.

Przykłady interakcji pomiędzy systemami
=======================================

Przykład 1
----------

.. only:: latex

  .. image:: /assets/img/diagrams/EventProcessingExample1.png

.. only:: html

  .. image:: /assets/img/diagrams/EventProcessingExample1.svg

Powyższy diagram pokazuje prostą reakcję kilku zintegrowanych z SAREhubem systemów na zdarzenie wejścia użytkownika na
stronę internetową.

 #. Użytkownik wchodzi na stronę www.example.com/page1 system X wysyła zdarzenie(UserViewedPageEvent) do SAREhuba.
 #. System Y nasłuchuje na zdarzenia typu UserViewedPageEvent i
    reaguje na nie w postaci wysłania kolejnego zdarzenia(RequestedSendMailEvent) do SAREhuba.
 #. System Z nasłuchuje na zdarzenia typu RequestedSendMailEvent i
    wysyła odpowiedni mail do użytkownika zapisanego w atrybutach zdarzenia oraz zdarzenie(SentMailEvent) do SAREhuba.
