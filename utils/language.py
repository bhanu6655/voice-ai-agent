def detect_language(text):

    tamil_chars = range(0x0B80, 0x0BFF)
    hindi_chars = range(0x0900, 0x097F)

    for char in text:

        if ord(char) in tamil_chars:
            return "ta"

        if ord(char) in hindi_chars:
            return "hi"

    return "en"