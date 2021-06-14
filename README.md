# Mini Surveillance System
Be it home or business, surveillance systems have become an essential part of security. The system is designed to easily fit in closed spaces to detect intruders and presents visuals on your computer screen. 
The embedded system is designed with Arduino Uno board with Atmega328P microcontroller. The IR sensor value and angle is serially transmitted which is retrieved by the python program to present on the web dashboard.

### Features
1. Live dashboard
2. Range: Upto 20cm
3. Battery operated system
4. Miniature system : 7cm x 6 cm area

### Hardware Components
1. Arduino Uno board (Atmega 328P 8-bit microcontroller)
2. IR sensor
3. Plastic case BO motor

### Circuit design
![Circuit design](https://github.com/arshitas/MiniSurveillanceSystem/blob/main/Circuit%20design.png)

### Python libraries
1. **Pyserial** : Enables the access of serial ports through python properties
2. **Streamlit** : Open-source python library to develop custom webpages 
3. **Plotly** : Graphing library offers wide range of charts to make interactive, publication quality graphs.   

#### Refernces
1. This work is inspired from M Khosarani's blend of [arduino and python](https://towardsdatascience.com/build-a-diy-mini-radar-using-arduino-python-and-streamlit-12a368ae03a4)
2. [Streamlit documentation](https://docs.streamlit.io/en/stable/index.html)
3. Plotly's python graphing library [API reference](https://plotly.com/python-api-reference/index.html)
