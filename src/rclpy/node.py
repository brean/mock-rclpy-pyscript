class Node:
    def __init__(self, name):
        print('init Node ' + name)

    def create_publisher(self, clz, topic, hz):
        print(
            f'create publisher for topic {topic}, type {clz.__name__}')
