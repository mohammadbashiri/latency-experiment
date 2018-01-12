# VRLatency

TODO:

1) data packaging from arduino - preferably containing both sensors with timing informatio
2) thread for reading data. Must work first on the mock serial channel

* reading data, sotre_data_draw must be decoupled. we can read as much as we want. grab a portion of
that data, and display it. So make sure store_to_draw works with variable data size as as input