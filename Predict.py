from package import *

# KDDCup99预测集的路径
test_data_path = "./Dataset/kddcup.testdata.unlabeled"

# 读取数据
df = pd.read_csv(test_data_path, names=columns)

# 删除无用的特征
df.drop('num_root', axis=1, inplace=True)
df.drop('srv_serror_rate', axis=1, inplace=True)
df.drop('srv_rerror_rate', axis=1, inplace=True)
df.drop('dst_host_srv_serror_rate', axis=1, inplace=True)
df.drop('dst_host_serror_rate', axis=1, inplace=True)
df.drop('dst_host_rerror_rate', axis=1, inplace=True)
df.drop('dst_host_srv_rerror_rate', axis=1, inplace=True)
df.drop('dst_host_same_srv_rate', axis=1, inplace=True)
df.drop('is_host_login', axis=1, inplace=True)

# 删除'service'列
df.drop('service', axis=1, inplace=True)

# 删除含有NaN的列
df = df.dropna(axis=1, how='any')

# 仅保留具有多个唯一值的列
df = df[[col for col in df if df[col].nunique() > 1]]

# 独热编码映射'protocol_type'、'flag'
protocol_map = {'icmp': 0, 'tcp': 1, 'udp': 2}
flag_map = {'SF': 0, 'S0': 1, 'REJ': 2, 'RSTR': 3, 'RSTO': 4, 'SH': 5, 'S1': 6, 'S2': 7, 'RSTOS0': 8, 'S3': 9,
            'OTH': 10}
df['protocol_type'] = df['protocol_type'].map(protocol_map)
df['flag'] = df['flag'].map(flag_map)

# 数据标准化
scaler = MinMaxScaler()
pre_dataset = scaler.fit_transform(df)

# 加载训练好的模型，假设模型名为'attention_cnn3_model.h5'
model = tf.keras.models.load_model('attention_cnn3_model.h5')

# 使用加载的模型对测试数据（test_dataset）进行预测，返回的是每个样本对应的类别概率分布
predictions = model.predict(pre_dataset)

# 使用argmax函数沿着最后一维（-1）获取每个样本预测的类别，argmax函数返回的是概率最高的索引
predicted_indices = np.argmax(predictions, axis=-1)

# 定义类别名称及其对应的索引映射，例如：0对应的类别是'Dos'，1对应的类别是'Normal'等
class_name_map = {0: 'Dos', 1: 'Normal', 2: 'Probe', 3: 'R2L', 4: 'U2R'}

# 创建一个字典，用于存储各类别的计数
class_names_count = {'Dos': 0, 'Normal': 0, 'Probe': 0, 'R2L': 0, 'U2R': 0}

# 遍历预测的类别索引，对每个索引对应的类别进行计数
for i in range(len(predicted_indices)):
    # 使用映射将索引转换为类别名称，然后更新类别的计数
    class_names_count[class_name_map[predicted_indices[i]]] += 1

# 打印各类别的计数结果
print(class_names_count)
