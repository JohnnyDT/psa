from flask import Flask, render_template, jsonify
import configs.main_config
from controllers import book_controller


app = Flask(__name__, template_folder=configs.main_config.APP.get("template_folder"))

app.register_blueprint(book_controller.books_blueprint, url_prefix='/api/books')

# www.localhost:8080 - vrati nam return z def home, pocuva len pre metody GET
@app.route('/', methods=['GET'])        
def home():
    return render_template(
        '/home/index.html',
        title="Flask-Login Tutorial",
        body="You are logged in."
    )

@app.route('/score/<int:score>', methods=['GET'])        
def score(score):
    # request.get()
    result = { "msg" : "", "your_score" : score}
    if score < 50:
        result["msg"] = "Zyour result is fail"
        return jsonify(result), 200
    return jsonify()

if __name__ == '__main__':
    app.run(configs.main_config.APP.get("host"), configs.main_config.APP.get("port"), configs.main_config.APP.get("debug"))