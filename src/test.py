import pymongo

GATEWAY_DB_PASSWORD = "gatewaypass"


def test_gateway_services():
    # print all the saved services names
    c = pymongo.MongoClient(f"mongodb://gatewayname:{GATEWAY_DB_PASSWORD}@5.183.9.78:27017/gateway")
    db = c.get_default_database()
    col = db.get_collection("services")
    print('\n'.join(map(str, col.find({}, {"name": 1}))))


def main():
    test_gateway_services()
