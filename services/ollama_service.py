from ollama import chat


def make_ollama_request(data: dict):
    prompt: str = '''
    Below is the latest system diagnostic data.
        Analyze it and answer the following questions:
        1. Are there any signs of CPU, memory, or disk overload?
        2. What are the possible causes of the problems you are experiencing?
        3. What actions do you recommend to improve system performance?
    Data:
    {data}'''.format(data=data)
    messages = [
        {"role": "system",
         "content": "You are an expert in analyzing computer system performance. Your job is to analyze provided system metrics and provide recommendations for improving performance, identifying potential problems, and advising on system optimization."},
        {"role": "user", "content": prompt},
    ]
    reply = chat(model='llama3.2', messages=messages)
    return reply.message.content