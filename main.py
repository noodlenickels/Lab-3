from fastapi import FastAPI, Form, Request
from transformers import pipeline
from fastapi.templating import Jinja2Templates

app = FastAPI()


@app.post('/generate')
def generate_text(payload: dict[str, str], config: str = Form('intro')):
    input_text = payload.get('text')
    generator = pipeline('text-generation', model='ai-forever/rugpt3small_based_on_gpt2')
    if config == 'annotation':
        config_annotation = {
            "max_length": 250,
            "min_length": 100,
            "temperature": 1.1,
            "top_p": 2.,
            "num_beams": 10,
            "repetition_penalty": 1.5,
            "num_return_sequences": 4,
            "no_repeat_ngram_size": 2,
            "do_sample": True
        }
        text = generator(input_text, pad_token_id=50256, **config_annotation)
        return {'generated_text': text}
    elif config == 'intro':
        config_intro = {
            "max_length": 400,
            "min_length": 200,
            "temperature": 1.1,
            "num_beams": 5,
            "repetition_penalty": 1.5,
            "num_return_sequences": 4,
            "no_repeat_ngram_size": 2,
            "do_sample": True
        }
        text = generator(input_text, pad_token_id=50256, **config_intro)
        return {'generated_text': text}


templates = Jinja2Templates(directory="template")


@app.get('/')
def get_layout(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})