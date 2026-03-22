import pandas as pd
import plotly.express as px
df = pd.DataFrame({
    "Epoch": list(range(1,11)),
    "Loss": [0.9, 0.7, 0.5, 0.35, 0.25, 0.18, 0.15, 0.13, 0.12, 0.1]
}
)

fig = px.line(
    df,
    x = "Epoch",
    y = "Loss",
    title = "Training loss over Epochs",
    labels = {
        "Epoch": "Epoch number",
        "Loss": "Training Loss"
    }
)

fig.add_annotation(x=8, y=0.13, text= "Loss Stabilizes", showarrow=True, arrowhead=1)
fig.show()