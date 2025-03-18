# Implement RANSAC for linear regression. Come up with test cases.
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

def run_ransac(data, n_samples=2, n_iterations=100, threshold=1):
    X, Y = data[:, 0], data[:, 1]
    best_a, best_b, best_n_inliers, best_mask, best_sample = 0, 0, 0, None, None
    
    for _ in range(n_iterations):
        data_n_random_indx = np.random.choice(data.shape[0], n_samples)
        sample = data[data_n_random_indx]
        
        X_sample, Y_sample = sample[:, 0], sample[:, 1]
        X_mean = np.mean(X_sample)
        Y_mean = np.mean(Y_sample)
        denominator = np.sum((X_sample - X_mean) ** 2)
        if denominator == 0:
            continue
        a = np.sum((X_sample - X_mean) * (Y_sample - Y_mean)) / denominator
        b = Y_mean - a * X_mean
        
        Y_pred = a * X + b
        error = np.abs(Y - Y_pred)
        mask = error < threshold
        n_inliers = X[mask].shape[0]
        
        if n_inliers > best_n_inliers:
            best_a, best_b, best_n_inliers, best_mask, best_sample = a, b, n_inliers, mask, sample
    
    return best_a, best_b, best_n_inliers, best_mask, best_sample


def plot_results(X, Y, best_a, best_b, best_n_inliers, best_mask, best_sample, threshold, title):
    plt.scatter(X, Y, label='Data')
    x_test = np.linspace(min(X), max(X), 10)
    plt.plot(x_test, best_a * x_test + best_b, c='red', label='Best fit')
    plt.scatter(best_sample[:, 0], best_sample[:, 1], c='red', label='Best sample')
    plt.scatter(X[best_mask], Y[best_mask], c='green', label='Inliers')
    plt.title(f"{title}\n{threshold=}, {best_n_inliers=}, slope={best_a:.2f}, intercept={best_b:.2f}")
    plt.legend()
    plt.show()


X1 = np.linspace(0, 10, 100)
Y1 = 2 * X1 + 3
data1 = np.column_stack((X1, Y1))
best_a, best_b, best_n_inliers, best_mask, best_sample = run_ransac(data1)
plot_results(X1, Y1, best_a, best_b, best_n_inliers, best_mask, best_sample, 1, "Test Case 1: Perfect Linear Data")

X2 = np.linspace(0, 10, 100)
Y2 = 2 * X2 + 3
Y2[10:20] += 10
data2 = np.column_stack((X2, Y2))
best_a, best_b, best_n_inliers, best_mask, best_sample = run_ransac(data2)
plot_results(X2, Y2, best_a, best_b, best_n_inliers, best_mask, best_sample, 1, "Test Case 2: Linear Data with Outliers")

X3 = np.linspace(0, 10, 100)
Y3 = 2 * X3 + 3 + np.random.normal(0, 0.5, 100)
data3 = np.column_stack((X3, Y3))
best_a, best_b, best_n_inliers, best_mask, best_sample = run_ransac(data3)
plot_results(X3, Y3, best_a, best_b, best_n_inliers, best_mask, best_sample, 1, "Test Case 3: Noisy Linear Data")

X4a = np.linspace(0, 5, 50)
Y4a = 2 * X4a + 3
X4b = np.linspace(5, 10, 50)
Y4b = -X4b + 5
X4 = np.concatenate([X4a, X4b])
Y4 = np.concatenate([Y4a, Y4b])
data4 = np.column_stack((X4, Y4))
best_a, best_b, best_n_inliers, best_mask, best_sample = run_ransac(data4)
plot_results(X4, Y4, best_a, best_b, best_n_inliers, best_mask, best_sample, 1, "Test Case 4: Multiple Lines")

X5 = np.random.uniform(0, 10, 100)
Y5 = np.random.uniform(0, 10, 100)
data5 = np.column_stack((X5, Y5))
best_a, best_b, best_n_inliers, best_mask, best_sample = run_ransac(data5)
plot_results(X5, Y5, best_a, best_b, best_n_inliers, best_mask, best_sample, 1, "Test Case 5: Random Data")

X6 = np.array([0, 1, 2, 3])
Y6 = np.array([3, 5, 7, 20])
data6 = np.column_stack((X6, Y6))
best_a, best_b, best_n_inliers, best_mask, best_sample = run_ransac(data6)
plot_results(X6, Y6, best_a, best_b, best_n_inliers, best_mask, best_sample, 1, "Test Case 6: Small Dataset with Outliers")

X7 = np.array([0, 10])
Y7 = np.array([3, 23])
data7 = np.column_stack((X7, Y7))
best_a, best_b, best_n_inliers, best_mask, best_sample = run_ransac(data7)
plot_results(X7, Y7, best_a, best_b, best_n_inliers, best_mask, best_sample, 1, "Test Case 7: Only Two Points")