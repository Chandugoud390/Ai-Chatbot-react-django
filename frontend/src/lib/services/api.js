import axios from "axios"

export async function promptOpenai(data) {
  try {
    const response = await axios.post(
      // "http://localhost:8000/ai/chat_with_unihelp/",
      "https://ai-chatbot-react-django-1.onrender.com/ai/chat_with_unihelp/",
      data
    )
    return response.data
  } catch (err) {
    if (axios.isAxiosError(err)) {
      throw new Error(err.response?.data?.error || err.message)
    }
  }
}