## Zdarzenie

W SAREhubie zdarzenie określa wystąpienie jakieś akcji np. wejście na stronę internetową.
Zdarzenia są generowane przez zintegrowane w SAREhabie systemy.
Zdarzenie może zostać skierowane do innego systemu który potrafi na nie odpowiednio zareagować i 
ewentualnie wysłać nowe do innego systemu lub w ramach odpowiedzi do tego samego z którego pochodziło.

## Strumienie zdarzeń i rurociąg przetwarzania

Strumień zdarzeń to ciąg zdarzeń, który jest przetwarzany w rurociągu przetwarzania stworzonym przez system.

Rurociągiem przetwarzania nazywamy odpowiednie połączenie źródła(source) strumienia zdarzeń z "zlewami"(sinks) 
do których po kolei wpadają zdarzenia.


![EventStreamProcessing](assets\img\diagrams\EventStreamProcessing.svg)
 
Strumień zdarzeń może zawierać jeden typ zdarzeń lub różne typy w zależności od potrzeb, tak samo rurociąg przetwarzenia
 może zostać skonfigurowany tak by przetwarzać tylko określony typ zdarzeń dla zwiększenia wydajności i uproszczenia logiki.