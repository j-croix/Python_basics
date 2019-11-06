time = int(input())
minutes = (time // 60) % 60
hours = (time // 3600) % 24
seconds = time %60
print(hours, str(minutes).zfill(2), str(seconds).zfill(2), sep=':')
