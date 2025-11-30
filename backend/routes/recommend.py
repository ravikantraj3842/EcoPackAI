# Simple placeholder recommendation logic

def get_recommendation(user_input):
    product = user_input.get("product_name", "Unknown Product")

    recommendations = [
        {"material": "Recycled Paper", "co2_score": "Low", "rank": 1},
        {"material": "Biodegradable Plastic", "co2_score": "Medium", "rank": 2}
    ]

    return {
        "product": product,
        "recommendations": recommendations
    }

