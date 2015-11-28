'''
    Constants
'''

DIR_IMG = 'img_2/'

PACKET_SIZE = 1024

ACK_PACKET_SIZE = 64 #CHECK IT

ROUTER_PACKET_GENERATION_INTERVAL = 5 #check it

EVENT_LINK_AVAILABLE = 'LinkAvailable'
EVENT_PACKET_RECEIPT = 'PacketReceipt'
EVENT_ROUTINGTABLE_OUTDATED = 'RoutingTableOutdated'
EVENT_PACKET_TIMEOUT = 'PacketTimeOut'
EVENT_FLOW_START = 'FlowStart'
EVENT_ROUTINGTABLE_UPDATE = 'RoutingTableUpdate'

CATE_LINK_RATE = "cate_link_rate"
CATE_PACKET_LOSS = "cate_packet_loss"
CATE_BUFFER_OCCUPANCY = "cate_buffer_occupancy"
CATE_FLOW_RATE = "cate_flow_rate"
CATE_WINDOW_SIZE = "cate_window_size"
CATE_PACKET_DELAY = "cate_packet_delay"
CATE_PKTS_RECEIVED = "cate_pkts_received"

CATE_ALL = [CATE_LINK_RATE, CATE_PACKET_LOSS, CATE_BUFFER_OCCUPANCY, CATE_FLOW_RATE, CATE_WINDOW_SIZE, CATE_PACKET_DELAY, CATE_PKTS_RECEIVED]




