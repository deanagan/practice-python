def left_join(phrases: tuple) -> str:
    """
        Join strings and replace "right" to "left"
    """
    return ",".join(word.replace('right', 'left') for word in phrases)
