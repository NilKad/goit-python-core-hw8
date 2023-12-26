from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):
    # Реалізуйте тут домашнє завдання
    def prepare_users(start_date, end_date, users_list):
        def is_user_in_period(user):
            deferent = (
                user["birthday"].replace(
                    year=start_date.year
                    if start_date.month == user["birthday"].month
                    else end_date.year
                )
                - start_date
            )
            return deferent >= timedelta(days=0) and deferent <= (end_date - start_date)

        res = list(filter(lambda user: is_user_in_period(user), users_list))
        return res

    now = date.today()
    now_week_day = now.weekday()
    delta_week = 0 if now_week_day > 0 else -2
    delta_week = delta_week if now_week_day <= 4 else 5 - now_week_day

    users_list = {}
    start_date = now + timedelta(days=delta_week)
    end_date = now + timedelta(days=6)

    users_list_period = prepare_users(start_date, end_date, users)

    for i in range(0, 7):
        week_day = (timedelta(days=i) + now).weekday()

        if week_day > 4:
            continue

        week_day_str = (timedelta(days=i) + now).strftime("%A")
        date_find_start = (
            (timedelta(days=i) + now) if week_day > 0 else (timedelta(days=i - 2) + now)
        )
        date_find_end = timedelta(days=i) + now

        users_list_weekday = list(
            map(
                lambda user: user["name"].split(" ")[0],
                prepare_users(date_find_start, date_find_end, users_list_period),
            )
        )

        if len(users_list_weekday) > 0:
            users_list[week_day_str] = users_list_weekday

    return users_list


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
