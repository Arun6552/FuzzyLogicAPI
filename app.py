from flask import Flask,request,jsonify
from thefuzz import fuzz
import jaro
from polyfuzz import PolyFuzz
from Levenshtein import ratio


app = Flask(__name__)
polyfuzz = PolyFuzz()

@app.route('/')
def home ():
    return "Welcome to Fuzzy Logic API"

@app.route('/Fuzzylogic', methods = ['POST'])
def FuzzyStringCheck():
    if request.method == 'POST':
        try:
            request_data = request.get_json()
            fromstring = str(request_data.get("fromString"))
            toString = str(request_data.get("toString"))

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
                print(result1)
                
                model2 = PolyFuzz("EditDistance") 
                model2.match(from_list, to_list)
                result2 = model2.get_matches()["Similarity"].values[0]
                print(result2)

                result3 = fuzz.ratio(fromstring, toString)
                result4 = fuzz.token_sort_ratio(fromstring, toString)
                result5 = jaro.jaro_winkler_metric(fromstring,toString)
                result6 = ratio(fromstring,toString)


                return  jsonify({"Model_TFIDF_Percentage":result1,"Model_EditDistance_Percentage":result2,"Model_Ratio_Percentage":result3,"Model_TokenSort_Percentage":result4,"Model_jaroDistance_Percentage":result5,"Model_LevisteniDistance_Percentage":result6})
            
        except Exception as e:
            return "Interval Server Error :" + str(e),500


if __name__ =="__main__":
    app.run(host="127.0.0.1", port=5000,debug=True)
          
          
