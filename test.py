import pickle

login_credentials = {}
with open('loginData.pkl', "wb") as f:
    pickle.dump(login_credentials, f)