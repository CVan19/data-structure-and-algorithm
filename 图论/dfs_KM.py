import json
import numpy as np

def findpath(x, left_num, right_num, left_vis, right_vis, left_ver, right_ver, weight, match):
    left_vis[x] = True #左边第x个agent记录进当前增广路中(从0开始数)
    for y in range(right_num): #y表示右边第几个agent，从0开始数
        if (right_vis[y] == False) and (left_ver[x] + right_ver[y] == weight[x, y]): #右边agent没有处在当前增广路中且左右两者的顶标和等于它们之间的边的权重
            right_vis[y] = True #第y个订单记录进当前增广路中
            if match[y] == None or findpath(match[y], left_num, right_num, left_vis, right_vis, left_ver, right_ver, weight, match):
                match[y] = x #匹配成功
                return True
    return False

def KM(left_num, right_num, left_ver, right_ver, weight, match):
    for x in range(left_num): #x表示左边第几位agent，从0开始数
        while True:
            left_vis = [False] * left_num #记录司机是否处在当前的增广路中
            right_vis = [False] * right_num #记录订单是否处在当前的增广路中
            if findpath(x, left_num, right_num, left_vis, right_vis, left_ver, right_ver, weight, match): #如果当前左边的agent匹配成功，继续为左边下一个agent匹配
                break
            #若未匹配到订单，则调整顶标值
            delta = float('inf')
            '''
            for i in range(left_num):
                if left_vis[i] == True: #如果左边的这个agent在增广路中
                    for j in range(right_num):
                        if right_vis[j] == False: #如果右边的这个agent不在增广路中
                            delta = min(delta, left_ver[i] + right_ver[j] - weight[i, j]) #找最小的delta
            #左边在增广路中的agent顶标减delta
            for i in range(left_num):
                if left_vis[i] == True:
                    left_ver[i] -= delta
            #右边在增广路中的agent顶标加delta
            for j in range(right_num):
                if right_vis[j] == True:
                    right_ver[j] += delta
            '''
            #向量化操作
            tmp_right_vis = [not x for x in right_vis]
            tmp_left_ver = left_ver[left_vis].reshape(-1,1)
            tmp_right_ver = right_ver[tmp_right_vis].reshape(1,-1)
            tmp_weight = weight[np.ix_(left_vis, tmp_right_vis)].reshape(tmp_left_ver.size, tmp_right_ver.size)
            delta = np.min(-tmp_weight +tmp_left_ver +tmp_right_ver)
            left_ver[left_vis] -= delta
            right_ver[right_vis] += delta
    return

if __name__ == '__main__':
    order_ids = ['D','E','F'] 
    driver_ids = ['A','B','C']
    num_orders = len(order_ids)
    num_drivers = len(driver_ids)
    dispatch_action = []
    match = dict()
    left_num, right_num = num_drivers, num_orders
    weight = np.array([[15,12,8], [14,6,8], [13,12,10]])
    for j in range(right_num):
        match[j] = None
    left_ver = np.max(weight, axis=1).astype('float64')
    right_ver = np.zeros(right_num, dtype='float64')
    KM(left_num, right_num, left_ver, right_ver, weight, match)
    for key, value in match.items():
        dispatch_action.append(dict(order_id=order_ids[key], driver_id=driver_ids[value]))
    print(dispatch_action)