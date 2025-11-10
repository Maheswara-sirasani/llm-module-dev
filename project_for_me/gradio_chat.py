import gradio as gr
def chat_with_ai(message,history):
    bot_reply=f"bot reply:{message}"
    history=history + [(message,bot_reply)]
    return history,""
with gr.Blocks() as demo:
    gr.Markdown("my first chat app")
    chat=gr.Chatbot(height=400)
    msg=gr.Textbox(placeholder="ask me anything")
    clear=gr.Button("clear")
    msg.submit(chat_with_ai,[msg,chat],[chat,msg])
    clear.click(lambda:None,None,chat,queue=False)
    
demo.launch()
    
