'''
背景：
当前需要维护一个公司的人员信息。每位员工都有且仅有一位直属的上司，同时可能有多位下属。

需要解决的问题：
已经得到了一组数据，记录了每个人的上司是谁。

业务上的查询需求有如下：
1. 得到一颗完整的上下属的树结构
2. 计算每个人有几位下属人员

实例：
岗位信息：("老大", "老二"), ("老大", "老三"), ("老三", "老三老大"), ("老大", "老四"),
输出：
{
    "name": "老大",
    "val": 4,//下级有老二，老三，老四，老三老大，共四个
    "childs": [
        {
            "val": 0,
            "childs": [],
            "name": "老四"
        },
        {
            "val": 1,
            "childs": [
                {
                    "val": 0,
                    "childs": [],
                    "name": "老三老大"
                }
            ],
            "name": "老三"
        },
        {
            "val": 0,
            "childs": [],
            "name": "老二"
        }
    ]
}
'''
# coding=utf-8
import json


class Node:
    def __init__(self, _name):
        self.name = _name
        self.val = 0
        self.childs = list()

    """
    题目：从当前节点开始，输出从当前节点开始的树结构转换成json格式后返回
    """

    def node2json(self):
        result = '{"name":%s,"val":%s,"childs":%s}' % (
            self.name, self.val, [] if self.val == 0 else ','.join([item.node2json() for item in self.childs])
        )

        return result

    """
    题目：更新当前node与下级node的val，val的值等于该node下一共有多少个子节点
    """

    def count_val(self):
        self.val = len(self.childs)
        for item in self.childs:
            item.count_val()


class Solve:
    def __init__(self, root_name):
        # 初始化根节点
        self.root_node = Node(root_name)
        # 边
        self.relations = list()
        # 节点list
        self.node_list = list()
        self.node_list.append(self.root_node)

    """
    题目：通过输入的各条边关系，创建出树结构，并返回根节点
    如：机器学习,线性模型。则线性模型node是机器学习node的child
    """

    def build(self):
        # todo
        self.relations_dict = {}
        for parent, child in self.relations:
            if parent in self.relations_dict:
                self.relations_dict[parent].append(child)
            else:
                self.relations_dict[parent] = [child, ]
        current_node = self.root_node
        self.dfs_build(current_node)

    def dfs_build(self, current_node: Node):
        if current_node.name not in self.relations_dict:
            return
        childs = self.relations_dict[current_node.name]
        for child in childs:
            node = Node(child)
            current_node.childs.append(node)
            self.dfs_build(node)

    def run(self, relations):
        self.relations = relations
        self.build()
        self.root_node.count_val()
        print(json.dumps(self.root_node.node2json(), ensure_ascii=False, indent=4))


if __name__ == '__main__':
    # 根节点名为机器学习,假装是人名
    ans = Solve("机器学习")
    # 有如下的边
    relations = [('机器学习', '线性模型'), ('机器学习', '神经网络'), ('神经网络', '神经元模型'), ('机器学习', '强化学习'), ('线性回归', '最小二乘法'),
                 ('线性模型', '线性回归'), ('神经网络', '神经元模型'), ('神经元模型', '激活函数'), ('多层网络', '感知机'), ('多层网络', '连接权'),
                 ('神经网络', '多层网络'), ('强化学习', '有模型学习'), ('强化学习', '免模型学习'), ('强化学习', '模仿学习'), ('有模型学习', '策略评估'),
                 ('有模型学习', '策略改进'), ('免模型学习', '蒙特卡洛方法'), ('免模型学习', '时序差分学习'), ('模仿学习', '直接模仿学习'), ('模仿学习', '逆强化学习')]
    # 完成以上创建树结构，计算子节点数和转换为json格式并输出
    ans.run(relations)
