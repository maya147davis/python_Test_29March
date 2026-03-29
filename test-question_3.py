def snake_to_camel(text: str) -> str:
    parts = text.split('_')
    camel = parts[0]
    for word in parts[1:]:
        camel += word.capitalize()

    return camel


print(snake_to_camel(input("Enter a string: ")))