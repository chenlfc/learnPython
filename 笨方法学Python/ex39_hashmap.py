
# 初始化，创建一个空的列表变量叫做aMap
def new(num_buckets=256):
    """Initializes a Map with the given number of buckets.用给定的总数初始化一个映射"""
    aMap = []
    for i in range(0, num_buckets):
        aMap.append([])
    return aMap

# 调用Python内建的函数hash()将字符串转换为一组数字，
# 并使用%取余数运算符将返回的值固定在aMap的长度以内
def hash_key(aMap, key):
    """Given a key this will create a number and the convert it to
    an index for the aMap's buckets."""
    return hash(key) % len(aMap)

# 返回指定aMap中对应key的列表
def get_bucket(aMap, key):
    """Given a key, find the bucket where it would go."""
    bucket_id = hash_key(aMap, key)
    return aMap[bucket_id]

# 返回一个元祖，i表示key对应于aMap中的索引，k就是key本身，v是key对应的值
def get_slot(aMap, key, default=None):
    """
    Returns the index, key, and value of a slot found in a bucket.
    Returns -1, key, and default (None if not set) when not found.
    """
    bucket = get_bucket(aMap, key)

    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            return i, k, v
    return -1, key, default

# 用于查找aMap中对应key的值并返回
def get(aMap, key, default=None):
    """Gets the value in a bucket for the given key, or the default."""
    i, k, v = get_slot(aMap, key, default)
    return v

# 用于设置aMap中指定key对应列表的值，
# 如果指定key对应的列表已经存在则修改它的值，如果不存在则追加一个
def set(aMap, key, value):
    """Sets the key to the value, replacing any existing value."""
    bucket = get_bucket(aMap, key)
    i, k, v = get_slot(aMap, key)
    bucket.append((key, value))
    # if i >= 0:
    #     # the key exists, replace it
    #     bucket[i] = (key, value)
    # else:
    #     # the key does not, append to create it
    #     bucket.append((key, value))

# 删除一个key
def delete(aMap, key):
    """Deletes the given key from the Map."""
    bucket = get_bucket(aMap, key)

    if len(bucket) > 0:
        bucket.clear()
    # for i in range(len(bucket)):
    #     k, v = bucket[i]
    #     if key == k:
    #         del bucket[i]
    #         break

# 打印指定aMap中的所有列表值
def list(aMap):
    """Prints out what's in the Map."""
    for bucket in aMap:
        if bucket:
            for k, v in bucket:
                print(k, v)