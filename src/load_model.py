import joblib
import requests
import os

def get_model(model_path):
    
    try:
        with open(model_path, "rb") as mh:
            rf = joblib.load(mh)
    except:
        print("Cannot fetch model from local downloading from drive")
        if not 'RT_rePickle.joblib' in os.listdir('.'):
            
            url = "https://drive.google.com/file/d/1-G8-t3RwR9FukA3S8nabMsY5l5RXCc9B/view?usp=sharing"
            r = requests.get(url, allow_redirects=True)
            open(r"RT_rePickle.joblib", 'wb').write(r.content)
            del r
        with open(r"RT_rePickle.joblib", "rb") as m:
            rf = joblib.load(m)
    return rf