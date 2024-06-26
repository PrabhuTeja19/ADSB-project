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


## Data Dictionary:
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
## Distribution Plots
![Comparision plot](https://github.com/PrabhuTeja19/ADSB-project/blob/main/Comparison%20plot.png)

#### Interpretation of gs vs tas
- **Direct Relationship**: The bar graph highlights a consistent relationship between ground speed (`gs`) and true airspeed (`tas`). Notably, as the ground speed increases, there is a corresponding increase in true airspeed, emphasizing the aircraft's capability to maintain higher speeds efficiently.

- **Speed Consistency**: A key observation from the bar graph is the absence of `tas` data below 250 knots when `gs` is below 250 knots. This pattern indicates that the aircraft consistently operates at speeds above 250 knots, with an average speed likely exceeding 300 knots. Such consistency in speed suggests optimal flight performance, potentially influenced by favorable wind conditions or strategic flight planning.

#### Interpretation of track vs nh
- **Similar Distribution**: Upon analyzing the bar graphs for track and navigation heading (nh), it is evident that both attributes exhibit a similar distribution pattern. The bars in both graphs demonstrate comparable frequencies across their respective categories, indicating consistency in the data distribution for track and nh.

- **Distinct Observation**: Notably, there is a distinct feature observed in the nh bar graph. While the majority of bars align closely with the corresponding bars in the track graph, there is a significant spike in the count value for nh when its value is North. This spike suggests a notable deviation from the typical distribution, indicating a higher frequency of occurrences where the navigation heading is reported as North.
- **Aircraft Direction Consistency**: Based on the data attributes of track and navigation heading, it can be inferred that most of the time, the aircraft moves in the direction it is pointing. The consistent distribution between track and nh suggests that the aircraft generally aligns its movement with its navigation heading, emphasizing the importance of navigation accuracy and consistency for aircraft operations.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Wind Vector Calculation and Visualization

This code snippet demonstrates a unit test to calculate and visualize the wind vector based on ground speed (`gs`) and true airspeed (`tas`) vectors. The code performs the following tasks:

1. Converts `gs` and `tas` from polar coordinates to Cartesian coordinates.
2. Calculates the wind direction and its east-west and north-south components.
3. Prints the calculated wind direction and components.
4. Visualizes the `gs`, `tas`, and resultant vectors on a plot using matplotlib.

## Python Code
 ### For Unit Test
```python
import math
from matplotlib import pyplot as plt

def polar_to_cartesian(speed, heading):
    x = speed * math.cos(math.radians(heading))
    y = speed * math.sin(math.radians(heading))
    return x, y

def get_wind_direction(x, y):
    angle_rad = math.atan2(y, x)
    angle_deg = math.degrees(angle_rad) % 360
    return angle_deg

sample_data = {'gs': 513.8, 'tas': 510, 'track': 69.7, 'nav_heading': 78.8}

gs_x, gs_y = polar_to_cartesian(400, 45)
tas_x, tas_y = polar_to_cartesian(500, 90)

dif_x = gs_x - tas_x
dif_y = gs_y - tas_y

print(gs_x, gs_y, tas_x, tas_y)
wind_direction = get_wind_direction(dif_x, dif_y)

if dif_y > 0:
    ew = 'west'
else:
    ew = 'east'

if dif_x < 0:
    ns = 'south'
else:
    ns = 'north'

print(f'{ew}ward component of the wind vector {round(abs(dif_y),3)} knots\n{ns}ward component of the wind vector {round(abs(dif_x),3)} knots')
print(f'wind direction is {wind_direction} deg')

plt.figure(figsize=(10,5))
plt.quiver(0, 0, gs_x, gs_y, angles='xy', scale_units='xy', scale=1, color='black', label='gs', width=0.005, headwidth=4, headlength=5)
plt.quiver(0, 0, tas_x, tas_y, angles='xy', scale_units='xy', scale=1, color='orange', label='tas', width=0.005, headwidth=4, headlength=5)
plt.quiver(0, 0, dif_x, dif_y, angles='xy', scale_units='xy', scale=1, color='gray', label='resultant', width=0.005, headwidth=4, headlength=5)

plt.text(900, 20, 'N', fontsize=10, color='black')
plt.text(-900, 20, 'S', fontsize=10, color='black')
plt.text(20, 900, 'W', fontsize=10, color='black')
plt.text(20, -900, 'E', fontsize=10, color='black')

plt.xlim(-1000, 1000)
plt.ylim(-1000, 1000)
plt.axhline(0, color='black', linewidth=0.05)
plt.axvline(0, color='black', linewidth=0.05)
plt.grid(visible=True, linestyle='--', alpha=0.1)
plt.legend()
plt.title(f'{ns} {round(dif_x,3)}, {ew} {round(dif_y,3)}  (in kts) | Direction {round(wind_direction,3)} deg', size=9)
plt.gca().set_aspect(aspect='equal', adjustable='box')
plt.tight_layout()
plt.show()
```
## Code Interpretation

The provided code includes functions to convert polar coordinates to Cartesian coordinates and calculate the wind direction based on the difference between two vectors representing ground speed (`gs`) and true airspeed (`tas`). It also includes a visualization using matplotlib to display the vectors and their resultant.

### Functions:

#### polar_to_cartesian(speed, heading):

- **Functionality**: 
    - Converts polar coordinates (speed and heading) to Cartesian coordinates (x, y).
- **Returns**: 
    - The x and y components of the vector.

#### get_wind_direction(x, y):

- **Functionality**: 
    - Calculates the wind direction based on the Cartesian components (x, y) of the wind vector.
- **Returns**: 
    - The wind direction in degrees.

### Code Execution:

#### Sample Data:

- `sample_data` dictionary contains sample values for ground speed (`gs`), true airspeed (`tas`), track, and navigation heading (`nav_heading`).

#### Calculations:

- `gs_x, gs_y` and `tas_x, tas_y` store the Cartesian coordinates for `gs` and `tas` vectors, respectively.
- `dif_x` and `dif_y` calculate the differences between the x and y components of the `gs` and `tas` vectors.

#### Wind Direction and Components:

- `get_wind_direction(dif_x, dif_y)` calculates the wind direction based on the difference between `gs` and `tas` vectors.
- `if` conditions determine the east-west and north-south components of the wind vector based on `dif_x` and `dif_y`.
- `print` statements display the east-west and north-south components of the wind vector, as well as the calculated wind direction.

## Output
```output
eastward component of the wind vector 217.157 knots
northward component of the wind vector 282.843 knots
wind direction is 322.4841371296373 deg
```
## Output Graph Plot

![Output Graph](https://github.com/PrabhuTeja19/ADSB-project/blob/main/Output%20of%20unit%20test%20code.png)

### Python Output Interpretation

#### Overview
The following output provides insights into the wind vector calculation based on the given ground speed (`gs`) and true airspeed (`tas`) values.
#### Calculated Values
- **Eastward Component**:  
  - Speed: 217.157 knots
  - Interpretation: The wind is pushing or blowing towards the east at a speed of 217.157 knots.
- **Northward Component**:  
  - Speed: 282.843 knots
  - Interpretation: The wind is pushing or blowing towards the north at a speed of 282.843 knots.
#### Wind Direction
- **Direction**:  
  - Angle: 322.4841371296373 degrees
  - Interpretation: The wind direction is approximately 322.484 degrees, indicating the wind is coming from the northwest, slightly west of due north.
#### Summary
The wind vector calculation suggests that the wind is predominantly pushing towards the north and east. The northward component of the wind is stronger with a speed of approximately 282.843 knots, while the eastward component has a speed of approximately 217.157 knots.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Data Aggregation for Analysis:
```python

def wind_vectors(path):
    seen = set()
    final_unique_data = []
    for file in os.listdir(path):
        c = 0
        fp = open(os.path.join(path,file), 'r')
        cols = ['tas','gs','nav_heading', 'alt_geom', 'lat', 'lon']
        for row in fp:
            row = json.loads(row)
            dto = None
            dto = datetime.datetime.strptime(row['dt'], "%Y-%m-%d %H:%M:%S.%f")
            dto = dto.date()
            dto = datetime.datetime.strftime(dto, "%Y-%m-%d")
            payload = row['payload']
            d = {}
            if isinstance(payload, dict):
                if set(cols).issubset(set(payload.keys())):
                    d['dt'] = dto
                    d['hex'] = payload['hex']
                    d['gs'] = payload['gs']
                    d['tas'] = payload['tas']
                    d['track'] = payload['track']
                    d['nav_heading'] = payload['nav_heading']
                    d['alt_geom'] = payload['alt_geom']
                    d['lat'] = payload['lat']
                    d['lon'] = payload['lon']
                    t = tuple(d.items())
                    if t not in seen:
                        final_unique_data.append(d)
                        seen.add(t)
    
    bin_5_15, bin_15_25, bin_25_35, bin_35_45 = [], [], [], []

    for d in final_unique_data:
        if d['alt_geom'] > 5000 and d['alt_geom'] <= 15000:
            bin_5_15.append(d)
        elif d['alt_geom'] > 15000 and d['alt_geom'] <= 25000:
            bin_15_25.append(d)
        elif d['alt_geom'] > 25000 and d['alt_geom'] <= 35000:
            bin_25_35.append(d)
        elif d['alt_geom'] > 35000 and d['alt_geom'] <= 45000:
            bin_35_45.append(d)
    return bin_5_15, bin_15_25, bin_25_35, bin_35_45, final_unique_data

bin_5_15, bin_15_25, bin_25_35, bin_35_45, final_unique_data = wind_vectors(path)


def agg_bins(bin, bin_name):
    keys_to_avg = ['gs', 'tas', 'track', 'nav_heading']
    sum_dict = {key: 0 for key in keys_to_avg}
    count_dict = {key: 0 for key in keys_to_avg}
    for d in bin:
        for k in keys_to_avg:
            sum_dict[k] += d.get(k, 0)
            if k in d:
                count_dict[k] += 1
    avg_dict = {k: round(sum_dict[k]/count_dict[k],4) if count_dict[k]>0 else 0 for k in keys_to_avg}
    avg_dict['bin'] = bin_name
    return avg_dict

bin_5_15_agg = agg_bins(bin_5_15, 'bin_5_15')
bin_15_25_agg = agg_bins(bin_15_25, 'bin_15_25')
bin_25_35_agg = agg_bins(bin_25_35, 'bin_25_35')
bin_35_45_agg = agg_bins(bin_35_45, 'bin_35_45')
final_agg_data = [bin_5_15_agg, bin_15_25_agg, bin_25_35_agg, bin_35_45_agg]
final_agg_data
```
# Purpose of the Code:
The code aims to process and analyze aircraft data captured through an ADS-B receiver.
### Removing Duplicates:
Initially, the code filters out duplicate data entries based on the 'Hex' and 'DT' variables. This ensures that each unique aircraft record is considered only once.
### Aggregation:
Post-duplicate removal, the data is aggregated into distinct altitude bins ranging from 5-15K, 15-25K, 25-35K, and 35-45K feet. This aggregation is performed based on the aircraft's altitude ('alt'), longitude ('lon'), and latitude ('lat').
### Averaging Payload Values:
Within each altitude bin, the code calculates the average values of 'gs' (ground speed), 'tas' (true air speed), 'nh' (navigation heading), and 'track'. This provides a consolidated representation of the payload data for each altitude bin.
### Wind Vector Calculation:
Finally, the code computes the wind vector for each aggregated data set. It does so by converting the ground speed and true air speed of each data point into Cartesian coordinates, determining the difference between them, and deriving the wind direction and speed.
### Aggregating Data into Bins:
The following segment describes the aggregation of aircraft data into specific altitude bins:
- **`agg_bins(bin, bin_name)`:** This function aggregates the provided `bin` of data and labels the resulting aggregated data with `bin_name`.
- **`bin_5_15_agg`, `bin_15_25_agg`, `bin_25_35_agg`, `bin_35_45_agg`:** These variables store the aggregated data corresponding to altitude bins of 5-15K, 15-25K, 25-35K, and 35-45K feet respectively.
- **`final_agg_data`:** This list combines all aggregated data from the distinct altitude bins.
By organizing the data in this manner, the code facilitates a structured examination of aircraft behavior across different altitude intervals. This structured approach aids in uncovering altitude-specific movement patterns and trends, offering valuable insights into aircraft navigation and wind behavior.








-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Wind Vector Visualization
```python
cax = 3
rax = round(len(final_data[:27]) / 3) + 1
fig, ax = plt.subplots(rax, cax, figsize=(20,40))
ax = ax.flatten()

def vector_plot(gs_x, gs_y, tas_x, tas_y, dif_x, dif_y, wd, i):
    ax[i].quiver(0, 0, gs_x, gs_y, angles = 'xy', scale_units = 'xy', scale = 1, color='black', label='gs', width=0.005, headwidth=4, headlength=5)
    ax[i].quiver(0, 0, tas_x, tas_y, angles = 'xy', scale_units = 'xy', scale = 1, color='orange', label='tas', width=0.005, headwidth=4, headlength=5)
    ax[i].quiver(0, 0, dif_x, dif_y, angles = 'xy', scale_units = 'xy', scale = 1, color='gray', label='resultant', width=0.005, headwidth=4, headlength=5)
    ax[i].set_xlim(-1000,1000)
    ax[i].set_ylim(-1000,1000)
    ax[i].axhline(0, color = 'black', linewidth = 0.1)
    ax[i].axvline(0, color = 'black', linewidth = 0.1)
    ax[i].grid(visible=True, linestyle = '--', alpha = 0.4)
    ax[i].legend()
    ax[i].set_title(f'{ns} {round(dif_x,3)}, {ew} {round(dif_y,3)}  (in kts) | Direction {round(wind_direction,3)} deg', size=9)
    ax[i].text(900, 20, 'N', fontsize=10, color='black')
    ax[i].text(-900, 20, 'S', fontsize=10, color='black')
    ax[i].text(20, 900, 'W', fontsize=10, color='black')
    ax[i].text(20, -900, 'E', fontsize=10, color='black')


for i, sample_data in enumerate(final_data[:27]):
    gs_x, gs_y, tas_x, tas_y, dif_x, dif_y = None, None, None, None, None, None
    gs_x, gs_y = polar_to_cartesian(sample_data['gs'], sample_data['nav_heading'])
    tas_x, tas_y = polar_to_cartesian(sample_data['tas'],  sample_data['nav_heading'])
    dif_x = gs_x - tas_x
    dif_y = gs_y - tas_y
    wind_direction = get_wind_direction(dif_x, dif_y)
    if dif_y > 0:
        ew = 'west'
    else:
        ew = 'east'

    if dif_x < 0:
        ns = 'south'
    else:
        ns = 'north'
    print(sample_data['gs'], sample_data['tas'], sample_data['nav_heading'], gs_x, gs_y, tas_x, tas_y, dif_x, dif_y)
    print(f'{ew}ward component of the wind vector {round(abs(dif_y),3)} knots\n{ns}ward component of the wind vector {round(abs(dif_x),3)} knots')
    print(f'wind direction is {wind_direction} deg\n')
    vector_plot(gs_x, gs_y, tas_x, tas_y, dif_x, dif_y, wind_direction, i)

plt.gca().set_aspect(aspect='equal', adjustable='box')
plt.tight_layout()
plt.show()
```
## Code Interpretation

The provided Python code is designed to visualize and analyze wind vectors based on ground speed (`gs`) and true airspeed (`tas`) data from the `final_data` list.

### Variables and Setup

- `cax = 3`: Specifies the number of columns in the subplot grid.
- `rax = round(len(final_data[:27]) / 3) + 1`: Determines the number of rows in the subplot grid based on the data length.
- `fig, ax = plt.subplots(rax, cax, figsize=(20,40))`: Initializes a figure with subplots based on the row and column counts.
- `ax = ax.flatten()`: Flattens the 2D array of axes into a 1D array for easier iteration.

### Functions

- `vector_plot(gs_x, gs_y, tas_x, tas_y, dif_x, dif_y, wd, i)`: A function utilized to plot vectors representing ground speed, true airspeed, and the resultant wind. This function also adds annotations, legends, and grid lines to the plots.

### Data Processing and Visualization

1. **Data Iteration**: 
   - Iterates through the first 27 data samples from `final_data`.
   - Extracts `gs`, `tas`, and `nav_heading` from each sample.
   - Calculates Cartesian coordinates for `gs` and `tas` using the `polar_to_cartesian()` function.
   - Computes the difference vectors (`dif_x` and `dif_y`).
2. **Wind Direction Calculation**:
   - Utilizes `get_wind_direction(dif_x, dif_y)` to calculate the wind direction.
   - Determines the cardinal directions (`north`, `south`, `east`, `west`) based on the sign of `dif_x` and `dif_y`.
3. **Visualization**:
   - Prints the calculated values and wind direction for each data sample.
   - Plots the vectors using the `vector_plot()` function.
   - Adds annotations, legends, and grid lines to the plots.

### Output

The output section displays:
- Cartesian coordinates for `gs` and `tas`.
- Difference vectors `dif_x` and `dif_y`.
- Wind direction in degrees.
- Eastward and northward components of the wind vector.

The code aims to visualize wind vectors for the given data samples, offering insights into the wind's direction and speed relative to the aircraft's ground speed and true airspeed. The plotted vectors aid in understanding the wind's impact on the aircraft's movement using the provided ADS-B data.

![Wind Vector Output](https://github.com/PrabhuTeja19/ADSB-project/blob/main/wind%20vector%20output.png)


# Wind Vector Visualization using Flask

## Overview

This Flask application serves as an API for generating wind vector plots based on user-selected altitude bin ranges. Leveraging aircraft data from an ADS-B receiver, the API provides an endpoint where users can specify the altitude bin range, and in response, the API computes and returns the wind vector plot corresponding to that range.

## Features

### Flask Application Setup

The code leverages the Flask framework to create a web API facilitating interaction with the wind vector prediction model.

- **Flask Initialization:**
  ```python
  app = Flask(__name__, static_url_path='')
  ```

  -**Static File Serving:**
  ```python
  @app.route('/static/<path:path>')
  def send_static(path):
      return send_from_directory('static', path)
  ```
### Flask Routes and Endpoints

#### Default Route

- **'/' - binning():**
  ```python
  @app.route('/')
  def binning():
      return render_template('test.html')
  #Renders the 'test.html' template when the root URL is accessed.
  
  ```

### Endpoints for Model Interaction
- **'/plotvector' - plotvector():**
  ```python
  @app.route('/plotvector')
  def plotvector():
      bin = request.args.get('bin')
      ...
   ```
Endpoint for visualizing wind vectors based on specific altitude bins. Accepts altitude bin as a query parameter.

* Running on http://127.0.0.2:5000
  - The web page will load with a dropdown menu prompting the user to select a bin range.
  - A search bar labeled "Show Chart" is available.
  - After selecting the bin range and clicking "Show Chart," the wind vector plot will be displayed.

This is the final output plot of wind direction vector. The graph plot showcases the ground speed vector, true air speed vector, and wind vector.

![Wind Vector Plot](https://github.com/PrabhuTeja19/ADSB-project/raw/main/final%20outputplot.png)
--

## Final Interface

Here's the final interface created using Flask:

![Final Interface](https://github.com/PrabhuTeja19/ADSB-project/raw/main/Final_interface.jpg)










