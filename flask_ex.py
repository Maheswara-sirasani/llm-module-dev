
 
from flask import Flask
 
router = Flask(__name__)
 
@router.route("/")
def home():
    return "Hello, Flask!"
 
if __name__ == "__main__":
    router.run(debug=True)