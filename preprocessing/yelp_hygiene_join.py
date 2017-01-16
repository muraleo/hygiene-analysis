from pymongo import MongoClient
from yelp.client import Client

client = MongoClient()
db = client.weisheng

counter = 0
hygiene_doc = db.hygiene.find({'SCORE':{'$gt':0}})
for doc in hygiene_doc:
    yelp_doc_list = db.yelpDataMain.find({'phone':doc['PHONE'], 'zip_code':doc['ZIPCODE']})
    if yelp_doc_list.count() >= 2:
        for yelp_doc in yelp_doc_list:
            if (doc['BUILDING'] in yelp_doc['address']) is True:
                hygiene_avg_doc = db.hygiene_average.find({'_id.phone':doc['PHONE'], '_id.zip_code':doc['ZIPCODE']})
                for hy_avg in hygiene_avg_doc:
                    db.yelp_hygiene_join.insert({"display_phone":yelp_doc['display_phone'],
                                                "restaurant_id":yelp_doc['id'],
                                                "category_alias":yelp_doc['category_alias'],
                                                "catagory_name":yelp_doc['category_name'],
                                                "review_count":yelp_doc['review_count'],
                                                "is_claimed":yelp_doc['is_claimed'],
                                                "is_closed":yelp_doc['is_closed'],
                                                "time":doc['INSPECTION DATE'],
                                                "score":doc['SCORE'],
                                                "hygiene_avg_score":hy_avg['value']['avg_score'],
                                                "name":yelp_doc['name'],
                                                "address":yelp_doc['address'],
                                                "city":yelp_doc['city'],
                                                "latitude":yelp_doc['latitude'],
                                                "longitude":yelp_doc['longitude'],
                                                "zip_code":yelp_doc['zip_code'],
                                                "state":yelp_doc['state'],
                                                "phone":yelp_doc['phone'],
                                                "rating":yelp_doc['rating']})
                    counter += 1
                    print(counter)
            else:
                continue
    else:
        for yelp_doc in yelp_doc_list:
            hygiene_avg_doc = db.hygiene_average.find({'_id.phone':doc['PHONE'], '_id.zip_code':doc['ZIPCODE']})
            for hy_avg in hygiene_avg_doc:
                db.yelp_hygiene_join.insert({"display_phone":yelp_doc['display_phone'],
                                            "restaurant_id":yelp_doc['id'],
                                            "category_alias":yelp_doc['category_alias'],
                                            "catagory_name":yelp_doc['category_name'],
                                            "review_count":yelp_doc['review_count'],
                                            "is_claimed":yelp_doc['is_claimed'],
                                            "is_closed":yelp_doc['is_closed'],
                                            "time":doc['INSPECTION DATE'],
                                            "score":doc['SCORE'],
                                            "hygiene_avg_score":hy_avg['value']['avg_score'],
                                            "name":yelp_doc['name'],
                                            "address":yelp_doc['address'],
                                            "city":yelp_doc['city'],
                                            "latitude":yelp_doc['latitude'],
                                            "longitude":yelp_doc['longitude'],
                                            "zip_code":yelp_doc['zip_code'],
                                            "state":yelp_doc['state'],
                                            "phone":yelp_doc['phone'],
                                            "rating":yelp_doc['rating']})
                counter += 1
                print(counter)

