import numpy as np
import matplotlib.pyplot as plt
# create a list of 10 epochs
epochs = np.arange(1, 11)

# generate synthetic training loss values
loss_vals = 1 / epochs

# ---line plot (Loss vs Epochs)---
plt.figure(figsize = (10,6))
plt.plot(epochs, loss_vals, linewidth = 3, marker = "D", markersize = 10, color = "blue", markerfacecolor = "black", label = "Loss")
plt.title("Training loss vs Epochs", fontsize = "20")
plt.xlabel("Epochs", fontsize = "14")
plt.ylabel("Loss", fontsize = "14")
plt.grid(True)
plt.legend()
plt.show()

# ---Scatter plot (Epochs vs Loss)---
plt.figure(figsize = (10, 6))
plt.scatter(epochs, loss_vals, marker = "s", s = 100, alpha = 0.8, color = "green")
plt.title("Epoch vs Loss", fontsize = "20")
plt.xlabel("Epochs", fontsize = "14")
plt.ylabel("Loss", fontsize = "14")
plt.grid(True)
plt.show()

# ----Bar Chart (Model Accuracy Comparison)---
models = ["Model A", "Model B", "Model C"]
accuracies = [0.85, 0.90, 0.88]

plt.figure(figsize = (10, 6))
plt.bar(models, accuracies, color = ["purple", "skyblue", "pink"], edgecolor = "black")
plt.title("Comparison of Model Accuracies", fontsize = "20")
plt.xlabel("Models", fontsize = "14")
plt.ylabel("Accuracy", fontsize = "14")
plt.show()