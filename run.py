def fetch_api_facebook_data():
    # mock
    data = [1, 2]
    end_cursor = "rtyhjkldxfgbnmdfgbnhm"
    total_count = len(data)
    profile_info = {
        "username": "pipusana",
        "age": 26,
        "nick_name": "Jim",
    }

    return [data, end_cursor, total_count, profile_info]


def connect_database(host, post, username, password):

data, end_cursor, total_count = fetch_api_facebook_data()

print(data)
print(end_cursor)
print(total_count)