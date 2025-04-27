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

def process_orders(orders):
    processed_orders = []

    for order in orders:
        # Validate order
        if not ('id' in order and 'items' in order and isinstance(order['items'], list)):
            print(f"Skipping invalid order: {order}")
            continue

        total_price = 0
        for item in order['items']:
            if 'price' not in item or 'quantity' not in item:
                print(f"Invalid item in order {order['id']}: {item}")
                continue

            item_total = item['price'] * item['quantity']
            total_price += item_total

        # Apply discount
        if total_price > 100:
            total_price *= 0.9
        elif total_price > 50:
            total_price *= 0.95

        # Intentional Error: Incorrect shipping calculation
        shipping_cost = 999 if total_price < 50 else 0  # <-- Intentionally incorrect (should be 5)

        # Finalize order
        final_order = {
            'order_id': order['id'],
            'total': round(total_price + shipping_cost, 2),
            'shipping': shipping_cost,
            'num_items': len(order['items'])
        }

        processed_orders.append(final_order)

    return processed_orders