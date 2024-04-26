
import json
import os, datetime
from re import L
import seaborn as sns
import matplotlib.pyplot as plt
import math
import warnings
import numpy as np
from flask import Flask
from flask import request, session, redirect, send_from_directory, make_response, render_template

warnings.filterwarnings('ignore')

app = Flask(__name__, static_url_path='')


@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)
  

path = 'ADSB_data'

# def dist(path):
#     final_data = []
#     gs_l, tas_l, track_l, nh_l = [], [], [], []
#     cols = ['tas','gs','nav_heading', 'alt_geom', 'lat', 'lon']
#     for file in os.listdir(path):
#         c = 0
#         fp = open(os.path.join(path,file), 'r')
#         for row in fp:
#             # print(row)
#             row = json.loads(row)
#             payload = row['payload']
#             if isinstance(payload, dict):
#                 if set(cols).issubset(set(payload.keys())):
#                     gs_l.append(payload['gs'])
#                     tas_l.append(payload['tas'])
#                     track_l.append(payload['track'])
#                     nh_l.append(payload['nav_heading'])
#                     d = {}
#                     d['gs'] = payload['gs']
#                     d['tas'] = payload['tas']
#                     d['track'] = payload['track']
#                     d['nav_heading'] = payload['nav_heading']
#                     d['alt_geom'] = payload['alt_geom']
#                     d['lat'] = payload['lat']
#                     d['lon'] = payload['lon']
#                     final_data.append(d)
#                     c+=1
#     return final_data, gs_l, tas_l, track_l, nh_l

# dist(path)        

def wind_vectors(path):
    seen = set()
    final_unique_data = []
    for file in os.listdir(path):
        # print("this file is good: ", file)
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


def polar_to_cartesian(speed, heading):
    x = speed * math.cos(math.radians(heading))
    y = speed * math.sin(math.radians(heading))
    return x, y

def get_wind_direction(x, y):
    angle_rad = math.atan2(y, x)
    angle_deg = math.degrees(angle_rad) % 360
    return angle_deg


def getvector(sample_data):
    gs_x, gs_y, tas_x, tas_y, dif_x, dif_y = None, None, None, None, None, None
    gs_x, gs_y = polar_to_cartesian(sample_data['gs'], sample_data['nav_heading'])
    tas_x, tas_y = polar_to_cartesian(sample_data['tas'],  sample_data['nav_heading'])
    
    # Below 2 lines for Unit test 
    # gs_x, gs_y = polar_to_cartesian(400, 45)
    # tas_x, tas_y = polar_to_cartesian(500, 90)
    
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
    print(sample_data)
    print(gs_x, gs_y, tas_x, tas_y, dif_x, dif_y)
    
    print(f'{ew}ward component of the wind vector {round(abs(dif_y), 3)} knots\n{ns}ward component of the wind vector {round(abs(dif_x), 3)} knots')
    print(f'wind direction is {wind_direction} deg\n')
    return ew, ns, gs_x, gs_y, tas_x, tas_y, dif_x, dif_y, wind_direction, sample_data


@app.route('/')
def binning():
    return render_template('test.html')


@app.route('/plotvector')
def plotvector():
    bin = request.args.get('bin')
    if not bin is None:
        if bin == '1':
            ew, ns, gs_x, gs_y, tas_x, tas_y, dif_x, dif_y, wind_direction, sample_data = getvector(final_agg_data[0])
            alt = 15000
        if bin == '2':
            ew, ns, gs_x, gs_y, tas_x, tas_y, dif_x, dif_y, wind_direction, sample_data = getvector(final_agg_data[1])
            alt = 25000
        if bin == '3':
            ew, ns, gs_x, gs_y, tas_x, tas_y, dif_x, dif_y, wind_direction, sample_data = getvector(final_agg_data[2])
            alt = 35000
        if bin == '4':
            ew, ns, gs_x, gs_y, tas_x, tas_y, dif_x, dif_y, wind_direction, sample_data = getvector(final_agg_data[3])
            alt = 45000
            # msg1 = f'You have selected {bin_name}K altitude'
            # msg2 = f'{ew}ward component of the wind vector {round(abs(dif_y),3)} knots'
            # msg3 = f'{ns}ward component of the wind vector {round(abs(dif_x),3)} knots'
            # wd = f'wind direction is {wind_direction} deg'
            # 282.842712474619 282.84271247461896 3.061616997868383e-14 500.0 282.84271247461896 -217.15728752538104
    
    ### unit test
    # sd = {'gs': 400, 'tas': 500, 'track': 69.7, 'nav_heading': 78.8}
    # ew, ns, gs_x, gs_y, tas_x, tas_y, dif_x, dif_y, wind_direction, sample_data = getvector(sd)
    # alt = 45000 
    ## unit test ends

    ew_speed = round(abs(dif_y), 3) 
    ns_speed = round(abs(dif_x), 3)

    return render_template('chart.html', gs_x=gs_x, gs_y=gs_y, tas_x=tas_x, tas_y=tas_y, dif_x=dif_x, dif_y=dif_y, wind_direction=round(wind_direction, 2), data = sample_data, ew=ew, ns=ns, alt=alt, ew_speed=ew_speed, ns_speed=ns_speed)


if __name__ == '__main__':
    app.run(host=os.getenv('HOSTIP', '127.0.0.1'), debug=os.getenv('FLASKDEBUG', True), port = os.getenv('PORT', '5000'))
