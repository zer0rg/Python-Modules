def ft_plot_area():
    try:
        length = int(input("Enter length:\n"))
        width = int(input("Enter width:\n"))
        area = length * width
        print("Plot area: ", area)
    except Exception:
        print("The width and length must be an integer")
