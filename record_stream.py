import serial
import queue

import argparse

from pathlib import Path
import time
     


def main():
  parser = argparse.ArgumentParser(description=
        "Specify a serial device, e.g. /dev/ttyUSB0")
  parser.add_argument('device', nargs='+', 
          help="Specifiy the input device name")
  parser.add_argument('-r', '--record', default=0, type=int,
              help="Record the specified number of packets, -r N")
  arg_dict = vars(parser.parse_args())
 


  sub_interval = 1000
  timeout_time = 2.0
  ser = serial.Serial(arg_dict['device'][0], baudrate=115200, timeout=timeout_time)
  
  bytelist = queue.Queue()

  waiting_for_connection = True
  if arg_dict['record'] != 0:
    print("Going to record data. ")
    recs = arg_dict['record'];
    try:
      while recs > 0:
        s = ser.read(sub_interval)
        for b in s:
          bytelist.put(b) # Blocking
      
        if len(s) < sub_interval: # timeout happened
          if waiting_for_connection:
            print("Waiting for connection...  ")
            continue
          else: 
            print('Connection timed out ({0} s)'.format(timeout_time))
            break
        else:
          waiting_for_connection = False
          print('. ', end='', flush=True)
      
      recs -= sub_interval
    except:
      print("Interrupted!")
    print("  Done!")
   # Process bytelist
   
      
  ser.close()
   
  print(bytelist.qsize())    
  mybytes = []
  while bytelist.empty() == False:
    try:
      mybytes.append(bytelist.get_nowait())
    except queue.Empty:
      break;
  
  record_byte_array = bytearray(mybytes)

  Path("out").mkdir(parents=True, exist_ok=True)
  outfilename = "out/" + "cap_rec_" + time.strftime("%Y%m%d-%H%M%S") + ".txt"
  with open(outfilename, "wb") as outfile:
    outfile.write(record_byte_array)
  
  print("Wrote to file {0}".format(outfilename))


if __name__ == "__main__":
  main()
