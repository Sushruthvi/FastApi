from fastapi import FastAPI
app=FastAPI()

def load_data():
  with open('pateints.json','r') as f:
     data=json.load(f)
     return data;

@app.get("/")
def hello():
  return {"message":"This is patient management system API"};

@app.get("/about")
def about():
  return {"About":"A fully functional API to manage pateint records"}

@app.get("/view")
def view():
 data=load_data()
 return data;