from django.shortcuts import render
import openai
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
import torch
from transformers import GenerationConfig, pipeline

def answer_question(request):
    if request.method == 'POST':
        question = request.POST.get('question')

        # Send question a question to Dolly API
        # Warning ensure you have sufficient memory (16 gb GPU minimum recommended).
        # generate_text = pipeline(model="databricks/dolly-v2-3b",
        #                          torch_dtype=torch.bfloat16,
        #                          trust_remote_code=True,
        #                          device_map="auto",
        #                          return_full_text=True)
        # answer = generate_text(question)


        #Make sure to export OPENAI_API_KEY if using the next two models. See https://platform.openai.com/account/api-keys

        # Send question to OpenAI API
        # response = openai.Completion.create(
        #     engine='text-davinci-001',
        #     prompt=question,
        #     max_tokens=100,
        #     n=1,
        #     stop=None,
        #     temperature=0.7,
        #     top_p=1,
        #     frequency_penalty=0,
        #     presence_penalty=0
        # )
        # answer = response.choices[0].text.strip()


        # Get Message Completions from a Chat Model using OpenAI API
        chat = ChatOpenAI(temperature=0)

        messages = [
            SystemMessage(content="You are a helpful assistant that only knows about pokemon. If a question is not about pokemon i want you to respond,'Sorry I'm only a Pokemon expert. I cant help with that question.'"),
            HumanMessage(content=question)
        ]
        chat(messages)
        answer = chat(messages)

        return render(request, 'pokemon/answer.html', {'answer': answer})

    return render(request, 'pokemon/question.html')
