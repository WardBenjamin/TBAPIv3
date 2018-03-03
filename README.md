# TBAPI v3

Python library to get data from The Blue Alliance. _Uses v3 of the TBA API._

This library returns JSON data fetched from The Blue Alliance's API. Requires an application-specific key issued by TBA.

Compatible with Python 3.

Official documentation for the The Blue Alliance API (the official API, not these bindings) can be found [here](https://www.thebluealliance.com/apidocs)

## Setup
First, install the module:

    pip3 install tbapiv3

Then, to use these functions, you must import the `tbapiv3` module:

```py
import tbapiv3
```

And then instantiate an instance of the bindings class:

```py
tba = tbapiv3.TBA('key')
```

## Authors

This software was created and is maintained by [Benjamin Ward](https://github.com/WardBenjamin). Thanks to [Erik Boesen](https://github.com/ErikBoesen) and other contributors for the original [TBApy library](https://github.com/frc1418/tbapy).
