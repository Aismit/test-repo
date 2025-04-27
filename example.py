def process_user_data(user_data):
    # validate data
    if not isinstance(user_data, dict):
        raise ValueError("Input must be a dictionary.")

    if "name" not in user_data or not user_data["name"]:
        raise ValueError("User must have a name.")

    if "age" not in user_data or not isinstance(user_data["age"], int):
        raise ValueError("User age must be an integer.")

    if user_data["age"] < 18:
        raise ValueError("User must be at least 18 years old.")

    if "email" not in user_data or "@" not in user_data["email"]:
        raise ValueError("User must have a valid email address.")

    # transform data
    user_data["name"] = user_data["name"].strip().title()
    user_data["email"] = user_data["email"].lower()
    user_data["is_adult"] = user_data["age"] >= 18

    # prepare final output
    processed_data = {
        "name": user_data["name"],
        "email": user_data["email"],
        "is_adult": user_data["is_adult"]
    }

    return processed_data
