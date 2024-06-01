from package import *
from pre_handle import *

# Pcap测试文件的路径
test_data_path = "./Data/TEST"

df = Pre_Handle_Data(file_name=test_data_path, columns=columns)

data_feature = df.columns.values.tolist()
predict_feature = ["Predict_type"] + data_feature

pre_data_list = pd.read_csv(test_data_path, names=columns)
feature_list = pre_data_list.values.tolist()

# 数据标准化
scaler = MinMaxScaler()
pre_dataset = scaler.fit_transform(df)

feature_scaler = scaler.fit_transform(get_pre_file_data(file_name=test_data_path))
feature_scaler_list = feature_scaler.tolist()

data_processing = pre_dataset.tolist()

# 加载训练好的模型，假设模型名为'attention_cnn3_model.h5'
model = tf.keras.models.load_model('cnn_attention_mode_finall.h5')

# 使用加载的模型对测试数据（test_dataset）进行预测，返回的是每个样本对应的类别概率分布
predictions = model.predict(pre_dataset)

# 使用argmax函数沿着最后一维（-1）获取每个样本预测的类别，argmax函数返回的是概率最高的索引
predicted_indices = np.argmax(predictions, axis=-1)

# 定义类别名称及其对应的索引映射，例如：0对应的类别是'Dos'，1对应的类别是'Normal'等
class_name_map = {0: 'Dos', 1: 'Normal', 2: 'Probe', 3: 'R2L', 4: 'U2R'}

result_list = []
for i in range(len(data_processing)):
    result_list.append([class_name_map[predicted_indices[i]]] + data_processing[i])

#
# # 创建一个字典，用于存储各类别的计数
# class_names_count = {'Dos': 0, 'Normal': 0, 'Probe': 0, 'R2L': 0, 'U2R': 0}
#
# # 遍历预测的类别索引，对每个索引对应的类别进行计数
# for i in range(len(predicted_indices)):
#     # 使用映射将索引转换为类别名称，然后更新类别的计数
#     class_names_count[class_name_map[predicted_indices[i]]] += 1
#
# # 打印各类别的计数结果
# print(class_names_count)
