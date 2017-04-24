from matplotlib import pyplot
from quicksort import *
from csv_reader import *
from numpy.random import rand
from linked_list_stack import Stack
import time

pyplot.style.use('seaborn-pastel')
pyplot.rcParams['text.antialiased'] = True


# Given a double linked list of points, determine the point with the lowest y-coordinate
def get_base_pt(p):
    base = p.get_head()
    for i in range(1, p.get_size()):
        temp = p.get(i)
        if temp.get_y() < base.get_y():
            base = temp
    return base


# Given a filename for a CSV file, determine and plot a convex hull around the points
def convex_hull(filename):
    start = time.time()  # Find the start time to later determine total time elapsed
    points = read_csv(filename)  # Read the csv file to a double linked list of points
    first_pt = get_base_pt(points)  # Determine the point with lowest y-coordinate to be used as base point
    n = points.get_size()  # Find the size of the double linked list of points

    points.swap(points.get_head(), first_pt)  # Swap the first point with the base point

    # Sort the list of points (excluding base point) on their angle with the base point
    # and the x-axis, using quick sort.
    qsort(points, 1, n - 1, points.get_head())
    m = 1
    i = 1

    # Loop through entire list of points (excluding base point) to get rid of redundant points
    while i < n:
        # If any two points are collinear with the base point, ignore the second point
        while i < (n - 1) and ccw(points.get_head(), points.get(i), points.get(i + 1)) == 0:
            i += 1

        # Set point at index m to be the point at index i
        points.get(m).set_xy(points.get(i).get_x(), points.get(i).get_y())
        m += 1
        i += 1

    # Initialize Stack object to hold the points of the convex hull
    # Use first three points of points list as initial values
    hull = Stack()
    hull.push(points.get(0))
    hull.push(points.get(1))
    hull.push(points.get(2))

    k = 3  # Initialize loop variable at 3 to ignore initial points
    while k < m:
        # If the current point make a clockwise turn with the top two points of the
        # stack, then pop the stack.
        while ccw(hull.second().get_value(), hull.top().get_value(), points.get(k)) != 1:
            hull.pop()

        # Push the current point onto the stack
        hull.push(points.get(k))
        k += 1

    # Determine and print the total time elapsed for the convex hull algorithm
    end = time.time()
    print "Total time elapsed: " + str(end - start)

    # Determine random colors to be used for points and set the scale
    color = rand(2, 3)
    scale = 100

    # Create strings with the x and y coordinates of the points to be used for plotting
    x_coord = points.get_coords("x")
    y_coord = points.get_coords("y")

    # Convert the string of coordinates to an array to be used for plotting only
    x_coord = x_coord.split(",")
    y_coord = y_coord.split(",")

    # Plot all of the data points
    pyplot.scatter(x_coord, y_coord, scale, color[0])

    # Declare a variable to hold the top point of the stack and initialize two single linked lists
    first = hull.top().get_value()
    x_list = Stack()
    y_list = Stack()

    # Loop through stack and append coordinates to respective single linked lists
    while not hull.is_empty():
        x_list.push(hull.top().get_value().get_x())
        y_list.push(hull.top().get_value().get_y())
        hull.pop()

    # Append the temp point variable to the list that is now also at the head of the list in order to complete
    # the shape of the convex hull
    x_list.push(first.x)
    y_list.push(first.y)

    # Convert the two single linked lists to string and then arrays for plotting only
    x_coord = x_list.to_string()
    y_coord = y_list.to_string()
    x_coord = x_coord.split(",")
    y_coord = y_coord.split(",")

    # Initialize plot axis
    axis = pyplot.subplot()
    axis.set_xlabel('X')
    axis.set_ylabel('Y')
    axis.set_title(filename[0].upper() + filename[1:] + "        Time Elapsed: ~" + str(end-start) + " sec")

    # Plot convex hull
    pyplot.plot(x_coord, y_coord, linewidth=3)
    pyplot.axis('tight')

    # Save the plot to a png file and show the plot
    pyplot.savefig(filename[:-4]+"_plot.png", format='png', bbox_inches='tight', dpi=300)
    pyplot.show()


convex_hull('exercise-1.csv')
convex_hull('exercise-2.csv')
convex_hull('exercise-3.csv')
convex_hull('exercise-4.csv')
convex_hull('exercise-5.csv')
convex_hull('exercise-6.csv')
