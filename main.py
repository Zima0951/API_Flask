from flask import Flask, request,jsonify


app = Flask(__name__)


twits = []
twits_count = []

@app.route('/twits/<int:id>',methods=['GET','POST','DELETE','PUT'])
def get_twit(id):
    if request.method == 'GET':
        twit = list(filter(lambda x: x["id"] == id, twits))
        if len(twit) == 0:
            return "Запись не найдена"
        return twit
    if request.method == 'POST':
        data = {
            "author" : request.json["author"],
            "body": request.json["body"]
            }
        num_id = len(twits_count)+1
        data ["id"] = int(num_id)
        twits.append(data)
        twits_count.append(data)
        return 'Запись создана'
    if request.method == 'DELETE':
        twit = list(filter(lambda x: x["id"] == id, twits))
        if len(twit) == 0:
            return 'записи не существует'
        else:
            twits.remove(twit[0])
        return 'запись удалена'
    if request.method == 'PUT':
        twit = list(filter(lambda x: x["id"] == id, twits))
        data = {
        "author" : request.json["author"],
        "body": request.json["body"]
        }
        if len(twit) == 0:
            return 'записи не существует'
        else:
            ind = twits.index(twit[0])
            twits[ind]["author"] = request.json["author"]
            twits[ind]["body"] = request.json["body"]
            return 'запись обновлёна'
    
 

@app.route('/twits',methods=['GET'])
def get_twits():
    return twits




if __name__=='__main__':
    app.run(debug=True)