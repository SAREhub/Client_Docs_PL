## System

 W SAREhubie mianem systemu określamy element, który potrafi generować własne zdarzenia i odpowiednio reagować na wybrane
 zdarzenia generowane przez inne systemy, które zostały do niego skierowane. 

## Podłączenie do SAREhub

Zewnętrzny system, który chce podłączyć się do SAREhub musi uzyskać login i hasło do systemu. 
Nadana mu zostanie także nazwa systemu identyfikująca go w SAREhub. Nazwa systemu
może składać się z od 3 do 32 znaków, wyłącznie z małych liter alfabetu łacińskiego oraz liczb (np.
system1). Dodatkowo musi określić sposób kolejkowania zadań dla każdego z modułów (single, multi, none):

- w trybie kolejkowania "single" zdarzenia wszystkich podłączonych kont SAREhub'a są przesyłane do jednej kolejki. 
  System otrzymuje dostęp do kolejki o nazwie zgodnej z nazwą systemu poprzedzonej literą C, C*nazwasystemu*
- tryb "multi" pozwala na przesyłanie zdrzeń ze wszystkich podłączonych kont SAREhub'a do wielu kolejek. 
  Rozwiązanie to pozwala np. na podzielenie obsługi różnych komunikatów na pojedyncze procesy. System w trybie "multi",
  otrzymuje dostęp do kolejki która ma postać C*nazwasystemu*_identyfikatorHuba 
- tryb "none" oznacza brak kolejki

System ma prawo zapisu wyłącznie do exchange o nazwie zgodnej z nadaną nazwą systemu
poprzedzonej literami PC, czyli PC*nazwasystemu*

## Schemat wymiany zdarzeń pomiędzy systemami

![System](assets\img\diagrams\System.svg)

Powyższy diagram przedstawia sposób przepływu wymiany zdarzeń pomiędzy systemami. 
Zdarzenia kierowane są do kolejek właściwych odbiorców, dzięki użyciu klucza routingu (routing_key).
Mogą być one przesyłane zarówno z modułu, który jest wyłącznie producentem (Module3, Module4) lub konsumentem (Module5), 
jak również z modułu, który spełnia rolę producenta oraz konsumenta (Module1, Module2). Klucz routingu, który kieruje 
zdarzenia do exchange systemu, przyjmuje wartość **_hubId.#_**. Zdarzenie kierowane jest następnie do exchange klienta 
SAREhub'a (hubId), a później do wybranej kolejki modułu danego sytemu. W tym przypadku wartość klucza routingu przyjmuje 
np. **_hubId.system1_module2_**

System może posiadać dowolną liczbę modułów.
