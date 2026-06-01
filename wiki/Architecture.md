# RiverProject Architecture

This page describes the overall system architecture of the River Project.

## System Overview

The River Project follows a distributed architecture with three main components:

```
┌─────────────────────────────────────────────────────────────┐
│                      Raspberry Pi                           │
│                  (Collect Array Program)                    │
│              ┌──────────────────────────┐                   │
│              │   Sense Hat Sensors      │                   │
│              │  (Environmental Data)    │                   │
│              └──────────────┬───────────┘                   │
│                             │                               │
│            Data Processing & Rolling Averages               │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      │ JSON over MQTT
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                    MQTT Broker                              │
│              (Message Distribution Hub)                     │
└──────────────────────┬──────────────────────────────────────┘
                       │
        ┌──────────────┴──────────────┐
        │                             │
        ▼                             ▼
┌──────────────────┐      ┌──────────────────────┐
│   Node-RED       │      │  Data Logging        │
│  Dashboard       │      │  Storage             │
│ (Visualization)  │      │  (Database/Files)    │
└──────────────────┘      └──────────────────────┘
```

## Component Details

### 1. Raspberry Pi - Collect Array Program

**Purpose:** Data collection and preprocessing

**Features:**
- Reads environmental data from Sense Hat sensors
- Calculates rolling averages for data smoothing
- Publishes data as JSON messages via MQTT
- Runs continuously to ensure consistent data collection

**Technologies:**
- Python 3
- Raspberry Pi Sense Hat library
- Deque (for rolling average calculations)

### 2. MQTT Broker

**Purpose:** Central message distribution hub

**Responsibilities:**
- Receives sensor data from Raspberry Pi
- Routes messages to subscribers
- Handles pub/sub communication
- Manages message persistence (optional)

**Configuration:**
- Default port: 1883
- Topics: Configurable based on sensor types

### 3. Node-RED Dashboard

**Purpose:** Real-time data visualization and event logging

**Features:**
- Visual representation of sensor data
- Event logging interface for field observations
- Real-time data updates via MQTT subscription
- User-friendly dashboard for monitoring

### 4. Data Analysis Component

**Purpose:** Historical data processing and analysis

**Features:**
- Stores collected sensor data
- Performs statistical analysis
- Generates reports and insights
- Supports trend analysis

## Data Flow

1. **Data Collection** → Sense Hat sensors collect environmental measurements
2. **Processing** → Collect Array program calculates rolling averages
3. **Transmission** → Data published to MQTT broker in JSON format
4. **Distribution** → MQTT broker routes data to subscribers
5. **Visualization** → Node-RED displays data in dashboard
6. **Logging** → Events and observations recorded in data store
7. **Analysis** → Historical data analyzed for patterns and insights

## Key Design Principles

- **Modularity** - Components can operate independently
- **Real-time Processing** - Minimal latency in data transmission
- **Scalability** - Easy to add additional sensors or data consumers
- **Reliability** - Continuous operation and data persistence
- **Open Standards** - Uses MQTT and JSON for interoperability

## Technologies Stack

| Component | Technology |
|-----------|-----------|
| Language | Python 3 |
| Hardware | Raspberry Pi |
| Sensors | Sense Hat |
| Messaging | MQTT |
| Dashboard | Node-RED |
| Data Format | JSON |

## Next Steps

- Review [[Hardware Setup]] for sensor configuration
- Explore [[Software Components]] for detailed code documentation
- Check [[Data Collection]] to understand the Collect Array program