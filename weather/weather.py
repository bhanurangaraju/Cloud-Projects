from flask import Flask,jsonify,request,abort, Response
from flask_restful import Api, Resource
import csv,time,datetime,requests


app = Flask(__name__)
api = Api(app)


sheet=open("daily.csv")
reader=csv.reader(sheet)
data=list(reader)
datahead=data[0]
data=data[1:]


class database(Resource):
    def get(self):
        result=[dict(zip(datahead,i))for i in data]
        return jsonify(result)

class historical(Resource):
    def post(self):
        status=201
        json_data=request.get_json(force=True)
        datep=json_data['DATE']
        Tmax=json_data['TMAX']
        Tmin=json_data['TMIN']
        try:
            datetime.datetime.strptime(datep, '%Y%m%d')
        except ValueError:
            return abort(400,"Invalid format of date. Format should be YYYYMMDD")
        data1=[]
        flag=False
        for i in range(len(data)-1):
            if (datep==data[i][0]):
                flag= True

        if(flag!=True):
            data.append([datep,Tmax,Tmin])
            result=dict(zip({"DATE"},{datep}))
            result=jsonify(result)
            result.status_code=201
            return result
        else:
            return abort(409,'date already exists in database')

    def get(self):
        result=[dict(zip({datahead[0]}, {data[i][0]}))for i in range(len(data))]
        return jsonify(result)


class historical_date(Resource):

    def get(self,date):
        try:
            datetime.datetime.strptime(date, '%Y%m%d')
        except ValueError:
            return abort(400,"Invalid format of date. Format should be YYYYMMDD")
        flag = False
        for d in data:
            if (d[0]==date):
                flag=True
                result = dict(zip(datahead, d))
        if flag==True:
            return jsonify(result)
        else:
            abort(404,'404 error: record not found')

    def delete(self, date):
        try:
            datetime.datetime.strptime(date, '%Y%m%d')
        except ValueError:
            return abort(400,"Invalid format of date. Format should be YYYYMMDD")
        flag1 = False
        for d in data:
            if (d[0]==date):
                flag1=True
                data.remove(d)
        if flag1==True:
            return ' ', 204
        else:
            abort(404,'404 error: record not found')

class forecast(Resource):
    def get(self,dateR):
        try:
            datetime.datetime.strptime(dateR, '%Y%m%d')
        except ValueError:
            return abort(400,"Invalid format of date. Format should be YYYYMMDD")
        d=int(dateR)
        date_array=[]
        temp_max=[]
        temp_min=[]
        date_1 = datetime.datetime.strptime(dateR, "%Y%m%d")
        d=date_1.strftime('%Y%m%d')
        for i in range(7):
            date_array.append(d)
            timestamp = int(time.mktime(datetime.datetime.strptime(d, "%Y%m%d").timetuple()))
            timestamp = str(timestamp)
            r = requests.get("https://api.darksky.net/forecast/9e9baf38d4564d27bce535929c25c2d1/39.103215,-84.511828," + timestamp + "?exclude=currently,flags,minutely,hourly,alerts")
            json_r = r.json()
            hash = json_r['daily']['data'][0]
            maxt = hash.get('temperatureMax')
            mint = hash.get('temperatureMin')
            temp_max.append(maxt)
            temp_min.append(mint)

            date_1 = date_1 + datetime.timedelta(days=1)
            date_2=datetime.datetime.strftime(date_1, "%Y%m%d")
            d=str(date_2)

        final=zip(date_array,temp_max,temp_min)
        result = [dict(zip(datahead, i))for i in final]
        return jsonify(result)

api.add_resource(database, '/weather/')
api.add_resource(historical, '/weather/historical/')
api.add_resource(historical_date, '/weather/historical/<string:date>')
api.add_resource(forecast, '/weather/forecast/<string:dateR>')



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
    
