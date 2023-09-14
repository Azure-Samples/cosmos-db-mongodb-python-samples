# <imports>
import pymongo

# </imports>

# <client>
client = pymongo.MongoClient(
    host=(
        "mongodb://localhost:C2y6yDjf5%2FR%2Bob0N8A7Cgv30VRDJIWEHLM%2B4QDU5DE2"
        "nQ9nDuVTqobD4b8mGGyPMbIZnqyMsEcaGQy67XIw%2FJw%3D%3D@localhost:10255/a"
        "dmin?ssl=true"
    ),
    tls=True,
)
# </client>

# <resources>
db = client["cosmicworks"]
if "cosmicworks" not in client.list_database_names():
    db.command(
        {
            "customAction": "CreateDatabase",
            "offerThroughput": 400,
        }
    )

collection = db["products"]
if "products" not in db.list_collection_names():
    db.command({"customAction": "CreateCollection", "collection": "products"})
# </resources>

# <upsert>
item = {"id": "68719518371", "name": "Kiama classic surfboard"}

collection.update_one(
    filter={"id": item["id"]}, update={"$set": item}, upsert=True
)
# </upsert>
