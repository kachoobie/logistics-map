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
    # Round to 6 decimal places for simplicity.
    relevant_outputs = outputs[round(num_iter*0.8):]
    for i in range(len(relevant_outputs)):
        relevant_outputs[i] = round(relevant_outputs[i], 6)
    stability_points = set(relevant_outputs)

    return list(stability_points)


def plot_bifurcation(mu_start=2.6, mu_end=4.0, x_0=0.4, increment=0.01):

    pass
    # for mu in range(mu_start, mu_end, increment):




if __name__ == "__main__":
    find_stability_for_mu(3.9)