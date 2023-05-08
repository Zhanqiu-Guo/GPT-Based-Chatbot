import openai
import gradio as gr
import os

os.environ['OPENAI_API_KEY'] = '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'
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

completion = openai.Completion()

def chatbot(input):
    if input:
        prom = f'\nCustomer: {input}\nAgent:' 
        response = completion.create( 
            model = 'ada:ft-personal-2023-03-23-02-43-27',
            prompt = prom,
        )
        return response.choices[0].text.strip()
'''
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            model='ada:ft-personal-2023-03-23-02-43-27', messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
'''
       
    

inputs = gr.inputs.Textbox(lines=7, label="Chat with AI")
outputs = gr.outputs.Textbox(label="Reply")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="AI Chatbot For Restaurant",
             description="Give description of your desired restaurant",
             theme="compact").launch(share=True)