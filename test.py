from polyfuzz import PolyFuzz

from_list = ["apple","Chaudhary"]
to_list = ["apple","Chau"]

model = PolyFuzz("TF-IDF")
model.match(from_list, to_list)

result =model.get_matches()
for row in result.iterrows():
    print(row)
