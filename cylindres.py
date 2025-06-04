def convert_cylinder(sphere: float, cylinder: float, axis: float) -> tuple:
    """Takes the values of the cylinder and translates them

    Args:
        sphere (float): The sphere of the glass
        cylinder (float): The cylinder of the glass
        axis (float): The axis of the glass

    Returns:
        tuple: A tuple containing the new sphere, cylinder and axis
    """
    new_sphere = sphere + cylinder
    new_cylinder = -cylinder
    new_axis = axis + 90 
    
    #if the axis is above 180, we should remove 180
    if new_axis > 180:
        new_axis -= 180
        
    return new_sphere, new_cylinder, new_axis


def show_translated_value(new_sphere: float, new_cylinder: float, new_axis: float) -> str: 
    """Takes the new visual correction values and show them in a formatted string

    Args:
        new_sphere (float): The sphere of the glass
        new_cylinder (float): The cylinder of the glass
        new_axis (float): The axis of the glass

    Returns:
        str: The formatted visual corrections
    """
    return f'+{new_sphere:.2f} / {'+' if new_cylinder > 0 else ''}{new_cylinder:.2f} x {new_axis}°'


def translate_to_positive_cylinder(sphere: float, cylinder: float, axis: float) -> str: 
    """This function takes vision correction with a negative cylinder to translate them into a positive one. 

    Args:
        sphere (float): The sphere of the glass
        cylinder (float): The cylinder of the glass
        axis (float): The axis of the glass

    Raises:
        ValueError: In case the cylinder is not negative, an error is raised.

    Returns:
        str: The formatted new visual corrections
    """
    if cylinder >= 0: 
        raise ValueError('Cylinder is not negative')
    new_sphere, new_cylinder, new_axis = convert_cylinder(sphere, cylinder, axis)
    
    return show_translated_value(new_sphere, new_cylinder, new_axis)


def translate_to_negative_cylinder(sphere: float, cylinder: float, axis: float) -> str: 
    """This function takes a visual correction with positive cylinder and translates it into a negative one

    Args:
        sphere (float): The sphere of the glass
        cylinder (float): The cylinder of the glass
        axis (float): The axis of the glass

    Raises:
        ValueError: Raises an error if the cylinder is not positive 

    Returns:
        str: The formatted new visual corrections
    """
    if cylinder < 0: 
        raise ValueError('Cylinder is not positive')
    new_sphere, new_cylinder, new_axis = convert_cylinder(sphere, cylinder, axis)
    
    return show_translated_value(new_sphere, new_cylinder, new_axis)


if __name__ == '__main__': 
    sphere = float(input('Enter the value of the sphere: '))
    cylinder = float(input('Enter the value of the cylinder: '))
    axis = float(input('Enter the value of the axis: '))
    if cylinder < 0: 
        print(translate_to_positive_cylinder(sphere, cylinder, axis))
    else: 
        print(translate_to_negative_cylinder(sphere, cylinder, axis))