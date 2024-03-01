import time

local_t = time.localtime(time.time())
mon = 0

if (local_t.tm_mon < 10):
    mon = '0' + str(local_t.tm_mon)
else:
    mon = str(local_t.tm_mon)
print(str(local_t.tm_year) + '-' + mon + '-' + str(local_t.tm_mday))