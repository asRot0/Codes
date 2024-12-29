def create_bubble(message: str, max_width: int = 40):
    """
    Creates a cloud-style speech bubble around the message.

    Args:
        message: The message to display in the speech bubble.
        max_width: Maximum width of the speech bubble.

    Returns:
        The formatted speech bubble string.
    """
    words = message.split()
    lines, current_line = [], []
    current_len = 0

    # Split the message into lines that fit the max_width
    for word in words:
        if current_len + len(word) + 1 > max_width:
            lines.append(" ".join(current_line))
            current_line = [word]
            current_len = len(word)
        else:
            current_line.append(word)
            current_len += len(word) + 1

    if current_line:
        lines.append(" ".join(current_line))

    # Create the bubble top and bottom (rounded edges for cloud effect)
    bubble_width = max(len(line) for line in lines)
    top = "  " + "_" * (bubble_width + 2)
    bottom = "  " + "-" * (bubble_width + 2)

    # Cloud-like round corners
    bubble_lines = "\n".join(f"/ {line.ljust(bubble_width)} \\" for line in lines)

    # Adding fluffy cloud effect
    cloud_bubble = f"{top}\n{bubble_lines}\n{bottom}"

    # Adding "tail" for the bubble, like in cartoons
    tail = r"""
        \\
         \\
          (o o)
         (  =  )
        """
    cloud = r'''
    ⠀⠀⠀⠀⠀⠀⠀⢀⣠⠤⠴⠒⠒⠒⠒⠒⠒⠒⠦⢤⣀⡀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⣀⡴⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⢦⡀⠀⠀⠀⠀
    ⠀⠀⢠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢳⡀⠀⠀
    ⠀⣰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣆⠀
    ⢰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡆
    ⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷
    ⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿
    ⢸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠇
    ⠀⢳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡯⠁
    ⠀⠀⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠁⠀
    ⠀⠀⠀⠀⠙⠦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠶⠋⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠉⠛⠲⠤⢤⣀⠀⠀⠀⠀⠀⢶⠶⠛⠉⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠳⢦⣄⡀⠈⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠓⢦⣝⣦⡀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⣓⠀⠀⠀⠀⠀⠀
    '''
    cloud1 = r'''
    ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛🟪⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟪🟪🟪⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜🟪⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛🟪🟪🟪🟪🟪⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛🟪⬜⬜⬜⬜⬛⬛⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟪⬛⬛🟪🟪🟪🟪🟪🟪⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛🟪🟪⬜🟪⬜⬜⬜⬛🟪⬛
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟪⬛⬛⬛⬛🟪🟪🟪🟪🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟪🟪🟪⬜🟪⬜🟪⬜⬛⬛🟪⬛
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟪⬛⬛⬛⬛⬛🟪🟪🟪🟪🟪🟪⬛⬛⬜⬜⬜⬜⬛⬛🟪🟪🟪⬛🟪🟪🟪🟪🟪⬜🟪⬜🟪⬛⬛⬛⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟪⬛⬛⬛⬛⬛🟪🟪🟪🟪🟪🟪🟪⬛🟪⬛⬛🟪🟪⬜⬜⬜🟪🟪🟪🟪🟪🟪🟪🟪🟪⬛⬛🟪⬛⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟪⬛⬛⬛⬛⬛⬛🟪🟪🟪🟪🟪🟪🟪⬛🟪🟪🟪🟪🟪🟪⬜⬜⬜🟪🟪🟪🟪🟪🟪⬛⬛⬛🟪⬛⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟪⬛⬛⬛⬛⬛⬛⬛🟪🟪⬜🟪🟪🟪⬛🟪🟪🟪🟪🟪🟪🟪⬜⬜⬜🟪🟪🟪🟪⬛⬛⬛🟪⬛⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟪⬛⬛⬛⬛⬛⬛⬛🟪🟪⬜🟪⬜🟪⬛🟪🟪🟪🟪🟪⬛⬛⬜⬜⬜🟪🟪⬛⬛⬛⬛🟪🟪⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟪⬛⬛⬛⬛⬛⬛⬛⬛🟪🟪⬜🟪⬜⬛🟪🟪🟪🟪⬛🟪⬜⬛⬜⬜🟪🟪⬛⬛⬛🟪⬛⬜⬜⬜
⬜⬜⬜⬜⬛🟪🟪⬜⬜⬜⬜⬜⬛🟪⬛⬛⬛⬛⬛⬛⬛⬛🟪🟪⬜🟪🟪🟪🟪🟪🟪⬛🟪🟪⬛⬜⬜⬜⬛⬛⬛🟪⬛⬜⬜⬜⬜
⬜⬜⬜⬛⬜⬜⬜🟪⬜⬜⬜⬜⬜⬛🟪⬛⬛⬛⬛⬛⬛⬛⬛🟪🟪🟪🟪🟪🟪🟪🟪🟪⬛⬛⬜⬜⬜🟪⬛⬛🟪⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬛🟪⬜⬜⬛⬜⬜⬜⬜⬜⬜⬛🟪⬛⬛⬛⬛⬛⬛⬛🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪⬜⬜⬜🟪⬛⬛⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬛🟪🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬛🟪⬛⬛⬛⬛⬛🟪🟪🟪⬛⬛🟪🟪⬜🟪🟪🟪🟪⬜⬜🟪⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬛🟪🟪🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬛🟪🟪⬛⬛⬛🟪🟪🟪⬛⬜⬛⬛⬜⬜🟪🟪🟪🟪⬜⬛⬜🟪⬛⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬛🟪🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛🟪🟪🟪🟪🟪🟪🟪⬛⬛⬛🟪⬜🟪🟪🟪🟪⬜⬛🟪🟪🟪⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬛🟪🟪🟪⬛⬜⬜⬜⬜⬛⬛🟪⬜⬜⬜⬜⬜⬛🟪🟪🟪🟪🟪🟪🟪🟪⬛⬛🟪🟪🟪🟪🟪⬜⬛⬛🟪🟪🟪⬛⬜⬜⬜⬜⬜
⬜⬛🟪🟪🟪🟪⬛⬜⬜⬜⬛🟪⬜⬜🟪⬜⬜⬜⬛🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪⬛🟪🟪🟪⬛⬜⬜⬜⬜⬜
⬜⬛🟪🟪🟪⬛⬜⬜⬜⬛🟪⬜⬜⬜⬛⬜⬜⬜⬛🟪🟪🟪🟪🟪⬛🟪🟪🟪🟪🟪🟪🟪🟪🟪⬛🟪🟪⬛🟪🟪🟪🟪⬛⬜⬜⬜⬜
⬜⬛🟪🟪🟪⬛⬜⬜⬛🟪🟪🟪⬜🟪⬛⬜⬜⬛🟪🟪🟪🟪🟪⬛🟪🟪⬛⬛🟪🟪🟪🟪🟪🟪🟪🟪⬛🟪🟪⬛⬛🟪⬛⬜⬜⬜⬜
⬛🟪🟪🟪🟪⬛⬜⬜⬛🟪🟪🟪🟪⬛⬜⬜⬜⬛🟪🟪🟪🟪🟪⬛🟪🟪🟪🟪⬛⬛🟪🟪🟪🟪⬛⬜⬜⬜⬛⬜⬜⬛⬛⬜⬜⬜⬜
⬛🟪🟪🟪⬛⬜⬜⬛🟪🟪🟪🟪⬛⬜⬜⬜⬜⬜⬛🟪🟪⬛⬜⬛🟪🟪🟪🟪🟪🟪⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬛🟪🟪🟪⬛⬜⬜⬛🟪🟪🟪⬛⬜⬜⬜⬜⬜⬜⬛🟪⬛⬜⬜⬛🟪🟪🟪🟪🟪🟪🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬛🟪🟪🟪⬛⬜⬛🟪🟪🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜⬛🟪🟪🟪🟪🟪🟪🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬛🟪🟪🟪⬛⬜⬛🟪🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟪🟪🟪🟪🟪🟪🟪🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬛🟪🟪🟪🟪⬛🟪🟪🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟪🟪🟪🟪🟪🟪🟪🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬛🟪🟪🟪⬜🟪🟪🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬛🟪🟪⬜🟪🟪🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬛🟪🟪⬜🟪🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬛🟪🟪⬜⬜🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬛🟪🟪⬜🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟪🟪🟪🟪🟪🟪🟪🟪⬜🟪🟪🟪🟪🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬛🟪🟪⬜🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟪🟪🟪🟪🟪🟪🟪⬜🟪⬛🟪🟪🟪🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬛🟪🟪🟪⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟪🟪🟪🟪🟪🟪🟪🟪🟪⬜⬛🟪🟪⬛🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬛🟪🟪⬜⬜⬛⬜⬜⬜⬜⬜⬜⬛🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪⬜🟪⬛🟪🟪⬛🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬛🟪🟪🟪⬜⬛⬜⬜⬜⬜⬜⬛🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪⬜⬛🟪⬛🟪🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬛🟪🟪🟪🟪⬛⬜⬜⬜⬛🟪🟪🟪🟪🟪🟪🟪🟪⬛🟪🟪🟪🟪🟪⬛⬛🟪🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬛🟪🟪🟪🟪🟪⬛⬛⬜⬛🟪🟪🟪🟪🟪🟪⬛🟪⬛🟪🟪🟪🟪🟪⬛⬛🟪🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛🟪🟪🟪🟪🟪🟪⬛🟪🟪🟪🟪🟪⬜⬜⬜🟪⬛⬛🟪🟪🟪🟪⬛🟪🟪🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪⬜⬜⬜⬜⬜🟪⬛🟪🟪🟪🟪⬛🟪🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬛⬛🟪🟪🟪⬛🟪🟪🟪🟪🟪⬜⬜⬜⬜🟪⬛🟪🟪🟪🟪⬛🟪🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛🟪🟪🟪🟪🟪🟪⬜⬜🟪🟪⬛⬛🟪🟪🟪⬛🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟪🟪🟪🟪🟪🟪🟪🟪🟪⬛⬛⬛🟪🟪🟪⬛🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟪🟪🟪🟪🟪🟪🟪⬛⬛🟪⬛🟪🟪🟪⬛🟪🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛🟪🟪🟪⬜🟪🟪⬛⬛⬛🟪🟪⬜⬛🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬜⬜⬛🟪🟪🟪⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
    '''

    return f"{cloud_bubble}{cloud1}"


print(create_bubble('hello worlsdcjdij eifjeijfiw jwijdiwjdi i'))