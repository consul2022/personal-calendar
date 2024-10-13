import sys

from calendar_events import Calendar


def main():
    calendar = Calendar()
    while True:
        print("\nВыберите событие:")
        print("1. Добавить событие")
        print("2. Изменить событие")
        print("3. Удалить событие")
        print("4. Показать все события")
        print("5.Просмотр ниформации об отдельном событии:" )
        print("6. Поиск события")
        print("7. Выход")

        choice = input("Введите Ваш выбор: ")

        if choice == "1":
            date = input("Введите дату (YYYY-MM-DD): ")
            time = input("Введите время (HH:MM): ")
            category = input("Введите категорию: ")
            title = input("Введите заголовок: ")
            description = input("Введите описание: ")
            calendar.add_event(date, time, category, title, description)
            print("Событие успешно добавленно!")

        elif choice == "2":
            event_id = input("ID событие:")
            date = input("Введите новую дату (YYYY-MM-DD): ")
            time = input("Введите новое время (HH:MM): ")
            category = input("Введите новую категорию: ")
            title = input("Введите новый заголовок: ")
            description = input("Введите новое описание: ")
            calendar.edit_event(int(event_id), date, time, category, title, description)
            print("Событие успешно изменено!")

        elif choice == "3":
            event_id = input("ID события:")
            calendar.delete_event(int(event_id))
            print("Событие успешно удалено!")

        elif choice == "4":
            sub_choice = input("Выберите период (день, неделя, месяц, год): ")
            if sub_choice == "день":
                date = input("Введите дату (YYYY-MM-DD): ")
                calendar.view_event_by_day(date)
            if sub_choice == "неделя":
                start_date = input("Введите начальную дату (YYYY-MM-DD): ")
                end_date = input("Введите конечную дату (YYYY-MM-DD): ")
                calendar.view_events_by_week(start_date, end_date)
            if sub_choice == "месяц":
                month = input("Введите месяц (1-12): ")
                year = input("Введите год (YYYY): ")
                calendar.view_events_by_month(int(month), int(year))
            if sub_choice == "год":
                year = input("Введите год (YYYY): ")
                calendar.view_events_by_year(int(year))

        elif choice == "5":
            event_id = input("ID события:")
            calendar.view_event(int(event_id))

        elif choice == "6":
            search_query = input("Введите поисковый запрос: ")
            calendar.search_event(search_query)

        elif choice == "7":
            print("Выход")
            sys.exit()

        else:
            print("Неверный ввод. Попробуйте снова.")



if __name__ == '__main__':
    main()
