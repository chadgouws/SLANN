# Get stock data from Yahoo Finance API

from yahoo_fin.stock_info import get_data


def get_stock_prices(ticker):
    return get_data(ticker, start_date=None, end_date=None, index_as_date=True, interval='1d')


if __name__ == '__main__':
    tickers = ['cpi.jo', 'psg.jo', 'dgh.jo', 'anh.jo', 'npn.jo', 'sbk.jo', 'abg.jo', 'rmh.jo', 'adi.jo', 'ned.jo',
               'aft.jo', 'ppc.jo', 'mnk.jo', 'cml.jo', 'fsr.jo', 'inl.jo', 'rem.jo', 'syg.jo', 'tkg.jo', 'cls.jo',
               'dcp.jo', 'msm.jo', 'pik.jo', 'shp.jo', 'spp.jo', 'arl.jo', 'tbs.jo', 'ton.jo', 'mnd.jo', 'sap.jo',
               'npk.jo', 'bvt.jo', 'coh.jo', 'ipl.jo', 'mrp.jo', 'pph.jo', 'tfg.jo', 'tru.jo', 'whl.jo', 'mei.jo',
               'ntc.jo', 'ari.jo', 'bil.jo', 'kio.jo', 'pan.jo', 'dsy.jo', 'lbh.jo', 'slm.jo', 'mcg.jo', 'prx.jo',
               'ams.jo', 'agl.jo', 'ang.jo', 'drd.jo', 'gln.jo', 'gfi.jo', 'har.jo', 'imp.jo', 'ssw.jo', 'mtn.jo',
               'vod.jo', 'snt.jo', 'exx.jo', 'sol.jo', 'apn.jo', 'eoh.jo', 'bti.jo', 'fbr.jo', 'bhp.jo', 'cfr.jo',
               'mnp.jo', 's32.jo', 'nhm.jo', 'bid.jo', 'qlt.jo', 'rni.jo', 'omu.jo', 'nrp.jo', 'rmi.jo', 'com.jo',
               'grt.jo', 'n91.jo', 'inp.jo', 'avi.jo', 'lhc.jo', 'cco.jo', 'mtm.jo', 'vvo.jo', 'hmn.jo', 'sre.jo',
               'baw.jo', 'gld.jo', 'rdf.jo', 'ite.jo', 'rbp.jo', 'txt.jo', 'byi.jo', 'tcp.jo', 'res.jo', 'ffa.jo',
               'ctk.jo', 'zplp.jo', 'ny1.jo', 'gtc.jo', 'kst.jo', 'equ.jo', 'imcb22.jo', 'mth.jo', 'sygwd.jo',
               'afe.jo', 'epp.jo', 'spg.jo'
               ]

    for tick in tickers:
        stock_prices = get_stock_prices(tick)
        print(stock_prices)
