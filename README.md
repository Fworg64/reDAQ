## record_stream.py

Record data through the command line

```
# Record up to 3000 packets
python3 record_stream.py -r 3000 /dev/ttyACM0
# Press CTRL+C to exit
```

## plot_stream_app.py

Record data through a GUI app

```
python3 plot_stream_app.py
```

Enter '/dev/ttyACM0' in the device bar and press open.
Then press record to record data.
Press stop when finished and then close the program.

Plotting does not work (yet!).


## plot_record.py

Show a plot of recorded data.

```
python3 plot_record.py out/cap_rec_20220929-74710.txt
```

