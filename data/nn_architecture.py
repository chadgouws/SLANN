import pipeline.prepare_data as prep


w1 = prep.read_nn_from_file('SMGANN_5000_research_W1_2021-05-18T18-12-58.csv')
print(w1.shape)
w2 = prep.read_nn_from_file('SMGANN_5000_research_W2_2021-05-18T18-12-58.csv')
print(w2.shape)
w3 = prep.read_nn_from_file('SMGANN_5000_research_W3_2021-05-18T18-12-58.csv')
print(w3.shape)
