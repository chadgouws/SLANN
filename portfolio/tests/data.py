weight_1 = 0.1
weight_2 = 0.05

fee = 0.001
fee_buy = 0.002
fee_sell = 0.004

cash_initial_0 = 0.0
asset_initial_0 = 0.0

cash_initial_1 = 1000.0
asset_initial_1 = 1.0

cash_initial_2 = 1000.0
asset_initial_2 = 0.0

cash_initial_3 = 0.0
asset_initial_3 = 5.0

data_1 = [{'token': 'BTC', 'asset_price': {'BTC': 500.0, 'cash': 1.0},
           'asset_amt': {'cash': 1000.0, 'BTC': 1.0},  'algo_output': 1.0,
           },
          {'token': 'BTC', 'asset_price': {'BTC': 600.0, 'cash': 1.0},
           'asset_amt': {'cash': 850.0, 'BTC': 1.2997}, 'algo_output': 0.5,
           },
          {'token': 'BTC', 'asset_price': {'BTC': 500.0, 'cash': 1.0},
           'asset_amt': {'cash': 850.0, 'BTC': 1.2997}, 'algo_output': 0.0,
           },
          {'token': 'BTC', 'asset_price': {'BTC': 700.0, 'cash': 1.0},
           'asset_amt': {'cash': 999.835015, 'BTC': 0.9997300000000001},  'algo_output': 1.0,
           },
          {'token': 'BTC',  'asset_price': {'BTC': 800.0, 'cash': 1.0},
           'asset_amt': {'cash': 829.8704135, 'BTC': 1.2422937669978573}, 'algo_output': 1.0,
           },
          {'token': 'BTC', 'asset_price': {'BTC': 900.0, 'cash': 1.0},
           'asset_amt': {'cash': 647.4998707901715, 'BTC': 1.4700289822067558},  'algo_output': 0.0,
           },
          {'token': 'BTC',  'asset_price': {'BTC': 900.0, 'cash': 1.0},
           'asset_amt': {'cash': 844.3554136723191, 'BTC': 1.2510816538982834},  'algo_output': 0.0,
           },
          {'token': 'BTC',  'asset_price': {'BTC': 800.0, 'cash': 1.0},
           'asset_amt': {'cash': 1041.1912710001784, 'BTC': 1.0321562203226418},  'algo_output': 0.5,
           }
          ]

data_2 = [{'token': 'BTC', 'asset_price': {'BTC': 500.0, 'ETH': 100.0, 'XRP': 20.0, 'cash': 1.0}, 'algo_output': 1.0,
           },
          {'token': 'ETH', 'asset_price': {'BTC': 500.0, 'ETH': 100.0, 'XRP': 20.0, 'cash': 1.0}, 'algo_output': 1.0,
           },
          {'token': 'XRP', 'asset_price': {'BTC': 500.0, 'ETH': 100.0, 'XRP': 20.0, 'cash': 1.0}, 'algo_output': 1.0,
           },

          {'token': 'BTC', 'asset_price': {'BTC': 600.0, 'ETH': 110.0, 'XRP': 25.0, 'cash': 1.0}, 'algo_output': 0.0,
           },
          {'token': 'ETH', 'asset_price': {'BTC': 600.0, 'ETH': 110.0, 'XRP': 25.0, 'cash': 1.0}, 'algo_output': 0.0,
           },
          {'token': 'XRP', 'asset_price': {'BTC': 600.0, 'ETH': 110.0, 'XRP': 25.0, 'cash': 1.0}, 'algo_output': 0.0,
           },

          {'token': 'BTC', 'asset_price': {'BTC': 700.0, 'ETH': 100.0, 'XRP': 30.0, 'cash': 1.0}, 'algo_output': 0.5,
           },
          {'token': 'ETH', 'asset_price': {'BTC': 700.0, 'ETH': 100.0, 'XRP': 30.0, 'cash': 1.0}, 'algo_output': 0.0,
           },
          {'token': 'XRP', 'asset_price': {'BTC': 700.0, 'ETH': 100.0, 'XRP': 30.0, 'cash': 1.0}, 'algo_output': 1.0,
           },

          {'token': 'BTC', 'asset_price': {'BTC': 600.0, 'ETH': 120.0, 'XRP': 35.0, 'cash': 1.0}, 'algo_output': 1.0,
           },
          {'token': 'ETH', 'asset_price': {'BTC': 600.0, 'ETH': 120.0, 'XRP': 35.0, 'cash': 1.0}, 'algo_output': 0.0,
           },
          {'token': 'XRP', 'asset_price': {'BTC': 600.0, 'ETH': 120.0, 'XRP': 35.0, 'cash': 1.0}, 'algo_output': 1.0,
           },

          {'token': 'BTC', 'asset_price': {'BTC': 500.0, 'ETH': 110.0, 'XRP': 25.0, 'cash': 1.0}, 'algo_output': 0.5,
           },
          {'token': 'ETH', 'asset_price': {'BTC': 500.0, 'ETH': 110.0, 'XRP': 25.0, 'cash': 1.0}, 'algo_output': 1.0,
           },
          {'token': 'XRP', 'asset_price': {'BTC': 500.0, 'ETH': 110.0, 'XRP': 25.0, 'cash': 1.0}, 'algo_output': 0.0,
           },
          ]

data_3 = [{'token': 'BTC', 'asset_price': {'BTC': 3000.0, 'ETH': 2000.0, 'XRP': 2.0, 'cash': 1.0}, 'algo_output': 0.0,
           },
          {'token': 'ETH', 'asset_price': {'BTC': 3000.0, 'ETH': 2000.0, 'XRP': 2.0, 'cash': 1.0}, 'algo_output': 1.0,
           },
          {'token': 'XRP', 'asset_price': {'BTC': 3000.0, 'ETH': 2000.0, 'XRP': 2.0, 'cash': 1.0}, 'algo_output': 1.0,
           },

          {'token': 'BTC', 'asset_price': {'BTC': 3100.0, 'ETH': 1900.0, 'XRP': 2.5, 'cash': 1.0}, 'algo_output': 0.0,
           },
          {'token': 'ETH', 'asset_price': {'BTC': 3100.0, 'ETH': 1900.0, 'XRP': 2.5, 'cash': 1.0}, 'algo_output': 0.0,
           },
          {'token': 'XRP', 'asset_price': {'BTC': 3100.0, 'ETH': 1900.0, 'XRP': 2.5, 'cash': 1.0}, 'algo_output': 1.0,
           },

          {'token': 'BTC', 'asset_price': {'BTC': 3200.0, 'ETH': 1950.0, 'XRP': 1.5, 'cash': 1.0}, 'algo_output': 1.0,
           },
          {'token': 'ETH', 'asset_price': {'BTC': 3200.0, 'ETH': 1950.0, 'XRP': 1.5, 'cash': 1.0}, 'algo_output': 0.5,
           },
          {'token': 'XRP', 'asset_price': {'BTC': 3200.0, 'ETH': 1950.0, 'XRP': 1.5, 'cash': 1.0}, 'algo_output': 1.0,
           },

          {'token': 'BTC', 'asset_price': {'BTC': 3150.0, 'ETH': 2050.0, 'XRP': 1.0, 'cash': 1.0}, 'algo_output': 1.0,
           },
          {'token': 'ETH', 'asset_price': {'BTC': 3150.0, 'ETH': 2050.0, 'XRP': 1.0, 'cash': 1.0}, 'algo_output': 1.0,
           },
          {'token': 'XRP', 'asset_price': {'BTC': 3150.0, 'ETH': 2050.0, 'XRP': 1.0, 'cash': 1.0}, 'algo_output': 0.5,
           },

          {'token': 'BTC', 'asset_price': {'BTC': 3250.0, 'ETH': 2000.0, 'XRP': 2.0, 'cash': 1.0}, 'algo_output': 0.0,
           },
          {'token': 'ETH', 'asset_price': {'BTC': 3250.0, 'ETH': 2000.0, 'XRP': 2.0, 'cash': 1.0}, 'algo_output': 0.5,
           },
          {'token': 'XRP', 'asset_price': {'BTC': 3250.0, 'ETH': 2000.0, 'XRP': 2.0, 'cash': 1.0}, 'algo_output': 0.0,
           },

          {'token': 'BTC', 'asset_price': {'BTC': 3350.0, 'ETH': 1900.0, 'XRP': 2.2, 'cash': 1.0}, 'algo_output': 1.0,
           },
          {'token': 'ETH', 'asset_price': {'BTC': 3350.0, 'ETH': 1900.0, 'XRP': 2.2, 'cash': 1.0}, 'algo_output': 0.5,
           },
          {'token': 'XRP', 'asset_price': {'BTC': 3350.0, 'ETH': 1900.0, 'XRP': 2.2, 'cash': 1.0}, 'algo_output': 0.0,
           },

          {'token': 'BTC', 'asset_price': {'BTC': 3300.0, 'ETH': 1900.0, 'XRP': 2.1, 'cash': 1.0}, 'algo_output': 1.0,
           },
          {'token': 'ETH', 'asset_price': {'BTC': 3350.0, 'ETH': 1900.0, 'XRP': 2.2, 'cash': 1.0}, 'algo_output': 1.0,
           },
          {'token': 'XRP', 'asset_price': {'BTC': 3350.0, 'ETH': 1900.0, 'XRP': 2.2, 'cash': 1.0}, 'algo_output': 1.0,
           },

          {'token': 'BTC', 'asset_price': {'BTC': 3200.0, 'ETH': 1800.0, 'XRP': 2.0, 'cash': 1.0}, 'algo_output': 1.0,
           },
          {'token': 'ETH', 'asset_price': {'BTC': 3200.0, 'ETH': 1800.0, 'XRP': 2.0, 'cash': 1.0}, 'algo_output': 0.0,
           },
          {'token': 'XRP', 'asset_price': {'BTC': 3200.0, 'ETH': 1800.0, 'XRP': 2.0, 'cash': 1.0}, 'algo_output': 1.0,
           },

          {'token': 'BTC', 'asset_price': {'BTC': 3250.0, 'ETH': 1850.0, 'XRP': 2.1, 'cash': 1.0}, 'algo_output': 0.0,
           },
          {'token': 'ETH', 'asset_price': {'BTC': 3250.0, 'ETH': 1850.0, 'XRP': 2.1, 'cash': 1.0}, 'algo_output': 1.0,
           },
          {'token': 'XRP', 'asset_price': {'BTC': 3250.0, 'ETH': 1850.0, 'XRP': 2.1, 'cash': 1.0}, 'algo_output': 0.5,
           },
          ]

data_4 = [{'token': 'BTC', 'asset_price': {'BTC': 3000.0, 'ETH': 2000.0, 'XRP': 2.0, 'cash': 1.0}, 'algo_output': 1.0,
           },
          {'token': 'ETH', 'asset_price': {'BTC': 3000.0, 'ETH': 2000.0, 'XRP': 2.0, 'cash': 1.0}, 'algo_output': 0.0,
           },
          {'token': 'XRP', 'asset_price': {'BTC': 3000.0, 'ETH': 2000.0, 'XRP': 2.0, 'cash': 1.0}, 'algo_output': 0.5,
           },

          {'token': 'BTC', 'asset_price': {'BTC': 3100.0, 'ETH': 1900.0, 'XRP': 2.5, 'cash': 1.0}, 'algo_output': 1.0,
           },
          {'token': 'ETH', 'asset_price': {'BTC': 3100.0, 'ETH': 1900.0, 'XRP': 2.5, 'cash': 1.0}, 'algo_output': 0.0,
           },
          {'token': 'XRP', 'asset_price': {'BTC': 3100.0, 'ETH': 1900.0, 'XRP': 2.5, 'cash': 1.0}, 'algo_output': 1.0,
           },

          {'token': 'BTC', 'asset_price': {'BTC': 3200.0, 'ETH': 1950.0, 'XRP': 1.5, 'cash': 1.0}, 'algo_output': 0.0,
           },
          {'token': 'ETH', 'asset_price': {'BTC': 3200.0, 'ETH': 1950.0, 'XRP': 1.5, 'cash': 1.0}, 'algo_output': 0.5,
           },
          {'token': 'XRP', 'asset_price': {'BTC': 3200.0, 'ETH': 1950.0, 'XRP': 1.5, 'cash': 1.0}, 'algo_output': 0.0,
           },

          {'token': 'BTC', 'asset_price': {'BTC': 3150.0, 'ETH': 2050.0, 'XRP': 1.0, 'cash': 1.0}, 'algo_output': 1.0,
           },
          {'token': 'ETH', 'asset_price': {'BTC': 3150.0, 'ETH': 2050.0, 'XRP': 1.0, 'cash': 1.0}, 'algo_output': 1.0,
           },
          {'token': 'XRP', 'asset_price': {'BTC': 3150.0, 'ETH': 2050.0, 'XRP': 1.0, 'cash': 1.0}, 'algo_output': 0.5,
           },

          {'token': 'BTC', 'asset_price': {'BTC': 3250.0, 'ETH': 2000.0, 'XRP': 2.0, 'cash': 1.0}, 'algo_output': 0.0,
           },
          {'token': 'ETH', 'asset_price': {'BTC': 3250.0, 'ETH': 2000.0, 'XRP': 2.0, 'cash': 1.0}, 'algo_output': 1.0,
           },
          {'token': 'XRP', 'asset_price': {'BTC': 3250.0, 'ETH': 2000.0, 'XRP': 2.0, 'cash': 1.0}, 'algo_output': 0.0,
           },

          {'token': 'BTC', 'asset_price': {'BTC': 3350.0, 'ETH': 1900.0, 'XRP': 2.2, 'cash': 1.0}, 'algo_output': 0.0,
           },
          {'token': 'ETH', 'asset_price': {'BTC': 3350.0, 'ETH': 1900.0, 'XRP': 2.2, 'cash': 1.0}, 'algo_output': 0.5,
           },
          {'token': 'XRP', 'asset_price': {'BTC': 3350.0, 'ETH': 1900.0, 'XRP': 2.2, 'cash': 1.0}, 'algo_output': 0.5,
           },

          {'token': 'BTC', 'asset_price': {'BTC': 3300.0, 'ETH': 1900.0, 'XRP': 2.1, 'cash': 1.0}, 'algo_output': 0.0,
           },
          {'token': 'ETH', 'asset_price': {'BTC': 3350.0, 'ETH': 1900.0, 'XRP': 2.2, 'cash': 1.0}, 'algo_output': 0.5,
           },
          {'token': 'XRP', 'asset_price': {'BTC': 3350.0, 'ETH': 1900.0, 'XRP': 2.2, 'cash': 1.0}, 'algo_output': 0.0,
           },

          {'token': 'BTC', 'asset_price': {'BTC': 3200.0, 'ETH': 1800.0, 'XRP': 2.0, 'cash': 1.0}, 'algo_output': 1.0,
           },
          {'token': 'ETH', 'asset_price': {'BTC': 3200.0, 'ETH': 1800.0, 'XRP': 2.0, 'cash': 1.0}, 'algo_output': 0.0,
           },
          {'token': 'XRP', 'asset_price': {'BTC': 3200.0, 'ETH': 1800.0, 'XRP': 2.0, 'cash': 1.0}, 'algo_output': 1.0,
           },

          {'token': 'BTC', 'asset_price': {'BTC': 3250.0, 'ETH': 1850.0, 'XRP': 2.1, 'cash': 1.0}, 'algo_output': 0.0,
           },
          {'token': 'ETH', 'asset_price': {'BTC': 3250.0, 'ETH': 1850.0, 'XRP': 2.1, 'cash': 1.0}, 'algo_output': 1.0,
           },
          {'token': 'XRP', 'asset_price': {'BTC': 3250.0, 'ETH': 1850.0, 'XRP': 2.1, 'cash': 1.0}, 'algo_output': 1.0,
           },

          {'token': 'BTC', 'asset_price': {'BTC': 3250.0, 'ETH': 1900.0, 'XRP': 2.2, 'cash': 1.0}, 'algo_output': 1.0,
           },
          {'token': 'ETH', 'asset_price': {'BTC': 3250.0, 'ETH': 1900.0, 'XRP': 2.2, 'cash': 1.0}, 'algo_output': 0.0,
           },
          {'token': 'XRP', 'asset_price': {'BTC': 3250.0, 'ETH': 1900.0, 'XRP': 2.2, 'cash': 1.0}, 'algo_output': 1.0,
           },

          {'token': 'BTC', 'asset_price': {'BTC': 3150.0, 'ETH': 1950.0, 'XRP': 2.0, 'cash': 1.0}, 'algo_output': 1.0,
           },
          {'token': 'ETH', 'asset_price': {'BTC': 3150.0, 'ETH': 1950.0, 'XRP': 2.0, 'cash': 1.0}, 'algo_output': 0.0,
           },
          {'token': 'XRP', 'asset_price': {'BTC': 3150.0, 'ETH': 1950.0, 'XRP': 2.0, 'cash': 1.0}, 'algo_output': 0.0,
           },

          {'token': 'BTC', 'asset_price': {'BTC': 3100.0, 'ETH': 1900.0, 'XRP': 2.2, 'cash': 1.0}, 'algo_output': 1.0,
           },
          {'token': 'ETH', 'asset_price': {'BTC': 3100.0, 'ETH': 1900.0, 'XRP': 2.2, 'cash': 1.0}, 'algo_output': 0.5,
           },
          {'token': 'XRP', 'asset_price': {'BTC': 3100.0, 'ETH': 1900.0, 'XRP': 2.2, 'cash': 1.0}, 'algo_output': 0.0,
           },

          {'token': 'BTC', 'asset_price': {'BTC': 3000.0, 'ETH': 1800.0, 'XRP': 2.3, 'cash': 1.0}, 'algo_output': 0.5,
           },
          {'token': 'ETH', 'asset_price': {'BTC': 3000.0, 'ETH': 1800.0, 'XRP': 2.3, 'cash': 1.0}, 'algo_output': 1.0,
           },
          {'token': 'XRP', 'asset_price': {'BTC': 3000.0, 'ETH': 1800.0, 'XRP': 2.3, 'cash': 1.0}, 'algo_output': 1.0,
           },

          {'token': 'BTC', 'asset_price': {'BTC': 3100.0, 'ETH': 1900.0, 'XRP': 2.4, 'cash': 1.0}, 'algo_output': 0.0,
           },
          {'token': 'ETH', 'asset_price': {'BTC': 3100.0, 'ETH': 1900.0, 'XRP': 2.4, 'cash': 1.0}, 'algo_output': 0.0,
           },
          {'token': 'XRP', 'asset_price': {'BTC': 3100.0, 'ETH': 1900.0, 'XRP': 2.4, 'cash': 1.0}, 'algo_output': 1.0,
           },
          ]
