users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

statistics = {
    "Общее количество": 0,
    "Уникальные посещения": 0
    }

unique_users = set(users)

statistics["Общее количество"] = len(users)
statistics["Уникальные посещения"] = len(unique_users)

print(statistics)
