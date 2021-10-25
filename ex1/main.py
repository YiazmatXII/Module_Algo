#!/usr/bin/env python3

import numpy as np
from parcours import parcours
from test import average_wait
from test import ref_parcours

def main():
    list_house = np.random.normal(0,1000,1000).tolist()
    average_wait(parcours(list_house))
    #parcours(list_house)

if __name__ == '__main__':
    main()
