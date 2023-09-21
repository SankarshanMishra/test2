from pyparsing import Literal, Word, alphas, Combine, Suppress, Group, Optional, restOfLine

# Define your chat template with user and assistant tags
chat_template = """
{{#user}}
{{user_message}}
{{/user}}
{{#assistant}}
{{assistant_message}}
{{/assistant}}
{{#assistant}}
{{gen_command}}
{{/assistant}}
"""

# Define grammar for Handlebars-like tags
open_user_tag = Literal('{{#user}}')
close_user_tag = Literal('{{/user}}')
open_assistant_tag = Literal('{{#assistant}}')
close_assistant_tag = Literal('{{/assistant}}')
gen_command = Combine(Literal('{{gen') + Word(alphas) + Suppress('}}'))


# Create a function that formats text into the chat template
def format_chat_message(user_message, assistant_message=None):
    # Wrap user message with user tags
    formatted_user_message = f"{{{{#user}}}}{user_message}{{{{/user}}}}"

    # Wrap assistant message with assistant tags
    if assistant_message:
        formatted_assistant_message = f"{{{{#assistant}}}}{assistant_message}{{{{/assistant}}}}"
    else:
        formatted_assistant_message = ""

    # Add an assistant command segment if there is no assistant message
    if not assistant_message:
        formatted_assistant_message += "{{{{#assistant}}{{gen 'default'}}{{/assistant}}}}"

    # Combine the user and assistant messages
    formatted_message = chat_template.replace('{{user_message}}', formatted_user_message)
    formatted_message = formatted_message.replace('{{assistant_message}}', formatted_assistant_message)

    return formatted_message


# Example usage:
user_message1 = "how are things going, tell me about Delhi"
assistant_message1 = "{{gen 'write' }}"
formatted_message1 = format_chat_message(user_message1, assistant_message1)

user_message2 = "Tweak this proverb to apply to model instructions instead. Where there is no guidance"
assistant_message2 = "{{gen 'rewrite'}}"
formatted_message2 = format_chat_message(user_message2, assistant_message2)

print(formatted_message1)
print(formatted_message2)
