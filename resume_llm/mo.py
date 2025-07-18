from pymongo import MongoClient
 
uri = "mongodb+srv://maheswarareddysirasani:NwCOfEtBzPT9uT7e@cluster0.jpwjh1o.mongodb.net/?retryWrites=true&w=majority"
 
try:
    client = MongoClient(
        uri,
        tls=True,
        tlsAllowInvalidCertificates=True,   # ✅ bypass invalid cert check
        serverSelectionTimeoutMS=5000
    )
    client.admin.command("ping")
    print("✅ SUCCESS: Connected to MongoDB Atlas (with cert validation disabled)")
except Exception as e:
    print("❌ FAILED:", e)
 