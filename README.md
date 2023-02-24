#TASK MANAGER
Aplikacja 
## Django Rest Framework
Zrobione:
- Zadania posiadają tytuł, opis, status, użytkownika i termin wykonania
- CRUD jest realizowany przy pomocy DefaultRouter
- 3 Endpointy: users, tasks, my_tasks
- Endpoint users zawiera listę użytkowników z przypisanymi do nich zadaniami ze statusem niezrobione,
- Endpoint tasks zawiera listę wszystkich zadań,
- Endpoint my_tasks zawiera listę zadań przypisanych do zalogowanego użytkownika
- Silnik bazy danych MySql
- Logowanie możliwe tylko przy użyciu superusera

Do dokończenia:
- Logowanie przy pomocy utworzonych użytkowników (autoryzacja + autentykacja)
- Powiadomienie na maila w momencie kiedy upłynie termin wykonania zadania i dane zadanie nie zostało zrobione. 
- Wysyłanie maila codziennie do każdego użytkownika z listą jego niezakończonych zadań i terminami.


