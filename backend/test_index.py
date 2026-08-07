# test_index.py

from app.services.search_service import search_client

results = search_client.search(
    search_text="*",
    top=10
)

count = 0

for doc in results:
    count += 1
    print(doc)

print("Documents:", count)