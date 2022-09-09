from array import array
import pandas as pd 
import numpy as np
import pickle
import json
import config   

class  model_price_range() :

    def __init__(self, battery_power, blue, clock_speed, dual_sim, fc, four_g, int_memory, m_dep, mobile_wt, n_cores, pc, px_height,px_width, ram, sc_h, sc_w, talk_time, three_g, touch_screen, wifi ) :

        self.battery_power = battery_power
        self.blue = blue
        self.clock_speed =clock_speed
        self.dual_sim =dual_sim
        self.fc = fc
        self.four_g =four_g
        self.int_memory = int_memory
        self.m_dep = m_dep
        self.mobile_wt = mobile_wt
        self.n_cores = n_cores
        self.pc =pc
        self.px_height = px_height
        self.px_width = px_width
        self.ram = ram
        self.sc_h = sc_h
        self.sc_w = sc_w
        self.talk_time = talk_time
        self.three_g = three_g
        self.touch_screen = touch_screen
        self.wifi = wifi

    def load_model(self) :
        with open(config.MODEL_FILE_PATH, 'rb') as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH, 'r') as f:
            self.json_data = json.load(f)


    def mobile_price_prediction(self) :
        test_array = np.zeros(20)

        test_array[0] = self.battery_power
        test_array[1] = self.blue
        test_array[2] = self.clock_speed
        test_array[3] = self.dual_sim
        test_array[4] = self.fc
        test_array[5] = self.four_g
        test_array[6] = self.int_memory
        test_array[7] = self.m_dep
        test_array[8] = self.mobile_wt
        test_array[9] = self.n_cores
        test_array[10] = self.pc
        test_array[11] = self.px_height
        test_array[12] = self.px_width
        test_array[13] = self.ram
        test_array[14] = self.sc_h
        test_array[15] = self.sc_w
        test_array[16] = self.talk_time
        test_array[17] = self.three_g
        test_array[18] = self.touch_screen
        test_array[19] = self.wifi

        predicted_range = self.model.predict

        return predicted_range
 