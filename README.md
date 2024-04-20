# ADSB-project

# Identifying the prevailing wind speed and direction influencing the aircraft from Automatic Dependent Surveillance–Broadcast Data.

--------------------------------------------------------------------------------------------------------------------------------------
## What is ADSB?
### Automatic Dependent Surveillance–Broadcast (ADS-B) is an aviation surveillance technology and form of Electronic Conspicuity in which an aircraft (or other airborne vehicles such as drones approved to fit "ADS-B Out") determines its position via satellite navigation or other sensors and periodically broadcasts its position and other related data, enabling it to be tracked.
#### ADS-B enables improved safety by providing:
- Radar-like IFR separation in non-radar airspace
- Increased VFR flight following coverage
- ATC final approach and runway occupancy, reducing runway incursions on the ground
- More accurate search and rescue response
- Although ADS-B can transmit "aircraft down" data, the FAA has stated that there is no intention to perform even a study of ADS-B's effectiveness in an "aircraft down" situation, simply based on the fact that ADS-B equipment has no requirement to be crashworthy, as compared to the current "black box" recorder. 
- ADS-B was demonstrated to the Civil Air Patrol (CAP) in March 2003 by AOPA via flight demonstrations for possible integration of the technology in CAP activities.
- Helps pilots to see and avoid other aircraft
- Cockpit final approach and runway occupancy
- Visual separation in VFR and MVFR conditions
- VFR-like separation in all weather conditions
- Real-time cockpit weather display
- Real-time cockpit airspace display
-------------------------------------------------------------------------------------------------------------------------------------

# ADS-B (Automatic Dependent Surveillance–Broadcast) Overview

## Description

ADS-B, or Automatic Dependent Surveillance–Broadcast, is a revolutionary surveillance technology transforming the aviation industry. By utilizing onboard satellite navigation systems, ADS-B enables aircraft to accurately determine their position and broadcast this information at regular intervals to ground stations and nearby aircraft.

### Key Features and Benefits

- **Radar-like IFR Separation in Non-radar Airspace**: Enables safe separation in areas with limited or no traditional radar coverage, enhancing safety in non-radar airspace.
  
- **Increased VFR Flight Following Coverage**: Enhances tracking and situational awareness for Visual Flight Rules (VFR) operations, improving flight following services.
  
- **ATC Final Approach and Runway Occupancy**: Provides precise tracking during critical flight phases, reducing runway incursions and enhancing ground safety.
  
- **Accurate Search and Rescue Response**: Facilitates quicker and more precise search and rescue operations by transmitting exact aircraft position and status during emergencies.
  
- **Collision Avoidance**: Assists pilots and Air Traffic Control (ATC) in detecting and avoiding potential collision risks through real-time position and velocity data.

- **Real-time Weather and Airspace Display**: Delivers real-time weather updates and airspace information directly to the cockpit, aiding in informed decision-making.

--------------------------------------------------------------------------------------------------------------------------------------------------------

## The Dataset:
![ADS-B Image](https://github.com/PrabhuTeja19/ADSB-project/raw/main/Screenshot%202024-04-20%20134502.png)


## Dataset Dictionary:
### Key Attributes

- **gs**: Ground speed (GS) refers to the speed of the aircraft relative to the ground, measured in knots.
- **tas**: True airspeed (TAS) is the speed of the aircraft relative to the surrounding air mass, adjusted for altitude and temperature, measured in knots.
- **track**: Track is the direction in which the aircraft is actually moving over the ground, measured in degrees from 0 to 359, where 0 degrees represents north.
- **nav_heading**: Navigation heading (NAV heading) is the selected heading of the aircraft, either in true or magnetic north, depending on the equipment and settings, measured in degrees.
- **alt_geom**: Geometric altitude (ALT geom) is the altitude of the aircraft above the WGS84 ellipsoid, measured in feet.
- **lat, lon**: Latitude and longitude represent the geographic coordinates of the aircraft's position on the Earth's surface, measured in decimal degrees.

### Additional Information

- **gs**: Ground speed is influenced by factors such as wind speed and direction, and it is important for determining the estimated time of arrival and fuel consumption.
- **tas**: True airspeed is crucial for aircraft performance, as it affects lift, drag, and fuel efficiency. It is used for calculating true ground speed and navigation.
- **track**: Track provides the actual direction of the aircraft's movement over the ground and is essential for navigation and traffic separation.
- **nav_heading**: Navigation heading indicates the intended direction of travel set by the pilot or autopilot system and is used for navigation and route planning.
- **alt_geom**: Geometric altitude is the actual altitude above the Earth's surface and is used for terrain clearance and vertical navigation.
- **lat, lon**: Latitude and longitude coordinates pinpoint the exact location of the aircraft on the Earth's surface and are essential for navigation, tracking, and route planning.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Comparison Plots
![Comparision plot](https://github.com/PrabhuTeja19/ADSB-project/blob/main/Comparison%20plot.png)

#### Interpretation of gs vs tas
- **Direct Relationship**: The bar graph highlights a consistent relationship between ground speed (`gs`) and true airspeed (`tas`). Notably, as the ground speed increases, there is a corresponding increase in true airspeed, emphasizing the aircraft's capability to maintain higher speeds efficiently.

- **Speed Consistency**: A key observation from the bar graph is the absence of `tas` data below 250 knots when `gs` is below 250 knots. This pattern indicates that the aircraft consistently operates at speeds above 250 knots, with an average speed likely exceeding 300 knots. Such consistency in speed suggests optimal flight performance, potentially influenced by favorable wind conditions or strategic flight planning.

#### Interpretation of track vs nh

- **Similar Distribution**: Upon analyzing the bar graphs for track and navigation heading (nh), it is evident that both attributes exhibit a similar distribution pattern. The bars in both graphs demonstrate comparable frequencies across their respective categories, indicating consistency in the data distribution for track and nh.

- **Distinct Observation**: Notably, there is a distinct feature observed in the nh bar graph. While the majority of bars align closely with the corresponding bars in the track graph, there is a significant spike in the count value for nh when its value is 0. This spike suggests a notable deviation from the typical distribution, indicating a higher frequency of occurrences where the navigation heading is reported as 0.








