import matplotlib.pyplot as plt


def x_n_plus_1(mu: float, x_n: float) -> float:
    """
    Logistic map equation.

    mu - growth rate
    x_n - value from previous generation
    """

    return mu * x_n * (1 - x_n)


def find_stability_for_mu(mu: float, x_0=0.4, num_iter=100000) -> list:
    """
    Determines the stability points for a given mu and initial x and returns
    them a as a list.

    mu - growth rate
    x_0 - initial x
    num_iter - number of iterations to find stability points
    """
    
    outputs = []

    current_x_n = x_0
    for i in range(num_iter):
        current_x_n = x_n_plus_1(mu, current_x_n)
        outputs.append(current_x_n)
    
    # Determine stability points from last 20% of calculations.
    # Round to 6 decimal places to eliminate negligible differences between values.
    relevant_outputs = outputs[round(num_iter*0.8):]
    for i in range(len(relevant_outputs)):
        relevant_outputs[i] = round(relevant_outputs[i], 6)
    stability_points = set(relevant_outputs)

    return list(stability_points)


def create_bifurcation_dict(mu_start=2.6, mu_end=4.0, x_0=0.4, increment=0.01) -> dict:
    """
    Creates and returns dictionary with mu as keys and corresponding stability points
    as values.

    mu_start - mu start for beginning of iteration
    mu_end - end point of iteration
    x_0 - initial x value
    increment - mu value increase per iteration
    """

    mu_x_dict = {}

    current_mu = mu_start
    while current_mu < mu_end:
        x_vals = find_stability_for_mu(current_mu, x_0=x_0)
        mu_x_dict[current_mu] = x_vals
        current_mu += increment
    
    return mu_x_dict


def create_bifurcation_plot_axes(mu_dict: dict) -> tuple:
    """
    Helper function for creating x and y axes to plot. Returns tuple(x, y).

    mu_dict - dictionary with mu as keys and stability points as values
    """

    x = []
    y = []
    for k in mu_dict.keys():
        current_y = mu_dict[k]
        current_x = [k] * len(current_y)    # Repeat instances of mu depending on
                                            # number of stability points
        x.extend(current_x)
        y.extend(current_y)
    
    return x, y


def main():

    bifurcation_dict = create_bifurcation_dict()
    x, y = create_bifurcation_plot_axes(bifurcation_dict)
    
    # Plot bifurcation
    plt.rcParams['text.usetex'] = True
    plt.scatter(x, y, s=1)
    plt.xlabel(r'$\mu$')
    plt.ylabel('x')
    plt.show()




if __name__ == "__main__":

    main()