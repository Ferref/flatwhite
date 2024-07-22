def correct_name(name: str) -> str:
    name = name.strip()
    name_parts = name.split()

    capitalize_parts = ' '.join(part.capitalize() for part in name_parts)

    return capitalize_parts
