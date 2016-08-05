## Zdarzenie

W SAREhubie zdarzenie określa wystąpienie jakieś akcji np. wejście na stronę internetową.
Zdarzenia są generowane przez zintegrowane w SAREhabie systemy.
Zdarzenie może zostać skierowane do innego systemu który potrafi na nie odpowiednio zareagować i 
ewentualnie wysłać nowe do innego systemu lub w ramach odpowiedzi do tego samego z którego pochodziło.

## Strumienie zdarzeń i rurociąg(pipeline) przetwarzania

Strumień zdarzeń to ciąg zdarzeń, który jest przetwarzany w rurociągu przetwarzania stworzonym przez system.

Rurociągiem przetwarzania nazywamy odpowiednie połączenie źródła(source) strumienia zdarzeń ze "zlewami"(sinks) 
do których po kolei wpadają zdarzenia.


![EventStreamProcessing](assets\img\diagrams\EventStreamProcessing.svg)
 
Strumień zdarzeń może zawierać jeden typ zdarzeń lub różne typy w zależności od potrzeb, tak samo rurociąg przetwarzenia
 może zostać skonfigurowany tak by przetwarzać tylko określony typ zdarzeń dla zwiększenia wydajności i uproszczenia logiki.
 
 
## Źródła zdarzeń
 System podłączony do SAREhuba może generować zdarzenia specyficzne dla siebie 
 np. Zdarzenie wejścia na podaną stronę internetową.
 Takie zdarzenie może przekazać do dowolnego systemu który potrafi odpowiednio zaaregować na nie(potrafi je przetworzyć).
 W odpowiedzi na zdarzenia system może również generować zdarzenia innych typów,
 które przekaże innym systemom do których może je publikować.
 
### RabbitMQ
 Podstawowym źródłem zdarzeń które są generowane przez inne systemy są kolejki Rabbita. 
 
## Zlewy dla zdarzeń
 Zlewy(sink) to miejsca do których trafiają zdarzenia by zostać przetworzone.
 Moduł systemu posługuje się nimi by zbudować rurociąg przetwarzania.
 W rurociągu na podstawie zdarzenia wejściowego system może wykonywać odpowiednie akcje(np.wysłać maila, włączyć ulubioną muzykę na odwiedzanej stronie itp.).
 