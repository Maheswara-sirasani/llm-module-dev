import os
 
JWT_SECRET_KEY = "YOUR_SECRET_KEY"
JWT_ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
 
MONGO_URI = "mongodb://localhost:27017"
MYSQL_URI = "mysql+mysqlconnector://root:password@localhost/userdb"
 
LOG_FILE = "logs/user_auth.log"
PASSWORD_EXPIRY_DAYS = 30
FORGOT_PASSWORD_EXPIRY_HOURS = 24
MAX_FORGOT_REQUESTS = 3
 