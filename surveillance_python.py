import serial
import streamlit as st
import plotly.graph_objects as go
import time

arduino = serial.Serial(port='COM3', baudrate=4800, parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS) 

st.sidebar.title('Mini Surveillance System')
info_bar = st.empty()
info_1 = st.empty()
info_2 = st.empty()
radar_placeholder = st.empty()

r = [0]*90

theta = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34,
36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70,72,
74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104,106, 108,
110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132,134, 136, 138,
140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160,162, 164, 166, 168,
170, 172, 174, 176, 178]

def radar_gauge(val,pos,placeholder):
    fig = go.Figure()
    pos= int(int(pos)/2)
    r[pos] = val

    fig.add_trace(go.Scatterpolar(
          r=r,
          theta=theta,
          mode='lines'
    ))

    r2 = [0]*90
    r2[pos] = 5
    fig.add_trace(go.Scatterpolar(
          r=r2,
          theta=theta,
          mode='lines'
    ))

    fig.update_layout(
      polar=dict(
        radialaxis=dict(
          visible=True,
          range=[0, 5]
        ),
      ),
      showlegend=False
    )
    placeholder.write(fig)

if st.sidebar.button('Start system'):
    info_bar.info('System started')

    try:
        arduino.open()
    except:
        pass

    if st.sidebar.button('Stop system'):
        info_bar.warning('System stopped')
        try:
            arduino.close()
        except:
            pass

    while True:
        arduino.flushInput()
        arduino.flushOutput()
        arduino.flush()
        try:
            val = arduino.readline().decode().strip('\r\n').split('*')[1]
        except:
            val = 0
        pos = arduino.readline().decode().strip('\r\n').split('*')[0]
        info_1.info(('Value (V) = **%s**' % (val)))
        info_2.info(('Position (°) = **%s**' % (pos)))
        radar_gauge(val,pos,radar_placeholder)
        time.sleep(0.05)

info_bar.warning('System stopped')

try:
    arduino.close()
except:
    pass
