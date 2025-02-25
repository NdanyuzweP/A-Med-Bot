from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load the fine-tuned model and tokenizer
model_path = "./fine_tuned_gpt2"
tokenizer = AutoTokenizer.from_pretrained(model)
model = AutoModelForCausalLM.from_pretrained (model)

# Set device (CPU or GPU)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Define the request body model
class ChatRequest(BaseModel):
    user_input: str

# Initialize FastAPI app
app = FastAPI()

# Define the chatbot response function
def chatbot_response(user_input: str) -> str:
    input_text = f"User: {user_input}\nBot:"
    input_ids = tokenizer(input_text, return_tensors="pt").input_ids.to(device)

    # Generate the response
    output = model.generate(input_ids, max_length=50, pad_token_id=tokenizer.eos_token_id)

    # Decode the response
    response = tokenizer.decode(output[:, input_ids.shape[-1]:][0], skip_special_tokens=True)

    return response

# Define the API endpoint
@app.post("/chat/")
async def chat(chat_request: ChatRequest):
    try:
        response = chatbot_response(chat_request.user_input)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Run the FastAPI app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)