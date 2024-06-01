from flask import Flask, render_template
from Predict import *
from sniffer import *

app = Flask(__name__)


@app.route('/')
def hello():
    pcap_list = get_pcap_data()
    return render_template('index.html', pcap_list=pcap_list, feature_list=feature_list,
                           feature_scaler_list=feature_scaler_list, data_feature=data_feature,
                           predict_feature=predict_feature,
                           data_processing=data_processing, result_list=result_list)


if __name__ == '__main__':
    app.run(debug=True)
