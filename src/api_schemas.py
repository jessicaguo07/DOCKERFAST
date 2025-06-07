from pydantic import BaseModel
class TextClassification(BaseModel):
    input_text_list: list[str]

class ResponseDict(BaseModel):
    output: dict[str, dict[str, float]]
    class Config:
        schema_extra = {
            "example": {
                "output": {
                    "Good":{
                        "negative": 0.1,
                        "neutral": 0.1,
                        "positive": 0.8
                    },
                    "Bad": {
                        "negative": 0.8,
                        "neutral": 0.1,
                        "positive": 0.1
                    }
                }
            }
        }
    
