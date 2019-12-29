import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

wind = pd.read_csv('Winds2000.csv')

fig1 = px.bar_polar(wind, r="TarguSecuiescSPD", theta="TarguSecuiesc",
                    template="plotly_dark",
                    title='Targu Secuiesc',
                    color_discrete_sequence= px.colors.sequential.Plasma[-2::-1]
                    )
fig1.show()

fig2 = px.bar_polar(wind, r="AurelVlaicuSPD", theta="AurelVlaicu",
                    template="plotly_dark",
                    title='Aurel Vlaicu'
                    #color_discrete_sequence= px.colors.sequential.Plasma[-2::-1]
                    )
fig2.show()

fig3 = px.bar_polar(wind, r="IasiSPD", theta="Iasi",
                    template="plotly_dark",
                    title='Iasi'
                    #color_discrete_sequence=px.colors.sequential.Plasma[-2::-1]
                    )
fig3.show()

fig4 = px.bar_polar(wind, r="ConstantaSPD", theta="Constanta",
                    template="plotly_dark",
                    title='Constanta'
                    #color_discrete_sequence=px.colors.sequential.Plasma[-2::-1]
                    )
fig4.show()

fig5 = px.bar_polar(wind, r="RamnicuValceaSPD", theta="RamnicuValcea",
                    template="plotly_dark",
                    title='Ramnicu Valcea',
                    color_discrete_sequence=px.colors.sequential.Plasma[7::-1]
                    )
fig5.show()
