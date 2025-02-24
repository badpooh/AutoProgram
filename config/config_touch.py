from enum import Enum

class ConfigTouch(Enum):
    ### 상단 메뉴 ###
    touch_main_menu_1 = [100, 85]
    touch_main_menu_2 = [260, 85]
    touch_main_menu_3 = [390, 85]
    touch_main_menu_4 = [560, 85]
    touch_main_menu_5 = [720, 85]
    
	### 왼쪽 사이드 메뉴 ###
    touch_side_menu_1 = [80, 135]
    touch_side_menu_2 = [80, 180]
    touch_side_menu_3 = [80, 225]
    touch_side_menu_4 = [80, 270]
    touch_side_menu_5 = [80, 315]
    touch_side_menu_6 = [80, 360]
    touch_side_menu_7 = [80, 405]
    touch_side_menu_8 = [80, 450]

    touch_data_view_1 = [320, 210]
    touch_data_view_2 = [620, 210]
    touch_data_view_3 = [320, 280]
    touch_data_view_4 = [620, 280]
    touch_data_view_5 = [320, 360]
    touch_data_view_6 = [620, 360]
    touch_data_view_7 = [320, 430]
    touch_data_view_8 = [620, 430]

    touch_toggle_ll = [410, 150]
    touch_toggle_ln = [510, 150]
    touch_toggle_thd_ll = [520, 150]
    touch_toggle_thd_ln = [620, 150]
    touch_toggle_max = [720, 150]
    touch_toggle_min = [620, 150]
    touch_toggle_phasor_vll = [620, 210]
    touch_toggle_phasor_vln = [720, 210]
    
	### phasor, harmonics, waveform 공통 ###
    touch_toggle_analysis_vol = [590, 150]
    touch_toggle_analysis_curr = [720, 150]
    
    touch_toggle_harmonics_fund = [510, 200]
    touch_dropdown_harmonics_1 = [230, 200]
    touch_dropdown_harmonics_2 = [360, 200]
    touch_toggle_waveform_vol_a = [360, 200]
    touch_toggle_waveform_vol_b = [430, 200]
    touch_toggle_waveform_vol_c = [490, 200]
    
	### harmonics a,b,c 와 공통 ###
    touch_toggle_waveform_curr_a = [620, 200]
    touch_toggle_waveform_curr_b = [680, 200]
    touch_toggle_waveform_curr_c = [740, 200]
    
	### harmonics dropdown menu의 선택지 ###
    touch_harmonics_sub_v = [230, 240]
    touch_harmonics_sub_fund = [230, 285]
    touch_harmonics_sub_rms = [230, 330]
    touch_harmonics_sub_graph = [360, 240]
    touch_harmonics_sub_text = [360, 285]

    ### popup button ####
    touch_btn_popup_enter = [340, 415],
    touch_btn_popup_cancel = [450, 430],
    
    ### touch 동작관련 address ###
    touch_addr_ui_test_mode = 57100
    touch_addr_pos_x = 57110
    touch_addr_pos_y = 57111
    touch_addr_touch_mode = 57112
    touch_addr_screen_capture = 57101
    touch_addr_setup_button_bit = 57120
    touch_addr_setup_button = 57121

class ConfigTouch123(Enum):
    touch_main_menu_1 = [100, 85]
    touch_main_menu_2 = [260, 85]
    touch_main_menu_3 = [390, 85]
    touch_main_menu_4 = [560, 85]
    touch_main_menu_5 = [720, 85]
    touch_side_menu_1 = [80, 135]
    touch_side_menu_2 = [80, 180]
    touch_side_menu_3 = [80, 225]
    touch_side_menu_4 = [80, 270]
    touch_side_menu_5 = [80, 315]
    touch_side_menu_6 = [80, 360]
    touch_side_menu_7 = [80, 405]
    touch_side_menu_8 = [80, 450]

    touch_meas_ll = [410, 150]
    touch_meas_ln = [510, 150]
    touch_thd_ll = [520, 150]
    touch_thd_ln = [620, 150]
    touch_max = [720, 150]
    touch_min = [620, 150]
    touch_phasor_vll = [620, 210]
    touch_phasor_vln = [720, 210]
    touch_analysis_vol = [590, 150]
    touch_analysis_curr = [720, 150]
    touch_harmonics_fund = [510, 200]
    touch_harmonics_submenu_1 = [230, 200]
    touch_harmonics_submenu_2 = [360, 200]
    touch_wave_curr_a = [620, 200]
    touch_wave_curr_b = [680, 200]
    touch_wave_curr_c = [740, 200]
    touch_wave_vol_a = [360, 200]
    touch_wave_vol_b = [430, 200]
    touch_wave_vol_c = [490, 200]
    touch_harmonics_sub_v = [230, 240]
    touch_harmonics_sub_fund = [230, 285]
    touch_harmonics_sub_rms = [230, 330]
    touch_harmonics_sub_graph = [360, 240]
    touch_harmonics_sub_text = [360, 285]
    
    #touch_address
    touch_addr_ui_test_mode = 57100
    touch_addr_pos_x = 57110
    touch_addr_pos_y = 57111
    touch_addr_touch_mode = 57112
    touch_addr_screen_capture = 57101
    touch_addr_setup_button_bit = 57120
    touch_addr_setup_button = 57121


def touch_data(self):
        coordinates = {
            
            "btn_apply": [620, 150],
            "btn_cancel": [720, 150],
            "btn_popup_1": [400, 110],
            "btn_popup_2": [400, 160],
            "btn_popup_3": [400, 215],
            "btn_popup_4": [400, 265],
            "btn_popup_5": [400, 315],
            
            "btn_number_1": [310, 200],
            "btn_number_2": [370, 200],
            "btn_number_3": [430, 200],
            "btn_number_4": [310, 255],
            "btn_number_5": [370, 255],
            "btn_number_6": [430, 255],
            "btn_number_7": [310, 310],
            "btn_number_8": [370, 310],
            "btn_number_9": [430, 310],
            "btn_number_0": [310, 370],
            "btn_number_dot": [370, 370],
            "btn_number_back": [490, 225],
            "btn_number_clear": [485, 340],
            "btn_num_pw_1": [255, 230],
            "btn_num_pw_2": [315, 230],
            "btn_num_pw_3": [370, 230],
            "btn_num_pw_4": [430, 230],
            "btn_num_pw_5": [485, 230],
            "btn_num_pw_6": [255, 290],
            "btn_num_pw_7": [315, 290],
            "btn_num_pw_8": [370, 290],
            "btn_num_pw_9": [430, 290],
            "btn_num_pw_0": [485, 290],
            "btn_num_pw_enter": [340, 345],
            "btn_testmode_1": [270, 100],
            "btn_testmode_2": [270, 160],
            "infinite": [490, 125],
            "cauiton_confirm": [340, 330],
            "cauiton_cancel": [450, 330],
        }
        return coordinates