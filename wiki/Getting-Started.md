# Getting Started with RiverProject

This guide will help you set up and run the River Project on your system.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- Raspberry Pi (with Sense Hat attached)
- Node-RED
- MQTT Broker (e.g., Mosquitto)
- Git

## Installation Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/cuthbert86/RiverProject.git
   cd RiverProject
   ```

2. **Install Python Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up MQTT Broker**
   - Install and configure your MQTT broker
   - Default configuration uses localhost on port 1883

4. **Configure Node-RED**
   - Start Node-RED and create a flow
   - Set up MQTT subscription node to receive data from the Raspberry Pi
   - Configure the data dashboard

5. **Deploy to Raspberry Pi**
   - Copy the Collect Array program to your Raspberry Pi
   - Ensure the Sense Hat is properly connected
   - Run the data collection script

## Running the Project

Once everything is set up:

1. Start the MQTT broker
2. Run the Collect Array program on the Raspberry Pi
3. Start Node-RED and your dashboard
4. Monitor data in real-time through the Node-RED interface

## Next Steps

- Explore the [[Architecture]] page to understand the system design
- Check [[Hardware Setup]] for detailed configuration
- Review [[Software Components]] for code documentation

## Troubleshooting

If you encounter issues, please refer to the [[Troubleshooting]] page for common solutions.