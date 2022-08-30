
# author: Quantium Rock
# license: MIT

import numpy as np
import pandas as pd
from pathlib import Path
from data_primary import PrimaryData


class SecondaryData ( PrimaryData ):
    

    def __init__ ( self ):

        super().__init__()
        self.secondary_path = self.primary_path.replace('primary', 'secondary')
        self.db_path = self.secondary_path

    
    def getData ( self, year=2022 ):

        in_path = self.primary_path + str(year) +'/'

        out_path = self.secondary_path + str(year) +'/'
        Path(out_path).mkdir(parents=True, exist_ok=True)

        # load mid prices
        op = pd.read_csv(in_path + 'opens.csv', index_col=0)
        hi = pd.read_csv(in_path + 'highs.csv', index_col=0)
        lo = pd.read_csv(in_path + 'lows.csv', index_col=0)
        cl = pd.read_csv(in_path + 'closes.csv', index_col=0)

        # create portfolio returns (standarize protfolio prices %)
        logs_ = ( np.log(cl) - np.log(op) )*100
        rets_ = ( cl / op -1 )*100
        vols_ = ( hi / lo -1 )*100
        higs_ = ( hi / cl -1 )*100
        lows_ = ( cl / lo -1 )*100

        logs_.to_csv(out_path + 'logs_.csv', index=True)
        rets_.to_csv(out_path + 'rets_.csv', index=True)
        vols_.to_csv(out_path + 'vols_.csv', index=True)
        higs_.to_csv(out_path + 'higs_.csv', index=True)
        lows_.to_csv(out_path + 'lows_.csv', index=True)

        del logs_, rets_, vols_, higs_, lows_

        return True
