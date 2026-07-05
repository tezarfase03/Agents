from langchain_google_genai import GoogleGenerativeAI
from langchain.agents import create_agent
from langchain.agents.middleware import wrap_model_call, ModelRequest, ModelResponse
from dotenv import load_dotenv
load_dotenv()
basic_model = GoogleGenerativeAI(model="gemini-2.5-flash")
advance_model = GoogleGenerativeAI(model="gemini-3.5-flash")

@wrap_model_call
def dynamic_model_selection(request: ModelRequest ,handler) -> ModelResponse:
    """choose model based on conversation complexity."""
    message_count = len(request.state["messages"])


    if message_count > 10:
        model = basic_model
    else:
        model = advance_model

    # ── Show which model is being used for this request ──────────────────────
    print(f"\n[Model Selected]: {model.model}\n")

    response = handler(request.override(model=model))

    # ── Print metadata from the response ─────────────────────────────────────
    if hasattr(response, "response_metadata") and response.response_metadata:
        print(f"[Response Metadata]: {response.response_metadata}\n")

    return response

agent = create_agent(
    model = basic_model,
    middleware=[dynamic_model_selection]
)

while True:
    user_input = input("you:    ")

    if user_input.lower() == "quit":
       break
    response=agent.invoke({
            "messages":[
                {   
                    "role":"user",
                    "content":user_input
                }
            ]
    }
    )
    print(f"Bot: {response}\n")
   
