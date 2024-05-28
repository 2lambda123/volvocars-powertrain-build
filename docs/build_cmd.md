# Run the build command

`pybuild/build.py` is the starting point for generating all the files needed for building a complete SW using the supplier make environment. The script takes one positional argument, and that is a [project_config](project_config.md).

This script acts as a command line wrapper for [build](../../pybuild/build.py).

```none
usage: build.py [-h] [-cd] [-d] [-na] [-if] [-V] proj_config

positional arguments:
    proj_config        the project root configuration file

optional arguments:
    -h,  --help        show this help message and exit
    -cd, --core_dummy  generate core dummy code to enable integration with old supplier code
    -d,  --debug       activate the debug log
    -na, --no_abort    do not abort due to errors
    -if, --interface   generate interface report
    -V,  --version     show application version and exit
```
