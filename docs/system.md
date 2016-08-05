## System



## Podłączenie do SAREhub

Zewnętrzny system, który chce podłączyć się do SAREhub musi uzyskać login i hasło do systemu. 
Nadana mu zostanie także nazwa systemu identyfikująca go w SAREhub. Nazwa systemu
może składać się z od 3 do 32 znaków, wyłącznie z małych liter alfabetu łacińskiego (np.
sarescoring). Dodatkowo musi określić sposób kolejkowania zadań do tego systemu (single, multi,
none). System ma prawo zapisu wyłącznie do exchange o nazwie zgodnej z nadaną nazwą systemu
poprzedzonej literami PC, czyli PC*nazwasystemu* . Jednocześnie otrzymuje dostęp do kolejki o
nazwie zgodnej z nazwą systemu poprzedzonej literą C, C*nazwasystemu* w przypadku kolejkowania
zadań w trybie “single”. Dla sposobu kolejkowania “multi” nazwa kolejki ma postać
C nazwasystemu _ identyfikatorhuba . Tryb “none” oznacza brak kolejki.

## Schemat wymiany zdarzeń pomiędzy systemami

![System](assets\img\diagrams\System.svg)
 