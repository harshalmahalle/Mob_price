import re
import config
from flask import Flask, jsonify, render_template, redirect, request, url_for 
import numpy as np
from Project_app.Utils import model_price_range

app = Flask(__name__)

@app.route('/')
def home_flask():

    return render_template('login.html')

@app.route('/predicted_price',methods= ['POST','GET'])

def predicted_price():
    if request.method == 'POST' :
        data = request.form

        battery_power = eval(data['battery_power'])
        blue = eval(data['blue'])
        clock_speed = eval(data['clock_speed'])
        dual_sim = eval(data['dual_sim'])
        fc= eval(data['fc'])
        four_g= eval(data['four_g'])
        int_memory = eval(data['int_memory'])
        m_dep= eval(data['m_dep'])
        mobile_wt = eval(data['mobile_wt'])
        n_cores = eval(data['n_cores'])
        pc = eval(data['pc'])
        px_height= eval(data['px_height'])
        px_width = eval(data['px_width'])
        ram= eval(data['ram'])
        sc_h = eval(data['sc_h'])
        sc_w= eval(data['sc_w'])
        talk_time = eval(data['talk_time'])
        three_g = eval(data['three_g'])
        touch_screen= eval(data['touch_screen'])
        wifi= eval(data['wifi'])


        obj = model_price_range (battery_power, blue, clock_speed, dual_sim, fc, four_g, int_memory, m_dep, mobile_wt, n_cores, pc, px_height,px_width, ram, sc_h, sc_w, talk_time, three_g, touch_screen, wifi )
        prediction = obj.mobile_price_prediction()
        
        return jsonify({'predicted price range ' : prediction})

    else :

        battery_power = eval(request.args.get('battery_power'))
        blue = eval(request.args.get('blue'))
        clock_speed = eval(request.args.get('clock_speed'))
        dual_sim = eval(request.args.get('dual_sim'))
        fc= eval(request.args.get9('fc'))
        four_g= eval(request.args.get('four_g'))
        int_memory = eval(request.args.get('int_memory'))
        m_dep= eval(request.args.get['m_dep'])
        mobile_wt = eval(request.args.get('mobile_wt'))
        n_cores = eval(request.args.get('n_cores'))
        pc = eval(request.args.ge('pc'))
        px_height= eval(request.args.get('px_height'))
        px_width = eval(request.args.get('px_width'))
        ram= eval(request.args.get('ram'))
        sc_w= eval(request.args.get('sc_w'))
        talk_time = eval(request.args.get('talk_time'))
        three_g = eval(request.args.get('three_g'))
        touch_screen= eval(request.args.get('touch_screen'))
        wifi= eval(request.args.get('wifi')) 



        obj = model_price_range (battery_power, blue, clock_speed, dual_sim, fc, four_g, int_memory, m_dep, mobile_wt, n_cores, pc, px_height,px_width, ram, sc_h, sc_w, talk_time, three_g, touch_screen, wifi )
        prediction = obj.mobile_price_prediction()
        
        return jsonify({'predicted price range ' : prediction})

if __name__ == '__main__'  :
    app.run(host = "0.0.0.0", port = config.PORT_NUMBER,debug=False)
 
