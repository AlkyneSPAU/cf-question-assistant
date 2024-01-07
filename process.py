import json
import time
import codecs


def Process() -> str:
    """
    通过获取目标题数target计算未做题数
    返回未做题数
    """

    # 获取目标题数
    with codecs.open('settings.json', 'r', 'utf-8') as f:
        target = json.load(f)['target']

    # 获取datas.json中的数据
    with open('datas.json', 'r') as file:
        data = json.load(file)
    var = data['data'][1:]

    # 统计已完成题数，并计算还有几道题没做
    finished = 0
    for elem in var:
        if elem['When'].split()[0] != time.strftime('%b/%d/%Y'):
            continue
        if elem['Verdict'] not in ['Accepted', 'Happy New Year!']:
            continue
        finished += 1

    # 返回未做题数
    if target - finished == 0:
        return "恭喜你完成了今日刷题任务!"
    elif target - finished < 0:
        return f"您已超量完成{finished - target}题,厉害!"
    return f"您还有{target - finished}题未完成,继续加油吧!"


if __name__ == '__main__':
    left = Process()
    if left:
        print(left)
    else:
        print('Finished!')
