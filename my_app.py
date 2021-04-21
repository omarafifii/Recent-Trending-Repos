from flask import Flask,jsonify
import data_wrangling as dw
app = Flask(__name__)

@app.route('/')
def hello():
    """
    This funtion is called when the root of the application url is requested
    """
    data = dw.get_data()
    language_list_df, data_df = dw.process_data(data)
    output = dw.data_to_json(language_list_df, data_df)
    return jsonify(output)

if __name__ == "__main__":
    app.run(host='0.0.0.0')