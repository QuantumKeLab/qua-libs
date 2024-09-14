import numpy as np

from pathlib import Path
link_path = Path(__file__).resolve().parent/"config_link.toml"

from QM_driver_AS.ultitly.config_io import import_config
config_obj, spec = import_config( link_path )


from qspec.update import update_ReadoutFreqs, update_Readout
new_LO = 6.13#5.65
rin_offset = (+0.01502-0.00016+7.9e-5,+0.01300+1.5e-5) # I,Q
# rin_offset = (+0,+0) # I,Q
tof = 280
# init_value of readout amp is 0.2
# ,#
# name, IF, amp, z, len, angle
ro_infos = [
    {
        "name":"q0",
        "IF": -159+1.1-3.91-14.72+3.51+0.48+0.91,
        "amp": 0.048*2*0.75*1.25*0.5,
        "length":400,
        "phase": 293.1+0.5+297.3+2.7
    },{
        "name":"q1",
        "IF": -62+1.36+2.8-1.17-10.31+0.7+0.05-1.52,
        "amp": 0.2*0.1*5*0.3*1.75*1.75*0.5*1.75*0.5*1.4,#*0.3*0.5*4*0.75 *0.8,
        "length":400,
        "phase": 294.7-0.8+41.7+290.2
    },{
        "name":"q2",
        "IF": -221+0.75+5-1.25-0.5-10.89-0.264+1.255-0.48+1.03-0.06-0.23-1.1-0.8+0.63,  #-213.1+0.28,
        "amp": 0.5*0.3*0.8*0.3*1.75*1.75*0.75*0.75*0.75*1.2, # 0.2 *0.1,#*0.15*2*2*1.1 *0.8,
        "length":400,
        "phase": 107.3+24.2+10.3-22.4+205
    },
    {
        "name":"q3",
        "IF": -42+0.83+5-2-0.96-10+0.9-1.6-1.74+1.78+0.27-0.35-1.39+0.83-0.49,
        "amp": 0.2*0.846*0.75*0.75,#*0.3*0.5 *0.8,
        "length":400,
        "phase": 156.1+269.6+2.8+344.8+234.9-6.3+137.9+274.4
    },
    # {
    #     "name":"q3",
    #     "IF": -42+0.83+5-2-0.96-10+0.9-1.6-1.74+1.78+0.27-0.35-1.39-0.5+2-0.19+0.39-0.27,
    #     "amp": 0.05*1.03*1.07*2*0.8*0.98,
    #     "length":15000,
    #     "phase": 156.1+269.6+2.8+344.8+234.9-6.3+273.9+336.4+45+314.6
    # },
    {
        "name":"q4",
        "IF":-128+0.68+5+1.6-2.4-7.5+1.28-3.79-0.6-2.738+0.66+2.32+0.59-0.73-0.99-1+1.36-2+0.44,
        "amp": 0.2*0.667*0.782,
        "length":400,
        "phase": 229.9+34+0.1+33.6+318.7+293.7+73.9+220.5+221.3+3.7+307.6+26.7+356.3
    },
    {
        "name":"q5",
        "IF": -159+1.1,
        "amp": 0.1,
        "length":8000,
        "phase": 75
    },{
        "name":"q6",
        "IF": -214+1.153-0.08-0.8-0.5,  #-213.1+0.28,
        "amp": 0.05, # 0.2 *0.1,#*0.15*2*2*1.1 *0.8,
        "length":4000,
        "phase": 0
    },
    # {
    #     "name":"q7",
    #     "IF": -42+0.83+5-2,  #-213.1+0.28,
    #     "amp": 0.05, # 0.2 *0.1,#*0.15*2*2*1.1 *0.8,
    #     "length":4000,
    #     "phase": 0
    # },
    {
        "name":"q7",
        "IF": -42+0.83+5-2-0.96-10+0.9-1.6-1.74+1.78+0.27-0.35-1.39-0.5+2-0.19+0.39-0.27,
        "amp": 0.05*1.03*1.07*2*0.8*0.98*0.9,
        "length":15000,
        "phase": 156.1+269.6+2.8+344.8+234.9-6.3+273.9+336.4+45+314.6+325.7
    },
    {
        "name":"q8",
        "IF": -128+0.68+5+1.6-2.4-7.5+1.28-3.79-0.6-2.738+0.66+2.32+0.59-0.73-0.99-1+0.8+0.2+1.9+0.1-1.76+0.42-0.34,#q3:-42+0.83+5-2-0.96-10+0.9-1.6-1.74+1.78+0.27-0.35-1.39,  
        "amp": 0.05*0.9*1.5*1.24*0.99, # 0.2 *0.1,#*0.15*2*2*1.1 *0.8,
        "length":15000,
        "phase": 156.1+269.6+2.8+344.8+234.9-6.3+40+218.3+226.2+90+75.5+253.1+160.7+159.2
    }
]
# cavities = [['q0',+150-33, 0.3*0.1, 0, 2000,0],['q1',+150+0.8, 0.3*0.1*1.5*1.5*1.4, 0.038, 560,84.7],['q8',+150+3, 0.01, 0.1, 2000,0],['q5',+150-36, 0.3*0.05, -0.11, 2000,0]]
for i in ro_infos:
    wiring = spec.get_spec_forConfig('wire')

    f = spec.update_RoInfo_for(target_q=i["name"],LO=new_LO,IF=i["IF"])
    update_ReadoutFreqs(config_obj, f)
    ro_rotated_rad = i["phase"]/180*np.pi
    spec.update_RoInfo_for(i["name"],amp=i["amp"], len=i["length"],rotated=ro_rotated_rad, offset=rin_offset, time=tof)
    update_Readout(config_obj, i["name"], spec.get_spec_forConfig('ro'),wiring)
    # print(spec.get_spec_forConfig('ro')["q1"])

    config_dict = config_obj.get_config() 

from QM_driver_AS.ultitly.config_io import output_config
output_config( link_path, config_obj, spec )
