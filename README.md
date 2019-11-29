# PIVPy app based on Streamlit.io

PIVPy helps to understand PIV data, inspired by PIVMAT. see http://pivpy.readthedocs.io and get it from http://github.com/alexlib/pivpy

Streamlit is the fastest app building package for machine learning, see http://streamlit.io

## Why the app?

We could write a full desktop PyQt5 GUI, like we did for `openpiv` and other packages, but it would take too long. With `streamlit` it was ready in 10 min

## How to run? 

    pip install streamlit pivpy --upgrade
    streamlit run https://raw.githubusercontent.com/alexlib/pivpy_streamlit_app/master/app.py
