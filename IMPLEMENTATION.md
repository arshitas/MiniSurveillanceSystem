## Implementation

#### a) Arduino

The components used are:
1. Arduino Uno board with Atmega328P microcontroller
2. Plastic case BO motor [Similar component](https://sproboticworks.com/shop/products/plastic-gear-motor-with-pcb.html)
3. IR sensor [Similar component](https://robu.in/product/waveshare-infrared-proximity-sensor-obstacle-avoiding/)

Components are connected as shown in Design.vbb 

Loading the surveillance_arduino.ino program for IR sensor to transmit values serially (In my system it was COM3)

#### b) Python
To interface python with arduino via serial USB connection, we will be using `Pyserial`. The IR sensor values are displayed as a polar plot using `Plotly` and the web dashboard is created using `Streamlit`

Once the system is installed with the above libraries, surveillance_python.py code is implemented to create the dashboard. 
