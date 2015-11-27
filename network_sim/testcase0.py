from events import * 
from element import  *
from engine import *
from parse import *

import matplotlib.pyplot as plt
import tcp_fast
import tcp_tahoe

def main():
    
    '''
        For Test Case 0,
        Link ID: L1
        Link Rate: 10 Mbps
        Link Delay: 10 ms
        Link Buffer: 64 KB
        Flow ID: F1
        Flow Src: H1
        Flow Dest: H2
        Data Amt: 20MB
        Flow Start:1.0s
        
        dataPacket Size: 1024 bytes
        ackPacket Size: 64 KB
        ROUTER_PACKET_GENERATION_INTERVAL: 1.0 s
    '''
    
    engine = SimEngine(60)
    file_name = 'testcase0.txt'
    parse(engine, file_name)
    engine.run()
            
    '''
        Data Visualization
    '''
    engine.recorder.plot()
    
        
    
    

if __name__ == '__main__':
    main()
