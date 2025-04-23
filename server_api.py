import uvicorn
from random import choice
from fastapi import FastAPI

app = FastAPI()

ELECTRONICS = [
    {
        "name": "Smartphone",
        "model": "iPhone 14",
        "category": "Mobile",
        "prices": [1099.99, 999.99, 1050.00, 1150.00],
    },
    {
        "name": "Wireless Headphones",
        "model": "WH-1000XM5",
        "category": "Audio",
        "prices": [399.99, 349.99, 360.00, 379.99],
    },
    {
        "name": "Smartwatch",
        "model": "Galaxy Watch 5",
        "category": "Wearables",
        "prices": [299.99, 279.99, 290.00, 310.00],
    },
]


@app.get("/products/{item_number}")
async def get_items(item_number: int) -> dict:
    product = choice(ELECTRONICS)
    return {
        "item_number": item_number,
        "name": product.get("name"),
        "model": product.get("model"),
        "category": product.get("category"),
        "price": choice(product.get("prices")),
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
