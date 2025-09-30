import streamlit as st

from apputil import *

# Load Titanic dataset
df = pd.read_csv('https://raw.githubusercontent.com/leontoddjohnson/datasets/main/data/titanic.csv')

st.write(
"Did men in third class have the lowest survival rate?"
)

def visualize_demographic():
    data = survival_demographics()
    men_data = data[data['Sex'] == 'male']
    
    fig = px.bar(
        men_data,
        x='Pclass',
        y='survival_rate',
        text='survival_rate',
        barmode='group',
        title='Survival Rate of Men by Class',
        labels={'Pclass': 'Passenger Class', 'survival_rate': 'Survival Rate'},
        color= "PClass" + men_data['Pclass'].astype(str),  # optional: color by class
    )
    fig.update_layout(
        xaxis=dict(type='category', tickmode='array', tickvals=['male','female']),
        yaxis=dict(range=[0, 1]),
        uniformtext_minsize=8,
        uniformtext_mode='hide'
    )   
    fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
    
    return fig

# Generate and display the figure
fig1 = visualize_demographic()
st.plotly_chart(fig1, use_container_width=True)


st.write("Do passengers with larger families pay higher fares in first class?")

def visualize_families():
    grouped = family_groups()

    # Plot: Average fare by family size for each class
    fig = px.scatter(
        grouped,
        x='family_size',
        y='avg_fare',
        size='n_passengers',
        color='Pclass',
        hover_data=['n_passengers', 'avg_fare'],
        title='Family Size vs Average Fare by Passenger Class',
        labels={
            'family_size': 'Family Size',
            'avg_fare': 'Average Fare',
            'Pclass': 'Passenger Class',
            'n_passengers': 'Number of Passengers'
        },
        size_max=60
    )
    
    # Customize layout
    fig.update_layout(
        xaxis=dict(tickmode='linear', dtick=1),
        yaxis=dict(tickformat=".0%"),
        showlegend=True
    )
    return fig


# Generate and display the figure
fig2 = visualize_families()
st.plotly_chart(fig2, use_container_width=True)
'''
st.write(
'''
# Titanic Visualization Bonus
'''
)
# Generate and display the figure
fig3 = visualize_family_size()
st.plotly_chart(fig3, use_container_width=True)
'''