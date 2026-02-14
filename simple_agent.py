from ollama import chat
from ollama import ChatResponse

response: ChatResponse = chat(model='gemma:2b', messages=[
  {
    'role': 'system',
    'content': 'You are a helpful assistant.',
  },
  {
    'role': 'user',
    'content': 'Can the ocean water level reduce due to gloabl warming?',
  },
])
print(response.message.content)