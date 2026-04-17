import plotly.io as pio
import plotly.graph_objects as go

red_black_template = go.layout.Template(
    layout=go.Layout(
        paper_bgcolor="#FFFFFF",
        plot_bgcolor="#F8F8F8",
        font=dict(
            family="sans-serif",
            color="#000000",
            size=12
        ),
        title=dict(
            font=dict(
                color="#000000",
                size=20
            ),
            x=0.5
        ),
        xaxis=dict(
            title_font=dict(color="#000000"),
            tickfont=dict(color="#000000"),
            gridcolor="#FFFFFF",
            linecolor="#A4A3A3",
            zerolinecolor="#464646"
        ),
        yaxis=dict(
            title_font=dict(color="#000000"),
            tickfont=dict(color="#000000"),
            gridcolor="#FFFFFF",
            linecolor="#D0D0D0",
            zerolinecolor="#6D6D6D"
        ),
        legend=dict(
            font=dict(color="#000000"),
            bgcolor="rgba(0,0,0,0)"
        ),
        colorway=[
            "#971C1C",  
            "#FB6363",  
            "#8B0000",  
            "#DC1212",  
            "#FA8072" 
        ],
        margin=dict(l=60, r=40, t=70, b=60)
    )
)

pio.templates["red_black"] = red_black_template
pio.templates.default = "red_black"
