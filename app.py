from flask import Flask,request,jsonify

from polyfuzz import PolyFuzz
# request.data

app = Flask(__name__)
polyfuzz = PolyFuzz()

@app.route('/')
def home ():
    return "Welcome to Fuzzy Logic API created by Arun"

@app.route('/Fuzzylogic', methods = ['POST'])
def FuzzyStringCheck():
    if request.method == 'POST':
        try:
            request_data = request.get_json()
            fromstring = str(request_data.get("fromString"))
            toString = str(request_data.get("toString"))
            modelNumber = str(request_data.get("modelNumber"))

            fromstring = fromstring.lower().strip()
            toString = toString.lower().strip()

            from_list = []
            to_list = []

            from_list.append(fromstring)
            to_list.append(toString)

            print(from_list,to_list)

            if from_list is not None:
                model1 = PolyFuzz("TF-IDF")
                model1.match(from_list, to_list)
                result1 = model1.get_matches()["Similarity"].values[0]
                
                model2 = PolyFuzz("EditDistance") 
                model2.match(from_list, to_list)
                result2 = model2.get_matches()["Similarity"].values[0]
                return  jsonify({"Model_Alog":"TF-IDF","Percentage":result1,"Model_Alog":"EditDistance","Percentage":result2})
            
        except Exception as e:
            return "Interval Server Error :" + str(e),500


if __name__ =="__main__":
    app.run(host="127.0.0.1", port=5000,debug=True)
          
          
