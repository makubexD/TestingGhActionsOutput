from tqdm import tqdm
import time
import os

# for i in tqdm(range(100), ncols=100, disable=True):
#     time.sleep(0.1)


# from rich.progress import Progress
# import time

# with Progress() as progress:
#     task = progress.add_task("[cyan]Processing...", total=900)
#     for i in range(900):
#         progress.update(task, advance=1)
#         time.sleep(0.1)

print("BEGIN = To check if GH")
print(os.getenv('GITHUB_ACTIONS'))
print("END = To check if GH")

for i in tqdm(range(900), miniters=10):
    time.sleep(0.1)



