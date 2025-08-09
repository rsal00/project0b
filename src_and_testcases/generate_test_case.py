# Generating the corrected TestOutputLine sequence for 999 diagonal boxes
def generate_test_output_lines_fixed(num_boxes: int):
    lines = []
    if num_boxes <= 0:
        return lines
    # Initial top and first side (first top has weight 1.0)
    lines.append("TestOutputLine('+-+', 1.0),")
    lines.append("TestOutputLine('| |', 0.1),")
    # For boxes 2..n, follow the observed pattern
    for k in range(2, num_boxes + 1):
        indent_top = " " * (2 * (k - 2))
        top = indent_top + "+-+-+"
        lines.append(f"TestOutputLine('{top}', 0.1),")
        indent_side = " " * (2 * (k - 1))
        side = indent_side + "| |"
        lines.append(f"TestOutputLine('{side}', 0.1),")
    # Final closing top for the last box (indented by 2*(n-1) spaces)
    final_indent = " " * (2 * (num_boxes - 1))
    final_top = final_indent + "+-+"
    lines.append(f"TestOutputLine('{final_top}', 0.1),")
    return lines

num_boxes = 500
lines = generate_test_output_lines_fixed(num_boxes)

# Save to a text file
out_path = "/Users/rubensalazar/Documents/Programming/PYTHON/project0b/test_output_500_boxes.txt"
with open(out_path, "w") as f:
    for line in lines:
        f.write(line + "\n")
