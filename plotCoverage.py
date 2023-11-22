import plotly.express as px
import argparse
import plotly.graph_objects as go
import pandas as pd

def create_combined_plot(tsv_file, html_output, sample_name):
    # Read data from TSV file
    df = pd.read_csv(tsv_file, sep='\t')

    # Create traces for lines
    line_traces = []
    for gene, color in zip(df['Gene'].unique(), px.colors.qualitative.Set1):
        subset = df[df['Gene'] == gene]
        line_trace = go.Scatter(x=subset['Position'], y=subset['Value'], mode='lines', name=gene, line=dict(color=color), showlegend=False)
        line_traces.append(line_trace)

    # Create traces for filled areas
    area_traces = []
    for gene, color in zip(df['Gene'].unique(), px.colors.qualitative.Set1):
        subset = df[df['Gene'] == gene]
        area_trace = go.Scatter(x=subset['Position'], y=subset['Value'], mode='lines', name=gene, fill='tozeroy', fillcolor=color, line=dict(color='rgba(255,255,255,0)'))
        area_traces.append(area_trace)

    # Create layout
    layout = go.Layout(title=f'Sample: {sample_name}',
                       height=500,
                       xaxis=dict(tickformat="d"),
                       xaxis_title='Genome Position',  # X-axis label
                       yaxis_title='Depth')  # Y-axis label

    # Create figure
    fig = go.Figure(data=line_traces + area_traces, layout=layout)

    # Save the plot as an HTML file
    fig.write_html(html_output)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create a combined line and area fill plot from a TSV file and save it as an HTML file.')
    parser.add_argument('--inTSV', required=True, help='Input TSV file path')
    parser.add_argument('--outHTML', required=True, help='Output HTML file path')
    parser.add_argument('--sample', required=True, help='Sample name for the title')
    args = parser.parse_args()

    create_combined_plot(args.inTSV, args.outHTML, args.sample)
