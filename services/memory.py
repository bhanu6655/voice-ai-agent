conversation_memory = []

def add_memory(role, message):

    conversation_memory.append({
        "role": role,
        "message": message
    })

def get_memory():
    return conversation_memory