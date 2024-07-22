def correct_name(full_name) -> str:
    full_name = full_name.strip()
    name_parts = full_name.split(' ')

    capitalize_parts  = ' '.join(part.capitalize() for part in name_parts)

    return capitalize_parts

