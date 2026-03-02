import turtle
def draw_circle(radius, line_color='black', fill_color=None, line_thickness=1, position=(0, 0)):
    turtle.penup()
    turtle.goto(position)
    turtle.pendown()
    turtle.color(line_color)
    turtle.pensize(line_thickness)
    if fill_color:
        turtle.fillcolor(fill_color)
        turtle.begin_fill()
    turtle.circle(radius)
    if fill_color:
        turtle.end_fill()
# Main program
if __name__ == "__main__":
    # Setup turtle speed (1 to 10)
    turtle.speed(1)
    # Get the circle parameters from the user
    radius = int(input("Enter the radius of the circle: "))
    line_color = input("Enter the line color (default is black): ") or 'black'
    fill_color = input("Enter the fill color (leave blank for no fill): ")
    line_thickness = int(input("Enter the line thickness: "))
    x = int(input("Enter the x-coordinate of the circle's position: "))
    y = int(input("Enter the y-coordinate of the circle's position: "))
    # Set the circle's position
    position = (x, y)
    # Draw the circle
    draw_circle(radius, line_color, fill_color, line_thickness, position)
    # Keep the window open until it's closed manually
    turtle.done()