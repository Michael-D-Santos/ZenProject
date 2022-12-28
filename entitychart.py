import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm

values = []
labels = []

# Create the bar chart
plt.bar(x=labels, height=values, color=cm.rainbow(np.linspace(0,1, len(labels))))

plt.xlabel("type of entity")
plt.ylabel("percntage of total entity occurrences")


# Show the plot
plt.show()
