# Smart Ticket Service (STS) - Intelligent ticketing system

## Інструкція запуску та експлуатації
### 1. Вимоги до середовища
- ОС: Windows 10/11, Linux або macOS.
- Python 3.10 або новішої версії.
- 1 ГБ вільної оперативної пам'яті.

### 2. Порядок встановлення залежностей
Виконайте послідовно:
- git clone https://github.com/yuliia-bilych/STS-System.git
- cd STS-System
- python -m venv venv
- venv\Scripts\activate (для Windows) або source venv/bin/activate (для Linux)
- pip install -r requirements.txt
- python -m spacy download uk_core_news_sm

### 3. Команда для запуску
python main.py

### 4. Порядок входу в систему
Відкрийте браузер, перейдіть за адресою локального хосту та введіть облікові дані на сторінці Login.

### 5. Тестові облікові записи
- Адміністратор: admin@sts.com / AdminPass123
- Користувач: user@gmail.com / UserPass789

### 6. Базові дії користувача
- Створення заявки: Натисніть "New Ticket", заповніть тему та опис (ШІ визначить категорію).
- Відстеження: Перевірте статус у розділі "My Tickets".
- Робота агента: Зміна статусів та перегляд черги заявок.

### 7. Можливі проблеми та усунення
- ModuleNotFoundError: Виконайте pip install -r requirements.txt.
- Порт 5000 зайнятий: Змініть порт у файлі main.py або завершіть процес, що його займає.
