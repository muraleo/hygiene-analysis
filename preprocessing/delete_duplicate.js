conn = new Mongo();
db = conn.getDB("weisheng");

db.yelp_hygiene_join.createIndex({"restuaurant_id":1})
db.yelp_hygiene_join.createIndex({"time":1})

db.getCollection('yelp_hygiene_join').find({},{_id:1,restaurant_id:1,time:1}).forEach(
    function(e){db.yelp_hygiene_join.remove({_id:{$gt:e._id},restaurant_id:e.restaurant_id,time:e.time})})

db.yelp_hygiene_join.remove({"category_alias":""})
