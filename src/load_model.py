import joblib
import requests
import urllib
import os

def get_model(model_path):
    
    try:
        with open(model_path, "rb") as mh:
            rf = joblib.load(mh)
    except:
        print("Cannot fetch model from local downloading from drive")
        if not 'rt_reduced.joblib' in os.listdir('.'):
            
            url = "https://drive.google.com/file/d/1-G8-t3RwR9FukA3S8nabMsY5l5RXCc9B/view?usp=sharing"
            r = requests.get(url, allow_redirects=True)
            open(r"rt_reduced.joblib", 'wb').write(r.content)
            del r
        with open(r"rt_reduced.joblib", "rb") as m:
            rf = joblib.load(m)
    return rf

def get_model2():        
    print("Cannot fetch model from local downloading from drive")   
        
    ##url = "https://drive.google.com/file/d/1-G8-t3RwR9FukA3S8nabMsY5l5RXCc9B/view?usp=sharing"
        
    rf = joblib.load(urllib.request.urlopen("https://drive.google.com/open?id=1M7Dt7CpEOtjWdHv_wLNZdkHw5Fxn83vW"))
        
    return rf