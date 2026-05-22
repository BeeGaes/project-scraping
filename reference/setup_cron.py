from crontab import CronTab

cron = CronTab(user=True)

job = cron.new(
    command='"/mnt/d/dicoding/Belajar Fundamental Pemrosesan Data/scraping-exercise/venv/bin/python" "/mnt/d/dicoding/Belajar Fundamental Pemrosesan Data/scraping-exercise/intermediate_scraping.py" >> /home/jihad/scraping.log 2>&1',
    comment='Scraping bookstoscrape'
)

job.minute.every(3)

cron.write()

print('Scraping data sudah dijadwalkan.')