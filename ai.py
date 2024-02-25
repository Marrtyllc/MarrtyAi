import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "Craft an engaging article with a unique perspective. Choose a captivating topic, infuse your distinct voice, use creative writing techniques, provide fresh insights, and conclude impactfully. Revise for clarity and coherence. Aim for memorable, thought-provoking content."}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Marrty Ai")

demo.launch(share=True)
