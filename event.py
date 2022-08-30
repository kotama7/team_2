import dictionary

def event_resalt(signal,tool):
    new_tool = tool
    extra_event_boo = False
    return new_tool, extra_event_boo

def call_text(signal):
    with open(dictionary[signal],'r',encoding='utf-8') as f:
        text = f.read()
    return text