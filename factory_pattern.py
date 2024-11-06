from abc import ABC, abstractmethod

# GeometricShape Interface (abstract base class)
class GeometricShape(ABC):
    @abstractmethod
    def draw_shape(self):
        pass

# Concrete classes implementing the GeometricShape interface
class Rectangle(GeometricShape):
    def draw_shape(self):
        print("Rectangle class::draw_shape() method.")

class Square(GeometricShape):
    def draw_shape(self):
        print("Square class::draw_shape() method.")

class Circle(GeometricShape):
    def draw_shape(self):
        print("Circle class::draw_shape() method.")

# Factory class for GeometricShape
class ShapeFactory:
    def shape_object(self, shape_type):
        # Return an object of the specified shape type
        if shape_type is None:
            return None
        elif shape_type.lower() == "circle":
            return Circle()
        elif shape_type.lower() == "rectangle":
            return Rectangle()
        elif shape_type.lower() == "square":
            return Square()
        return None

# Main code to demonstrate the Factory Pattern
if __name__ == "__main__":
    # Create a ShapeFactory object
    shape_factory = ShapeFactory()

    # Create Circle object and call draw_shape method
    shape_circle = shape_factory.shape_object("CIRCLE")
    shape_circle.draw_shape()

    # Create Rectangle object and call draw_shape method
    shape_rectangle = shape_factory.shape_object("RECTANGLE")
    shape_rectangle.draw_shape()

    # Create Square object and call draw_shape method
    shape_square = shape_factory.shape_object("SQUARE")
    shape_square.draw_shape()