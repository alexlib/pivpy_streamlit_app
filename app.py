import streamlit as st
import pathlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pkg_resources


data_path = pathlib.Path(pkg_resources.resource_filename('pivpy','data'))

# st.title('My first app')

# st.write("Here's our first attempt at using data to create a table:")
# st.write(pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
# }))

"""
# Streamlit app for PIVPy
Here's our first attempt at using streamlit to work with PIV output:
"""

# df = pd.DataFrame({
#   'first column': [1, 2, 3, 4],
#   'second column': [10, 20, 30, 40]
# })

# df

# chart_data = pd.DataFrame(
#      np.random.randn(20, 3),
#      columns=['a', 'b', 'c'])

# st.line_chart(chart_data)

from pivpy import pivpy, io, graphics
import time

def main():

    data_selectbox = st.sidebar.selectbox(
        'Which dataset?',
        ('Demo', 'Jet', 'PIV Challenge'))

    streamlines = st.sidebar.checkbox('Streamlines?',value = False)

    colorbar = st.sidebar.checkbox('Color bar?',value=False)

    average = st.sidebar.checkbox('Average?',value=False)


    st.subheader('Create data set')

    """
    `data = io.create_sample_Dataset()`

    """




    st.subheader('Present data as Pandas DataFrame')

    """
    `data.to_dataframe()`
    """

    data = load_data(data_selectbox)
    st.write(data.to_dataframe())

    st.subheader('Plot some vector fields using matpotlib quiver')

    """
    ` graphics.quiver(data.isel(t=0)`
    """



    # progress_bar = st.progress(0)
    # status_text = st.empty()
    # chart = st.line_chart(np.random.randn(10, 2))

    # for i in range(len(data)):
    #     # Update progress bar.
    #     progress_bar.progress(i)

    #     new_rows = np.random.randn(10, 2)

    #     # Update status text.
    #     status_text.text(
    #         'The latest random number is: %s' % new_rows[-1, 1])

    #     # Append data to the chart.
    #     # chart.add_rows(new_rows)
    #     graphics.quiver(data.isel(t=i))
    #     st.pyplot()

    #     # Pretend we're doing some computation that takes time.
    #     time.sleep(1)

    # status_text.text('Done!')
    # st.balloons()




    # fig, ax = plt.subplots()
    if average:
        fig, ax = graphics.quiver(data.piv.average,streamlines=streamlines,colbar=colorbar,colbar_orient='vertical')
    else:
        t = st.selectbox('Frame number',range(len(data.t)))
        fig, ax = graphics.quiver(
            data.isel(t=t), 
            streamlines=streamlines, 
            colorbar=colorbar,
            colorbar_orient='vertical'
        )


    the_plot = st.pyplot(plt)

    from execbox import execbox


    # Draw a text editor and a "Run" button. When you press "Run", the code in the editor executes!
    execbox()


    # Makes the code run automatically on each keystroke.
    # execbox(autorun=True, key='pivpy_execbox')


    # Draw an execbox with some initial text.
    execbox("""
    a = 10
    b = 20
    st.write(a + b)
    """)



    # max_x = 5
    # max_rand = 10

    # x = np.arange(0, max_x)
    # ax.set_ylim(0, max_rand)
    # line, = ax.plot(x, np.random.randint(0, max_rand, max_x))
    # the_plot = st.pyplot(plt)

    # def init():  # give a clean slate to start
    #     line.set_ydata([np.nan] * len(x))

    # def animate(i):  # update the y values (every 1000ms)
    #     ax.set_ydata(np.random.randint(0, max_rand, max_x))
        
    #     the_plot.pyplot(plt)

    # init()
    # for i in range(100):
    #     animate(i)
    #     time.sleep(0.1)

@st.cache(allow_output_mutation=True)
def load_data(data_selectbox='Demo'):
    """ loads data """
    if data_selectbox == 'Demo':
        data = io.create_sample_Dataset()
    elif data_selectbox == 'Jet':
        data = io.load_directory((data_path / "Insight"),basename='Run*',ext='.vec')
    # elif data_selectbox == 'Canopy':
    #     data = io.load_directory(data_path / "urban_canopy" ,ext='.vc7')
    elif data_selectbox == 'PIV Challenge':
        data = io.load_directory ( ( data_path / "PIV_Challenge"), ext='.txt')


    return data


if __name__ == "__main__":
    main()
    
