import ollama

ollama_client = ollama.Client(host='http://localhost:11434')

def clean_up_translated_text(text):
    if text.startswith('"') and text.endswith('"'):
        text = text[1:-1].strip()
    if text.startswith('```') and text.endswith('```'):
        text = text[1:-1].strip()
    if text.startswith('``') and text.endswith('``'):
        text = text[1:-1].strip()
    if text.startswith('`') and text.endswith('`'):
        text = text[1:-1].strip()
    if text.startswith('```'):
        text = text[3:].strip()
    if text.endswith('```'):
        text = text[:-3].strip()
    return text

def translate_text(text, language, model='llama3'):
    if language is None:
        return text

    prompt = (f"You are a professional translator from English to {language}. "
              f"Translate the following text, which is enclosed in triple backticks, from English language to grammatically perfect {language} language. "
              f"Instructions: 1) Use only the {language} alphabet in the translated text. 2) Return the translated text ONLY, without any additional comments whatsoever. "
              f"Text to translate: ```{text}``` "
              f"Translated text: ")
    response = ollama_client.chat(model=model, messages=[
        {
            'role': 'user',
            'content': prompt,
        },
    ])
    result = clean_up_translated_text(response['message']['content'])
    # logging.info(f'Input: {text[:50]} | Translated to {language}: {result[:50]} | Model: {model}')
    return result

if __name__ == '__main__':
    print(translate_text('adasda', 'English'))