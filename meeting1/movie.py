# hh:mm:ss
# 3605
# 01:00:05
total_seconds = int(input("Insert movie length in seconds: "))
hours, seconds = divmod(total_seconds, 3600)
total_minutes, seconds = divmod(total_seconds, 60)
minutes = (total_seconds // 60) % 60
print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")