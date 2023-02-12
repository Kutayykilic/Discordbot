def handle_response(message):
    p_message=message.lower()

    if p_message == "upload":
        return "sup"
    else:
        return "Yeah I can't understand it"

