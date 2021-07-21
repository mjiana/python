# 시간 감각을 맞춰보는 프로그램

# 10초 경과를 정확히 맞춰보기
import time

input("엔터를 누르고 10초를 셉니다.")
start = time.time()  # 현재 시간에 대한 타임스탬프
# time()은 소수로 리턴하여 정수는 초단위, 소수는 마이크로 초단위
print(start)  # 1626230974.9546428
input("10초가 되었다면 엔터를 치세요")
end = time.time()  # 현재 시간
elapse = end - start
print("소요시간", elapse, "초")
print("시간 차", abs(elapse-10), "초")

# 시간에 대한 출력값
import time
tm = time.gmtime(time.time())
print(tm)
# time.struct_time(
    # tm_year=2021, tm_mon=7, tm_mday=14,
    # tm_hour=2, tm_min=49, tm_sec=34,
    # tm_wday=2, tm_yday=195, tm_isdst=0
# )

# local time
import time
ltm = time.localtime(time.time())
print("year", ltm.tm_year)
print("month", ltm.tm_mon)
print("day", ltm.tm_mday)
print("hour", ltm.tm_hour)
print("min", ltm.tm_min)
print("sec", ltm.tm_sec)

# 
import datetime
now = datetime.datetime.now()
print(now)  # 2021-07-14 11:58:49.833109