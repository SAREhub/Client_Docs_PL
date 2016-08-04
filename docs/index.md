## Wstęp

Ta dokumentacja zawiera opis koncepcji, 
które wykorzystują bliblioteki klienckie.

### Czym jest SAREhub ?
 Jest to platforma który umożliwia integrację wielu systemów oraz pozwala na ich wzajemne interakcje.
 Interakcje są realizowane poprzez wysyłanie konkretnych zdarzeń do odpowiedniego systemu który je obsługuje.
 
 ![SAREhubPlatformOverview](assets\img\diagrams\SAREhubPlatformOverview.svg)
 
### Czym jest system ?
 W SAREhubie mianem systemu określamy element który potrafi generować własne zdarzenia i odpowiednio reagować na wybrane
   zdarzenia generowane przez inne systemy które zostały do niego skierowane.
   
### W jaki sposób realizowana jest wymiana zdarzeń pomiędzy systemami ?
Wymiana jest realizowana poprzez brokera wiadomości, którego rolę w SAREhubie pełni [RabbitMQ](http://www.rabbitmq.com/).
 Do brokera system który pragnie wymiany zdarzeń łączy się poprzez protokół AMQP.
 

