import argparse
import matplotlib.pyplot as plt

import packetprocessor.packet_processor as ppr

import pdb

def main():
  parser = argparse.ArgumentParser(description=
              "Specify files to plot")
  parser.add_argument('files', nargs='+', help=
              "Specify the input file from a recording file")
  arg_dict = vars(parser.parse_args())

  # for each file:
  #   open file:
  #     process file into data: rinse packets and count missing
  
  for input_file in arg_dict['files']:
    packer = ppr.packetProcessor()
    packet_list = []
    drop_count = 0
    with open(input_file, "rb") as infile:
      # give each byte to state packitizer
      # collect packets when given
      cur_byte = infile.read(1)
      while (cur_byte): # reading eol gives "False"
        state, ret = packer.give_byte(cur_byte)
        if ret is not None:
          packet_list.append(ret)
        cur_byte = infile.read(1)
      
    print(drop_count)
    print(len(packet_list))
    print(packet_list[0:10])
    
    

    exes = [packet["seq"] for packet in packet_list if packet["crc_valid"]]
    wyes1 = [packet["chan_a"] for packet in packet_list if packet["crc_valid"]]
    wyes2 = [packet["chan_b"] for packet in packet_list if packet["crc_valid"]]
    wyes3 = [packet["chan_c"] for packet in packet_list if packet["crc_valid"]]
    wyes4 = [packet["chan_d"] for packet in packet_list if packet["crc_valid"]]

    print("Found {0} packets with valid CRCs".format(len(exes)))

    plt.figure()
    plt.plot(exes)
    plt.figure()
    plt.subplot(4,1,1)
    plt.plot(wyes1)
    plt.subplot(4,1,2)
    plt.plot(wyes2)
    plt.subplot(4,1,3)
    plt.plot(wyes3)
    plt.subplot(4,1,4)
    plt.plot(wyes4)

  plt.show()
  # for each dataset:
  #   extract x indices, y indices for starters
  #   plot data with matplotlib

  
if __name__ == "__main__":
  main()
