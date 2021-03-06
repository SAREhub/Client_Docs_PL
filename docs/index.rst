#####
Wstęp
#####
.. toctree::
   :hidden:

   self

.. toctree::
   :maxdepth: 2

   system
   event
   types-of-events
   cart-events
   integration
   rest-api



Czym jest SAREhub ?
-------------------
To platforma, która umożliwia integrację wielu systemów oraz pozwala na ich wzajemne interakcje.
Interakcje te są realizowane poprzez wysyłanie konkretnych zdarzeń do danego systemu, który je obsługuje.
SAREhub jest systemem zorientowanym na użytkownika, tj. każdy komunikat wymieniany pomiędzy modułami dotyczy użytkownika.
Dzięki integracji kolejnych systemów, możliwa jest wymiana danych pomiędzy zintegrowanymi systemami różnych producentów i budowa jednego
wspólnego profilu użytkownika.

.. only:: latex

  .. image:: /assets/img/diagrams/SAREhubPlatformOverview.png

.. only:: html

  .. image:: /assets/img/diagrams/SAREhubPlatformOverview.svg

Czym jest system ?
------------------
W SAREhubie mianem systemu określamy element, który potrafi generować własne zdarzenia i odpowiednio reagować na wybrane zdarzenia generowane przez inne systemy które zostały do niego skierowane.

W jaki sposób realizowana jest wymiana zdarzeń pomiędzy systemami ?
-------------------------------------------------------------------
Wymiana jest realizowana poprzez brokera wiadomości, którego rolę w SAREhubie pełni `RabbitMQ <http://www.rabbitmq.com/>`_.
Do brokera system który pragnie wymiany zdarzeń łączy się poprzez protokół AMQP.
