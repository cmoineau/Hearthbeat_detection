# Hearthbeat detection

This little project is a 2 hours "fun" project where I tried to implement in python a method to detect R-peaks.

## What is it all about

Basically, the goal of this project is to get the index of every R-peaks on an ECG signal. This is import for computing valuable informations like the hearth rate, the R amplitude etc ...

You can take a look at this [wikipedia link](https://en.wikipedia.org/wiki/Electrocardiography) for more details on ECG. 

## The algorithm :
Two parameters : initial max and filter parameter.
Initial max : Initialise the slope threshold, if too low you will detect a lot of small peaks if to high you will not detect any peaks.
Filter parameter : A value to adjust the new initial max once you have found a new peak.

The algorithm seek R peaks by looking at the variation of the slope
## Result :

![result](./result.png)

## Reference :
- [data-set](https://www.kaggle.com/shayanfazeli/heartbeat/data) to play with. 
- A better implementation of the method : https://github.com/GCY/wxECGAnalyzer
- So, H. H., and K. L. Chan. "Development of QRS detection method for real-time ambulatory cardiac monitor." Engineering in Medicine and Biology Society, 1997. Proceedings of the 19th Annual International Conference of the IEEE. Vol. 1. IEEE, 1997.

