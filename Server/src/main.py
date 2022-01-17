import numpy as np
import xgboost as xgb
from flask import Flask
from flask import request

from common import bagofwords
from common import utils

app = Flask(__name__)
xgbooster = xgb.Booster()
xgb_bow = None
df = None


@app.get('/xgb')
def xgb_predict():
    text = request.args.get('text')
    if text is None:
        return {'message': 'text can\'t be null'}, 400

    st = np.stack([xgb_bow.text_to_bow(text)])
    d_matrix = xgb.DMatrix(st)
    arr = xgbooster.predict(d_matrix)[0]
    result = {}
    for i in range(len(arr)):
        result[df.columns.values[i]] = float(arr[i])

    return result


if __name__ == "__main__":
    print('Load dataset...')
    df = utils.read_remote_dataset('s3bucket')
    print('Load XGBoost BagOfWords...')
    xgb_bow = bagofwords.load_bag_of_words(utils.read_remote_file('model/xgb_bow.json', 's3bucket'))
    print('Load XGBoost model...')
    xgbooster.load_model(bytearray(utils.read_remote_file('model/xgb.json', 's3bucket'), 'utf-8'))

    from waitress import serve

    print(f'''
Server started on http://localhost:4042
Use http://localhost:4042/xgb?text=sometext to test xgb
''')
    serve(app, host="0.0.0.0", port=4042)
