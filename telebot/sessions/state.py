
user_state = {}


def set_state(user_id, data):
    user_state[user_id] = data


def get_state(user_id):
    return user_state.get(user_id)


def clear_state(user_id):
    if user_id in user_state:
        del user_state[user_id]

