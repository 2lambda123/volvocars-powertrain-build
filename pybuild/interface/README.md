#Folder for abstract interfaces

The idea is to be able to calculate an interface between any two things.

Examples:
* Calculate the interface between a raster and the EMS.
* Calculate the interface between two rasters.

This is done by specifying anything as something with insignals and outsignals.
Then we can match the insignals from one item with the outsignals of the other.
When we do this, it is important that the signal names correspond.
The insignal name in one item has to be exactly the same as the outsignal name in the other.
That is why we have the HALA, to translate between internal signal name and hal property name.

We can also combine more than one interface to a domain.

Examples of domains:
* All raster to raster interfaces -> internal domain
* All rasters communication with one hal -> that hals domain
