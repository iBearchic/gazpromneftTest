# Имеется папка с файлами
# Реализовать удаление файлов старше N дней

import os
import time

def delete_old_files(directory, N):
    now = time.time()
    cutoff = now - (N * 86400)  # 86400 секунд в дне

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            # Получение времени последней модификации
            file_mtime = os.path.getmtime(file_path)
            if file_mtime < cutoff:
                os.remove(file_path)
                print(f"Удаление файла: {file_path}")
