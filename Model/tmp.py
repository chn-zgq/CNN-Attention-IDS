import tensorflow as tf
from tensorflow.keras.layers import LayerNormalization, Dense, Dropout
from tensorflow.keras import backend as K
from tensorflow.keras.layers import MultiHeadAttention


def multi_head_self_attention(inputs, d_model=128, num_heads=8, dropout_rate=0.1):

    assert d_model % num_heads == 0

    dim_per_head = d_model // num_heads

    qkv_linear = Dense(d_model * 3)
    qkv = qkv_linear(inputs)
    q, k, v = tf.split(qkv, 3, axis=-1)

    q = tf.concat(tf.split(q, num_heads, axis=2), axis=0)
    k = tf.concat(tf.split(k, num_heads, axis=2), axis=0)
    v = tf.concat(tf.split(v, num_heads, axis=2), axis=0)

    attention_scores = tf.matmul(q, k, transpose_b=True)
    attention_scores = attention_scores / tf.math.sqrt(tf.cast(dim_per_head, tf.float32))

    attention_probs = tf.nn.softmax(attention_scores, axis=-1)

    attention_probs = Dropout(dropout_rate, name="dropout_attn")(attention_probs)

    context_layer = tf.matmul(attention_probs, v)
    context_layer = tf.concat(tf.split(context_layer, num_heads, axis=0), axis=2)

    out_proj = Dense(d_model, name="dense_attn")
    outputs = out_proj(context_layer)

    return outputs


# 示例调用（请替换真实输入数据）
output_of_attention = multi_head_self_attention(inputs)
