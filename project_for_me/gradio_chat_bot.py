import gradio as gr
def chat_with_ai_bot(message,history):
    bot_reply=f"echo:{message}"
    history=history+[(message,bot_reply)]
    return history,""
with gr.Blocks() as demo:
    gr.Markdown("my first chat bot")
    chat=gr.Chatbot(height=400)
    msg=gr.Textbox(placeholder="ask me everything")
    clear=gr.Button("clear")
    
    msg.submit(chat_with_ai_bot,[msg,chat],[chat,msg])
    clear.click(lambda:None,None,chat,queue=False)
    
demo.launch()    
    