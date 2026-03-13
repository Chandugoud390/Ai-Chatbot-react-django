from groq import Groq
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response


client = Groq(api_key=settings.GROQ_API_KEY)

def load_system_prompt():
    with open("prompts/unihelp_template.md", "r", encoding="utf-8") as f:
        return f.read()
    

@api_view(["POST"])
def chat_with_unihelp(request):
    try:
        SYSTEM_TEMPLATE = load_system_prompt()
        user_message = request.data.get("message", "")

        # Construct the new "input" format
        prompt_input = [
            {
                "role": "system",
                "content": SYSTEM_TEMPLATE
            },
            {
                "role": "user",
                "content": user_message
            }
        ]

        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=prompt_input
        )

        # Extract model response
        answer = completion.choices[0].message.content

        return Response({"response": answer})

    except Exception as e:
        return Response(
            {"error": f"An unexpected error occurred. {str(e)}"},
            status=500
        )

