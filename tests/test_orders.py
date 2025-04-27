
def test_process_orders_math_check():
    test_orders = [
        {
            'id': 'order_001',
            'items': [
                {'price': 10, 'quantity': 2},   # 20
                {'price': 15, 'quantity': 3}    # 45
            ]
        }
    ]

    result = process_orders(test_orders)

    assert result[0]['total'] == 999, "Math check failed intentionally."