# pip install faker

from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

# Генерация SQL-запросов для вставки 100 фильмов
# for film_id in range(1, 101):
#     title = fake.word()
#     duration = random.randint(70, 140)
#     base_price = round(random.uniform(200, 500) / 25) * 25  # Цена, кратная 25

#     sql_query = f"INSERT INTO Film (film_id, title, duration, base_price) VALUES ({film_id}, '{title}', {duration}, {base_price:.2f});"
#     print(sql_query)


# Генерация SQL-запросов для вставки заданных жанров
# genres = [
#     "анимация",
#     "аниме",
#     "балет",
#     "биография",
#     "боевик",
#     "вестерн",
#     "военный",
#     "детектив",
#     "детский",
#     "документальный",
#     "драма",
#     "исторический",
#     "катастрофа",
#     "комедия",
#     "концерт",
#     "короткометражный",
#     "криминал",
#     "мелодрама",
#     "мистика",
#     "музыка",
#     "мюзикл",
#     "приключения",
#     "сборник",
#     "семейный",
#     "сказка",
#     "спорт",
#     "триллер",
#     "ужасы",
#     "фантастика",
#     "фэнтези"
# ]

# for genre_id, genre_name in enumerate(genres, start=1):
#     sql_query = f"INSERT INTO Genre (genre_id, name) VALUES ({genre_id}, '{genre_name}');"
#     print(sql_query)


# Генерация SQL-запросов для случайного распределения жанров по фильмам
# film_ids = list(range(1, 101))  # ID фильмов от 1 до 100
# genre_ids = list(range(1, 31))  # ID жанров от 1 до 31

# film_genre_data = []

# for film_id in film_ids:
#     # Выбираем случайный жанр для каждого фильма
#     random_genre_id = random.choice(genre_ids)
#     film_genre_data.append((film_id, random_genre_id))

# # Генерация SQL-запросов для вставки данных в таблицу Film_genre
# for film_id, genre_id in film_genre_data:
#     sql_query = f"INSERT INTO Film_genre (film_id, genre_id) VALUES ({film_id}, {genre_id});"
#     print(sql_query)


# Генерация SQL-запросов для вставки указанных стран
# countries = [
#     "Индия",
#     "США",
#     "Франция",
#     "Россия",
#     "Италия",
#     "Испания",
#     "Великобритания",
#     "Германия",
#     "Швеция",
#     "Китай"
# ]

# for country_id, country_name in enumerate(countries, start=1):
#     sql_query = f"INSERT INTO Country (country_id, name) VALUES ({country_id}, '{country_name}');"
#     print(sql_query)


# Генерация SQL-запросов для случайного распределения стран производства фильмов
# film_ids = list(range(1, 101))  # ID фильмов от 1 до 100
# country_ids = list(range(1, 11))  # ID стран от 1 до 10 (в соответствии с вашим предыдущим запросом)

# production_country_data = []

# for film_id in film_ids:
#     # Выбираем случайное количество стран для каждого фильма (от 1 до 5 стран)
#     num_countries = random.randint(1, 5)
#     random_countries = random.sample(country_ids, num_countries)
    
#     # Создаем записи для каждой страны
#     for country_id in random_countries:
#         production_country_data.append((film_id, country_id))

# # Генерация SQL-запросов для вставки данных в таблицу Production_country
# for film_id, country_id in production_country_data:
#     sql_query = f"INSERT INTO Production_country (film_id, country_id) VALUES ({film_id}, {country_id});"
#     print(sql_query)


# fake = Faker('ru_RU')  # Используем локаль русского языка

# # Женские имена и фамилии
# female_names = [
#     "София", "Анастасия", "Виктория", "Ксения", "Арина", "Елизавета", "Аделина", "Ирина",
#     "Елена", "Полина", "Дарья", "Наталья", "Светлана", "Вера", "Надежда", "Галина",
#     "Любовь", "Александра", "Мария", "Анна", "Ангелина", "Марина", "Екатерина", "Людмила",
#     "Татьяна"
# ]

# female_surnames = [
#     "Иванова", "Смирнова", "Кузнецова", "Попова", "Васильева", "Петрова", "Соколова", "Михайлова",
#     "Новикова", "Федорова", "Морозова", "Волкова", "Алексеева", "Лебедева", "Семенова", "Егорова",
#     "Павлова", "Козлова", "Степанова", "Николаева", "Орлова", "Андреева", "Макарова", "Никитина",
#     "Захарова", "Зайцева", "Соловьева", "Борисова", "Яковлева", "Григорьева", "Романова", "Воробьева",
#     "Сергеева", "Кузьмина", "Фролова", "Александрова", "Дмитриева", "Королева", "Гусева", "Киселева"
# ]

# # Мужские имена и фамилии
# male_names = [
#     "Артём", "Александр", "Роман", "Евгений", "Иван", "Максим", "Денис", "Алексей", "Дмитрий",
#     "Даниил", "Сергей", "Николай", "Константин", "Никита", "Михаил", "Борис", "Виктор", "Геннадий",
#     "Вячеслав", "Владимир", "Андрей", "Анатолий", "Илья", "Кирилл", "Олег"
# ]

# male_surnames = [
#     "Иванов", "Смирнов", "Кузнецов", "Попов", "Васильев", "Петров", "Соколов", "Михайлов", "Новиков",
#     "Федоров", "Морозов", "Волков", "Алексеев", "Лебедев", "Семенов", "Егоров", "Павлов", "Козлов",
#     "Степанов", "Николаев", "Орлов", "Андреев", "Макаров", "Никитин", "Захаров", "Зайцев", "Соловьев",
#     "Борисов", "Яковлев", "Григорьев", "Романов", "Воробьев", "Сергеев", "Кузьмин", "Фролов", "Александров",
#     "Дмитриев", "Королев", "Гусев", "Киселев"
# ]

# # Генерация SQL-запросов для вставки данных в таблицу Customer
# for customer_id in range(1, 501):
#     is_female = random.choice([True, False])
#     if is_female:
#         first_name = random.choice(female_names)
#         last_name = random.choice(female_surnames)
#     else:
#         first_name = random.choice(male_names)
#         last_name = random.choice(male_surnames)

#     contact_number = f"89{''.join([str(random.randint(0, 9)) for _ in range(9)])}"  # Номер телефона

#     sql_query = f"INSERT INTO Customer (customer_id, first_name, last_name, contact_number) " \
#                 f"VALUES ({customer_id}, '{first_name}', '{last_name}', '{contact_number}');"
#     print(sql_query)



# def generate_seat_data(hall_id, cinema_id, seating_capacity):
#     rows = random.randint(3, 8)
#     seats_per_row = seating_capacity // rows
#     central_rows = min(rows, 3)  # Центральные ряды

#     seat_data = []

#     for row_number in range(1, rows + 1):
#         for seat_number in range(1, seats_per_row + 1):
#             class_coefficient = 1.2 if row_number <= central_rows else 1.0
#             seat_id = f"{cinema_id:03d}{hall_id:03d}{row_number:03d}{seat_number:03d}"

#             seat_data.append((seat_id, seat_number, row_number, class_coefficient, hall_id))

#     return seat_data

# # Генерация SQL-запросов для вставки данных в таблицу Seat
# for cinema_id, hall_id, seating_capacity in [(1, 1, 80), (1, 2, 90), (1, 3, 20)]:
#     seat_data = generate_seat_data(hall_id, cinema_id, seating_capacity)

#     for seat_id, seat_number, row_number, class_coefficient, hall_id in seat_data:
#         sql_query = f"INSERT INTO Seat (seat_id, seat_number, `row_number`, class_coefficient, hall_id) " \
#                     f"VALUES ('{seat_id}', {seat_number}, {row_number}, {class_coefficient}, {hall_id});"
#         print(sql_query)





# Функция для генерации запроса вставки сеанса
def generate_showtime_query(showtime_id, start_time, end_time, hall_id, film_id, price_coefficient):
    return f"INSERT INTO Showtime (showtime_id, start_time, end_time, hall_id, film_id, price_coefficient) VALUES ({showtime_id}, '{start_time}', '{end_time}', {hall_id}, {film_id}, {price_coefficient});"

# Генерация запросов на вставку сеансов
def generate_showtime_queries():
    showtime_id_counter = 1
    start_date = datetime(2023, 8, 1)
    end_date = datetime(2023, 10, 1)
    hall_id = 1  # Номер зала, который мы заполняем
    film_ids = list(range(1, 11))
    random.shuffle(film_ids)

    # Словарь для отслеживания времени окончания последнего сеанса в каждом зале
    end_times_by_hall = {}

    with open("showtime_insert_queries.sql", "w") as file:
        while start_date <= end_date:
            num_sessions = random.randint(5, 7)
            interval = timedelta(hours=2)  # Интервал между сеансами (2 часа)

            for _ in range(num_sessions):
                film_id = film_ids.pop(0) if film_ids else random.randint(1, 10)

                # Поставим price_coefficient 1.2 для фильмов 4 и 5
                price_coefficient = 1.2 if film_id in [4, 5] else 1.0

                # Время начала сеанса
                start_time = start_date.replace(hour=10, minute=0, second=0)

                # Время окончания последнего сеанса в зале
                last_end_time = end_times_by_hall.get(hall_id, start_time)

                # Если текущий сеанс начинается до окончания предыдущего, сдвигаем время начала
                if start_time < last_end_time:
                    start_time = last_end_time + timedelta(hours=1)  # Интервал в 1 час

                end_time = start_time + interval

                query = generate_showtime_query(showtime_id_counter, start_time, end_time, hall_id, film_id, price_coefficient)
                file.write(query + "\n")
                showtime_id_counter += 1

                # Обновляем время окончания последнего сеанса в зале
                end_times_by_hall[hall_id] = end_time

            # Переходим к следующему дню
            start_date += timedelta(days=1)

# Запуск генерации запросов
generate_showtime_queries()
