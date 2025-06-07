import torch
from scipy.special import softmax
from fastapi import FastAPI, Security
from src.preprocess_helper import preprocess
from src.security import auth_api_key
from src.setup_model import download_model
from src.api_schemas import TextClassification, ResponseDict

#Start up app
app = FastAPI()
# Load the model
tokenizer, model = download_model()
labels = ['negative', 'neutral', 'positive']
@app.get("/")
def read_root():
    return {"Hello": "World"}
@app.post('/score/', response_model = ResponseDict)
def score(input_data: TextClassification, api_key: str = Security(auth_api_key)):
    # Process user input strings
    user_input_list = input_data.input_text_list
    processed_user_input_list = [preprocess(text) for text in user_input_list]
    encoded_input = tokenizer(processed_user_input_list, return_tensors='pt', padding=True, truncation=True)

    # Run through model and normalize
    with torch.no_grad():
        scores = model(**encoded_input)[0].detach().numpy()
    scores_normalized = softmax(scores, axis=1).tolist()
    output_dict = {}
    for i, text in zip(processed_user_input_list, scores_normalized):
        scores_dict = {k:v for k, v in zip(labels, text)}
        output_dict[i] = scores_dict
    return {'output': output_dict}


# app = FastAPI()
    
# @app.get("/")
# def test_import():
#         # test_text = "Hello @user check http://example.com"
#         # return {"result": preprocess(test_text)}   
#     return {"message": "Hello World!"}


if __name__ == "__main__":
    #This runs when executing `python src/main.py` directly
    import uvicorn
    print("Running self-test...")
    test_text = "Direct test @user http://test.com"
    print(f"Test: {preprocess(test_text)}")
    uvicorn.run(app, host="0.0.0.0", port=8000)
    






        
        
