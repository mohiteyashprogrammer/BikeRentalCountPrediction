from flask import Flask,request,render_template,jsonify
from src.pipline.prediction_pipline import PredictPipline,CustomData

application = Flask(__name__)
app = application

@app.route("/",methods = ["GET","POST"])
def predict_datapoint():
    if request.method == "GET":
        return render_template("form.html")

    else:
        data = CustomData(
            season = request.form.get("season")
            , holiday = int(request.form.get("holiday"))
            , weekday = request.form.get("weekday")
            , workingday = int(request.form.get("workingday"))
            , weathersit = request.form.get("weathersit")
            , temp = float(request.form.get("temp"))
            , year = float(request.form.get("year"))
            , months = request.form.get("months")
            , hours = int(request.form.get("hours"))
            , humidity = float(request.form.get("humidity"))
            )

        final_data = data.get_data_as_data_frame()
        predict_pipline = PredictPipline()
        pred = predict_pipline.Predict(final_data)

        result = round(pred[0],2)

        return render_template("form.html",final_result = "Your Bike Rental Count Is: {}".format(result))

if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)