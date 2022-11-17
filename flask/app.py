'''

https://www.youtube.com/watch?v=-XuS0cfkvuA

'''

from flask import Flask, jsonify
# API 형성 가능해짐

from flask_restx import Api, Resource # API생성 도움

app = Flask(__name__)

api = Api(app) #api가 될거라고 하는게 app이니까


@api.route('/books') # 데코로 경로 하나 잡아주고
class Books(Resource) :
    def get(self) :
        return jsonify({"message":"Hello World"})

    def post(self) :
        pass




@api.route('/book<int:id>') # 다양한 클래스 만들어질 수 있음..?
class BookResource(Resource) :
    def get(self, id) :
        pass

    def put(self, id) :
        pass

    def delete(self, id) :
        pass



# json으로 반응하기때문에?
# 그래서 jsonify를 넣어줬고
# 그 이후 route/book에서 원래 get ~ pass 였는데 return ~ 해줌


if __name__ == "__main__" :
    app.run(debug=True)

    



