output_matrix = np.load('shenzhen_outflux_matrix.npy')

test_data = output_matrix[:,288 * 49 : 288 * 59]

tw = 144
test_x = []
test_y = []
for i in range(10 * 12 * 24 - 147):
    if i >= 144:
        x = test_data[:,i:i+tw]
        y = test_data[:,i+tw+2:i+tw+3]
        test_x.append(x)
        test_y.append(y)