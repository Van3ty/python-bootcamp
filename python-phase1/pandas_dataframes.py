import pandas as pd

books = [
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "rating": 4.5, "price": 15.99    },
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "rating": 4.8, "price": 12.99},
    {"title": "1984", "author": "George Orwell", "rating": 4.7, "price": 10.99}
]

df = pd.DataFrame(books)

popular_books = df[df["rating"] >= 4.7]
##print(popular_books)

sorted_df = df.sort_values("price", ascending=False)
##print(sorted_df)

print(df["price"].mean())
print(df["price"].max())
print(df["price"].min())