# Reflection Tree Diagram

```mermaid
flowchart TD
    START --> A1_OPEN

    %% Axis 1
    A1_OPEN -->|Productive/Mixed| A1_Q_AGENCY_HIGH
    A1_OPEN -->|Tough/Frustrating| A1_Q_AGENCY_LOW

    A1_Q_AGENCY_HIGH --> A1_R_INT
    A1_Q_AGENCY_LOW --> A1_R_EXT

    A1_R_INT --> BRIDGE_1_2
    A1_R_EXT --> BRIDGE_1_2

    %% Axis 2
    BRIDGE_1_2 --> A2_OPEN
    A2_OPEN -->|Helped/Taught| A2_R_CONTRIBUTION
    A2_OPEN -->|Needed/Overlooked| A2_R_ENTITLEMENT

    A2_R_CONTRIBUTION --> BRIDGE_2_3
    A2_R_ENTITLEMENT --> BRIDGE_2_3

    %% Axis 3
    BRIDGE_2_3 --> A3_OPEN
    A3_OPEN -->|Just me| A3_R_SELF
    A3_OPEN -->|Team/Colleague/Customer| A3_R_ALTRO

    A3_R_SELF --> SUMMARY
    A3_R_ALTRO --> SUMMARY

    SUMMARY --> END
