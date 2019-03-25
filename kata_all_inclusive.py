def contain_all_rots(strng, arr):
    if not strng:
        return True
    from collections import deque
    raw_list = [x for x in strng]
    dq = deque(raw_list, len(raw_list))
    for i in range(len(raw_list)):
        if ''.join(dq) not in arr:
            return False
        dq.rotate()
    return True
print(contain_all_rots("", ["bsjq", "qbsj"]))